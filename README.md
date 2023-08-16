# AI AutoPilot

AI Autopilot represents a cutting-edge deep learning initiative that leverages advanced computer vision methodologies to forecast precise steering angles for self-driving automobiles. Enclosed within this repository is the comprehensive codebase and model framework that empowers an artificial intelligence system to independently guide a vehicle, utilizing an intricate analysis of input images sourced from a forward-oriented camera.
### Demo:
<img width="491" alt="Screenshot 2023-07-24 225732" src="https://github.com/yash1017/Auto_Pilot/blob/55f2b4aa120ef1486f57743cf51769c7aeccd05b/Demo/Screenshot%202023-07-24%20225901.png">

<img width="436" alt="Screenshot 2023-07-24 225901" src="https://github.com/yash1017/Auto_Pilot/blob/55f2b4aa120ef1486f57743cf51769c7aeccd05b/Demo/Screenshot%202023-07-24%20231035.png"> 

## Installation

- Clone the repository:

```bash
  git clone https://github.com/Dileep-56/AI-AutoPilot.git
```
- Install the required dependencies:
```bash
  pip install -r requirements.txt
```
- Download the dataset [here](https://www.kaggle.com/datasets/roydatascience/training-car/download?datasetVersionNumber=1) and place it in the data directory.
- Run `model_training.py` file in src/components/model_training.py
- Then specify the path of the images and path of the saved model in `evaluate_model.py` file in src/components/evaluate_model.py

## Project Architecture:
<img width="768" alt="Project Architectur" src="https://github.com/Dileep-56/AI-AutoPilot/assets/121457201/3386acae-3bb8-4ddf-84dd-b61e31b87f2b">

### Convolutional Neural Network Model Architecture:
<img width="557" alt="image" src="https://github.com/Dileep-56/AI-AutoPilot/assets/121457201/3e464d8f-cdc9-41da-923b-753a8fa70d45">

## Notice:
This code is solely intended for statistical analysis; it is in no way intended for use in any kind of application or testing.
Under No circumstances should anyone ever operate a vehicle while using computer vision software that has been trained using this code, or any other type of homemade software for that matter. Even if you believe you know what you're doing, using your own self-driving software in a car is exceedingly risky. 

## References:
- This is a implementation of [Nvidia paper](https://arxiv.org/pdf/1604.07316.pdf), this document provides complete architecture of how this model should be done.
- For Deep Learning, you can follow this book [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems, Third Edition](https://www.amazon.in/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/9355421982).
