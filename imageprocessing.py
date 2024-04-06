from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from flask import Flask, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('webcam.html')

# Your existing code refactored into a function
def get_prediction():
    model = load_model("./keras_model.h5", compile=False)
    class_names = open("labels.txt", "r").readlines()
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


@app.route('/predict', methods=['GET'])
def predict():
    class_name, confidence = get_prediction()
    return jsonify({'class': class_name, 'confidence': float(confidence)})

if __name__ == '__main__':
    app.run(debug=True)
