import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import random

def get_rand_img_path(folder="/../train/"):
    train_dir = os.getcwd() + folder
    train_files = os.listdir(train_dir)
    return train_dir + random.choice(train_files)

def get_img(label, folder="/../train/"):
    train_dir = os.getcwd() + folder
    path = os.path.join(train_dir,f"{label}-0.png")
    img = cv2.imread(path)
    return img

def get_label(img_path):
    filename = os.path.basename(img_path)
    label = filename.split('-')[0]
    return label

def get_rand_img():
    path = get_rand_img_path()
    label = get_label(path)
    img = cv2.imread(path)
    return img, label

def show_img(img, title=None):
    plt.figure()
    plt.axis("off")
    if title is not None:
        plt.title(title)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()