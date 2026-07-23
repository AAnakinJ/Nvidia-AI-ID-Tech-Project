# Nvidia-AI-ID-Tech-Project
# 🚦 Traffic Sign & Light Classifier (Jetson Orin Nano)

This project is an artificial intelligence model trained to detect and classify traffic signs. Specifically, it is capable of distinguishing between **speed limit signs** and **traffic lights**. 

The model was trained using the **ImageNet** architecture via NVIDIA's [jetson-inference](https://github.com/dusty-nv/jetson-inference) library and is optimized to run efficiently on a **Jetson Orin Nano**.

![AI output example](https://drive.google.com/file/d/1ibY1r_sEN4gnIeN8wt-2JFWR9x5YJAdw/view?usp=sharing)


## 🛠 Hardware & Prerequisites

*   **Hardware:** NVIDIA Jetson Orin Nano
*   **Framework:** `jetson-inference` 
*   **Camera:** USB Webcam (optional, for real-time inference)

## 📊 Dataset

The dataset used for training is sourced from **Kaggle**. It has been restructured to be compatible with the classification requirements of `jetson-inference`: [Data Set](https://www.kaggle.com/datasets/pkdarabi/cardetection)

The dataset is split using the following file system:

dataset/

├── train/       # Training images

├── val/         # Validation images

└── test/        # Testing images


## The Algorithm

[Train.py](https://docs.google.com/document/d/1Ntqpt_Va4BI6mHEDFuLBjUmVQF0ROEfFfOuRMVm1d_w/edit?usp=sharing)

[reorganize.py](https://docs.google.com/document/d/1l7d2_Vh9qECCyrUtNQrFlQvSz6y-rbdPo-_2a0v-Tuk/edit?usp=sharing)

[onnx_export.py](https://docs.google.com/document/d/1m6WHlbUfmlXYAtZTbKSXt6am-Sl5ju9eiKVh-noMfdo/edit?usp=sharing)

[onnx_validate.py](https://docs.google.com/document/d/1nJQ0YYCak-djCjwA1_2J4yRhvhErDhOhr-4yYCYtfAk/edit?usp=sharing)

## Running this project

<pre><code>#!/bin/bash
curl -L -o ~/Downloads/cardetection.zip \
  https://www.kaggle.com/api/v1/datasets/download/pkdarabi/cardetection</code></pre>

<pre><code>cd jetson-inference/python/training/classification/data</code></pre>


[View a quick video explanation here](https://drive.google.com/file/d/1DII7u_ZH6H3vxy3KSRnmuQ2As5q0aC9Z/view?usp=sharing)

