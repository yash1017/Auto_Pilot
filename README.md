# AI AutoPilot

AI Autopilot represents a cutting-edge deep learning initiative that leverages advanced computer vision methodologies to forecast precise steering angles for self-driving automobiles. Enclosed within this repository is the comprehensive codebase and model framework that empowers an artificial intelligence system to independently guide a vehicle, utilizing an intricate analysis of input images sourced from a forward-oriented camera.
### Demo:
<img width="436" alt="Screenshot 2023-07-24 225732" src="https://github.com/yash1017/Auto_Pilot/blob/55f2b4aa120ef1486f57743cf51769c7aeccd05b/Demo/Screenshot%202023-07-24%20225901.png">

<img width="436" alt="Screenshot 2023-07-24 225901" src="https://github.com/yash1017/Auto_Pilot/blob/55f2b4aa120ef1486f57743cf51769c7aeccd05b/Demo/Screenshot%202023-07-24%20231035.png"> 

## Installation
- Install the required dependencies:
```bash
  pip install -r requirements.txt
```
- Download the dataset [here](https://www.kaggle.com/datasets/roydatascience/training-car/download?datasetVersionNumber=1) and place it in the data directory.
- Run `model_training.py` file in src/components/model_training.py
- Then specify the path of the images and path of the saved model in `evaluate_model.py` file in src/components/evaluate_model.py

- Clone the repository:

```bash
  git clone https://github.com/yash1017/AutoPilot.git
```



### Convolutional Neural Network Model Architecture:
<img width="557" alt="image" src="https://github.com/yash1017/Auto_Pilot/blob/25353b76787237c75d3d79a653e87ec28cfbfa3e/real_world_img_testing/cnn_arch.png">

## Project Architecture:
<img width="768" alt="Project Architectur" src="https://github.com/yash1017/Auto_Pilot/blob/25353b76787237c75d3d79a653e87ec28cfbfa3e/real_world_img_testing/Proj_arch.png">
## References:
- This is a implementation of [Nvidia paper](https://arxiv.org/pdf/1604.07316.pdf), this document provides complete architecture of how this model should be done.
- For Deep Learning, you can follow this book [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems, Third Edition](https://www.amazon.in/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/9355421982).
