 
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense, Conv2D, MaxPooling2D
from keras.optimizers import Adam
import data_transformation 

from src.logger import logging

#Creating the model
def create_model(learning_rate=0.001):
    model = Sequential()
    model.add(Conv2D(filters=24,kernel_size=(5,5),strides=(2,2),activation='relu',padding='valid',input_shape=(200,66,1)))
    model.add(Conv2D(filters=36,kernel_size=(5,5),strides=(2,2),activation='relu',padding='valid'))
    model.add(Conv2D(filters=48,kernel_size=(5,5),strides=(2,2),activation='relu',padding='valid'))
    model.add(Conv2D(filters=64,kernel_size=(3,3),strides=(1,1),activation='relu',padding='valid'))
    model.add(Conv2D(filters=64,kernel_size=(3,3),strides=(1,1),activation='relu',padding='valid'))


    model.add(Flatten())

    model.add(Dense(units=1152,activation='relu'))
    model.add(Dropout(rate=0.5))

    model.add(Dense(units=100,activation='relu'))
    model.add(Dropout(rate=0.5))

    model.add(Dense(units=50,activation='relu'))
    model.add(Dropout(rate=0.5))

    model.add(Dense(units=10,activation='relu'))
    model.add(Dropout(rate=0.5))

    model.add(Dense(units=1,activation='linear'))


    model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=learning_rate))
    
    return model

logging.info("Started creating the model")
model = create_model(learning_rate=0.0001)
logging.info("Created the model")
model.fit(data_transformation.X_train,data_transformation.y_train, validation_data=(data_transformation.X_val,data_transformation.y_val), epochs=60,batch_size=96)
logging.info("Trained the model")
#Saving the model.
model.save("Saved_Model.h5")
logging.info("Saved the model as saved_model in HDF5 format")
