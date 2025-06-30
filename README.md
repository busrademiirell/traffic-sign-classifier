# Traffic Sign Classifier

This project implements a **Traffic Sign Classification** system using deep learning techniques. The goal is to accurately identify various traffic signs from images, which is a fundamental task for autonomous driving and advanced driver-assistance systems (ADAS).

---

## Project Overview

- **Model:** A convolutional neural network (CNN) trained on a labeled traffic sign dataset.  
- **Preprocessing:** Input images are resized, converted to grayscale, histogram equalized, and normalized before prediction.  
- **Evaluation:** Includes metrics such as accuracy and a confusion matrix to analyze model performance.  
- **User Interface:** An interactive web app built with Gradio to allow users to upload images and get real-time predictions.

---

## Features

- Robust image preprocessing pipeline to improve prediction accuracy.  
- Easy-to-use Gradio-based web interface for live testing.  
- Detailed performance analysis with visualization of confusion matrix.  
- Model and preprocessing code fully available for reproducibility.

---

## Dataset

This project uses the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset, which contains over 50,000 labeled images of various traffic signs. It is a popular benchmark dataset for traffic sign classification tasks and provides a wide variety of traffic sign types and lighting conditions.

- Number of classes: 43
- Number of images: ~50,000
- Source: [GTSRB Dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset)

## Live Demo

Try the live demo of the Traffic Sign Classifier here:  
👉 [https://huggingface.co/spaces/bsrademirell/traffic-sign-classifier](https://huggingface.co/spaces/bsrademirell/traffic-sign-classifier)  

Upload your own images and see the model's predictions instantly!

---
## How to Use

```bash
# 1. Clone this repository
git clone https://github.com/busrademiirell/traffic-sign-classifier.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Gradio app
python app.py
```
## Technologies Used
- Python
- TensorFlow / Keras
- OpenCV
- Gradio
- NumPy
- Matplotlib & Seaborn (for analysis & visualization)

## Future Improvements
- Increase dataset size and diversity for better generalization.
- Optimize model architecture for faster inference.
- Deploy the app on cloud platforms for scalable access.
- Integrate real-time video input for live traffic sign detection.

## About Me
I am a passionate student and aspiring machine learning engineer, focusing on computer vision applications. This project demonstrates my ability to develop end-to-end ML solutions, including data preprocessing, model training, evaluation, and deployment.


