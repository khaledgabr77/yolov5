#!/usr/bin/python

import os 
from sklearn.model_selection import train_test_split
import shutil

os.listdir()

images_path = "drone-net/images/"
os.listdir(images_path)

images = os.listdir(images_path)
images = sorted(images)
labels = [file.replace(".jpg",".txt") for file in images]

len(images)
len(labels)

images = ["drone-net/images/"+file for file in images]
labels = ["drone-net/normalized-labels/"+file for file in labels]

train_imgs ,val_imgs,train_labels,val_labels = train_test_split(images,labels,test_size = 0.2,random_state = 42)

print(len(train_imgs))
print(len(train_labels))
print(len(val_imgs))
print(len(val_labels))

source_dir = 'drone-net/dataset/'

def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False

# Move the splits into their folders
move_files_to_folder(train_imgs, source_dir+'images/train')
move_files_to_folder(val_imgs, source_dir+'images/val/')

move_files_to_folder(train_labels, source_dir+'labels/train/')
move_files_to_folder(val_labels, source_dir+'labels/val/')

