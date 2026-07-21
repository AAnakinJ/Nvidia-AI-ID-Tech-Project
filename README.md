# Nvidia-AI-ID-Tech-Project
# 🚦 Traffic Sign & Light Classifier (Jetson Orin Nano)

This project is an artificial intelligence model trained to detect and classify traffic signs. Specifically, it is capable of distinguishing between **speed limit signs** and **traffic lights**. 

The model was trained using the **ImageNet** architecture via NVIDIA's [jetson-inference](https://github.com/dusty-nv/jetson-inference) library and is optimized to run efficiently on a **Jetson Orin Nano**.


## 🛠 Hardware & Prerequisites

*   **Hardware:** NVIDIA Jetson Orin Nano
*   **Framework:** `jetson-inference` 
*   **Camera:** USB Webcam (optional, for real-time inference)

## 📊 Dataset

The dataset used for training is sourced from **Kaggle**. It has been restructured to be compatible with the classification requirements of `jetson-inference`. 

The dataset is split using the following file system:

dataset/
├── train/       # Training images
├── val/         # Validation images
└── test/        # Testing images
