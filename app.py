
import gradio as gr
import numpy as np
from PIL import Image
import cv2
from tensorflow.keras.models import load_model

model = load_model('model.h5')

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def equalize(img):
    return cv2.equalizeHist(img)

def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img / 255.0
    return img

def predict(img):
    img = np.array(img)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    img = img.reshape(1, 32, 32, 1)
    pred_probs = model.predict(img)
    pred_class = np.argmax(pred_probs, axis=1)[0]
    return f"Predicted class: {pred_class}"

iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Traffic Sign Classifier"
)

iface.launch()
