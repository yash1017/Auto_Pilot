#Importing all the Libraries
import os
import sys
from src.exception import CustomException
from src.logger import logging

xs = []
ys = []

def load_images_from_directory(data_directory):
    try:
        logging.info("Reading and Splitting the dataset into x and y variables")
        #Lableling the images 
        with open(data_directory) as f:
            for line in f:
                xs.append("D://driving_dataset/" + line.split()[0])
                ys.append(float(line.split()[1]) * 3.14159265 / 180)
        logging.info("Splitting of Data done!")
        return xs,ys
        

    except Exception as e:
        raise CustomException(e,sys)
        
        
data_directory = "D://driving_dataset/data.txt"
xs, ys = load_images_from_directory(data_directory)


