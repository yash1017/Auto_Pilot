import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

model = tf.keras.models.load_model("path_of_saved_model_in_h5_format.h5")
real_world_images = "path_of_the_testing_images"

def real_world_img(real_world_images):
    for filename in os.listdir(real_world_images):
        image = real_world_images+filename
        image = cv2.imread(image)
        plt.imshow(image)
        plt.show()
        image = cv2.resize((cv2.cvtColor(image, cv2.COLOR_RGB2HSV))[:, :, 1], (200, 66))
        image = image/255.0
        image = np.expand_dims(image, axis=0)
        image = image.reshape(image.shape[0], 200, 66, 1)
        print("The predicted angle is",list(model.predict(image)*(180/3.14159265))[0])
print(real_world_img(real_world_images))