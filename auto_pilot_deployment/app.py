from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from PIL import Image  # Import Image from the Pillow library

model = load_model('auto_pilot_deployment\Saved_Model-Copy1.h5')  # Update the path to your model

app = Flask(__name__)

# Define the correct path for the 'uploads' folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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
    if image:
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)
        image = Image.open(image_path)  # Use Image from the Pillow library to open the image
        # Add your image preprocessing and prediction code here
        # Example:
        image = cv2.resize((cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV))[:, :, 1], (200, 66))
        # if image.max()==255.0:
        image = image/255.0
        image = np.expand_dims(image, axis=0)
        image = image.reshape(image.shape[0], 200, 66, 1)
        steering_angle = list(model.predict(image)*(180/3.14159265))[0]
        # Return the predicted angle
        return f'The predicted angle is <h1>{steering_angle}</h1> degrees'

if __name__ == '__main__':
    app.run(debug=True)

#         image = real_world_images+filename
#         image = imread(image)
#         plt.imshow(image)
#         plt.show()
#         image = cv2.resize((cv2.cvtColor(image, cv2.COLOR_RGB2HSV))[:, :, 1], (200, 66))
# #         image = image/255.0
#         image = np.expand_dims(image, axis=0)
#         image = image.reshape(image.shape[0], 200, 66, 1)
#         print("The predicted angle is",list(model.predict(image)*(180/3.14159265))[0])