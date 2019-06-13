#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:42:16 2019

@author: narayan
"""


import cv2
import imutils.paths as paths

import face_recognition
import pickle
import os
dataset = "/home/narayan/Desktop/Forsk2019/Day_27/nd/"# path of the data set 
module = "encoding1.pickle" # were u want to store the pickle file 

imagepaths = list(paths.list_images(dataset))
knownEncodings = []
knownNames = []
for (i, imagePath) in enumerate(imagepaths):
    print("[INFO] processing image {}/{}".format(i + 1,len(imagepaths)))
    name = imagePath.split(os.path.sep)[-2]
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)	
    boxes = face_recognition.face_locations(rgb, model= "hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
       knownEncodings.append(encoding)
       knownNames.append(name)
       print("[INFO] serializing encodings...")
       data = {"encodings": knownEncodings, "names": knownNames}
       output = open(module, "wb") 
       pickle.dump(data, output)
       output.close()