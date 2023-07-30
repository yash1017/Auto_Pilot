import sys
import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
import data_ingestion 


def norm_array(image_path):
    #Reading the image
    image = cv2.imread(image_path)
    #Resizing the image to (200,66) & converting the image to HSV color by extracting the second component of the image.
    image = cv2.resize((cv2.cvtColor(image, cv2.COLOR_RGB2HSV))[:, :, 1], (200, 66))
    #Normalising the image.
    image = image/255.0
    return image

X = []
y = []


try:
    logging.info("Started Normalising the images")
    for i in range(0,len(data_ingestion.xs)):
        X.append(norm_array(data_ingestion.xs[i]))
        y.append(data_ingestion.ys[i])
        print(i)
    logging.info("Normalisation done! and starting to split into train_test_split")
except Exception as e:
    raise CustomException(e,sys)
        
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2,random_state=84)

X_train=np.array(X_train)
X_val=np.array(X_val)
y_train=np.array(y_train)
y_val=np.array(y_val)
logging.info("Converting the image file to np.array")

X_train = X_train.reshape(X_train.shape[0], 200, 66, 1)
X_val = X_val.reshape(X_val.shape[0], 200, 66, 1)
logging.info("Changed the shape of training and validation data into (len,200,66,1)")

        
    
    
    
    
        
    
