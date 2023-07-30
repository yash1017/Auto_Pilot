# AI AutoPilot

AI Autopilot is an innovative deep learning project that utilizes computer vision techniques to predict accurate steering angles for autonomous vehicles. This repository contains the codebase and model architecture that enables an AI system to autonomously steer a car by analyzing input images captured from a front-facing camera.
### Demo:
<img width="491" alt="Screenshot 2023-07-24 225732" src="https://github.com/Dileep-56/AI-AutoPilot/assets/121457201/ee928ecc-db27-402e-b3e3-42d8e245073b">

<img width="436" alt="Screenshot 2023-07-24 225901" src="https://github.com/Dileep-56/AI-AutoPilot/assets/121457201/74853d34-4df4-4039-99df-bf2275fe5d2f"> 

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
