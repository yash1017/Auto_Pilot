from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from PIL import Image
import io  # Import io for reading image data from the request

model = load_model('Saved_Model-Copy1.h5')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file part"
    image = request.files['image']
    if image.filename == '':
        return "No selected file"
    
    # Read and process the image directly from the request
    image_data = image.read()
    image = Image.open(io.BytesIO(image_data))
    
    # Add your image preprocessing and prediction code here
    # Example:
    image = cv2.resize((cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV))[:, :, 1], (200, 66))
    image = image/255.0
    image = np.expand_dims(image, axis=0)
    image = image.reshape(image.shape[0], 200, 66, 1)
    steering_angle = list(model.predict(image)*(180/3.14159265))[0]
    
    # Return the predicted angle
    return f'The predicted angle is <h1>{steering_angle}</h1> degrees'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
