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

Download the Dataset 
<pre><code>#!/bin/bash
curl -L -o ~/Downloads/cardetection.zip \
  https://www.kaggle.com/api/v1/datasets/download/pkdarabi/cardetection</code></pre>

Change directory
<pre><code>
cd jetson-inference/python/training/classification/data</code></pre>

You may need to create a subfolder to store the files in. This depends on if the dataset comes with one or not. In this case, it's required.


<pre><code>
Unzip the file from your downloads. The -d flag can be omitted if you didn't create a subfolder:
unzip ~/Downloads/your_dataset.zip -d subfolder_name</code></pre>

Now you will organize the Dataset (test/val/train)
<pre><code>
python3 reorganize.py</code></pre>

If you want the exact same project you will may be have to clean or divide the Dataset in only 2 classes


In your dataset directory create a new file. Name it labels.txt. In labels.txt, put each class of objects. Ensure that all of these are in alphabetical order. 

[labels.txt]()

then run the docker container: 


Ensure that all of these are in alphabetical order.

<pre><code>
cd ~/jetson-inference/
./docker/run.sh</code></pre>

Navigate into your classification folder:

<pre><code>
cd python/training/classification</code></pre>

<pre><code>
python3 train.py --model-dir=models/Your_Model data/dataset</code></pre>

and if you want to make the training shorter or longer change the 
<pre><code>epoch</code></pre>

<pre><code>
python3 train.py --epochs=10 --model-dir=models/Your_Model data/dataset</code></pre>

Run the ONNX export script:
<pre><code>
python3 onnx_export.py --model-dir=models/Your_Model</code></pre>

exit the docker container:
<pre><code>
Ctrl + d</code></pre>

Set the variables
<pre><code>
NET=models/Your_Model
DATASET=data/dataset</code></pre>

Run the AI
<pre><code>
imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/dataset/your_image_input output.jpg</code></pre>

Here a video on how the AI work basically 

[View a quick video explanation here](https://drive.google.com/file/d/1DII7u_ZH6H3vxy3KSRnmuQ2As5q0aC9Z/view?usp=sharing)

