var content1 = document.getElementById("content1");
var content2 = document.getElementById("content2");
var content3 = document.getElementById("content3");

var btn1 = document.getElementById("btn1");
var btn2 = document.getElementById("btn2");
var btn3 = document.getElementById("btn3");

const learnButton = document.getElementById("learnButton");
learnButton.addEventListener("click", openLearnTab);

function openHOME() {
    content1.style.transform = "translateX(0)";
    content2.style.transform = "translateX(100%)";
    content3.style.transform = "translateX(100%)";
    
    btn1.style.color = "#090c9b";
    btn2.style.color = "#000";
    btn3.style.color = "#000";
}
function openLEARN() {
    content1.style.transform = "translateX(100%)";
    content2.style.transform = "translateX(0)";
    content3.style.transform = "translateX(100%)";
    btn1.style.color = "#000";
    btn2.style.color = "#3066be";
    btn3.style.color = "#000";
}
function openABOUT() {
    content1.style.transform = "translateX(100%)";
    content2.style.transform = "translateX(100%)";
    content3.style.transform = "translateX(0)";
    btn1.style.color = "#000";
    btn2.style.color = "#000";
    btn3.style.color = "#b4c5e4";
}

function openLearnTab(){
    const url = "http://127.0.0.1:5000";
    window.open(url);
}