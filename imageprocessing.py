from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
import os
from io import BytesIO


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('webcam.html')

model = load_model("./LLMModels/keras_model.h5", compile=False)
class_names = open("./labels/labels.txt", "r").readlines()

# Your existing code refactored into a function
def get_prediction():
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    image_path = "./userimages/userimage.jpg"
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()  # strip() to remove newline characters
    confidence_score = prediction[0][index]
    
    return class_name, confidence_score


@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected for uploading'}), 400

    if file:
        # Convert the Image to the correct format for prediction
        image = Image.open(BytesIO(file.read())).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)  
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array

        # Predict
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index].strip()  
        confidence_score = prediction[0][index]

        return jsonify({'class': class_name, 'confidence': float(confidence_score)})


    return jsonify({'error': 'Error processing the image'}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

