#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:02:45 2019

@author: narayan
"""

"""
Facial Recognition + OpenCV Python

Facial recognition is a biometric software application capable of uniquely identifying or verifying 
a person by comparing and analyzing.

Things that you need in this project: OpenCV and face_recognition

The project is mainly a method for detecting faces in a given image by using OpenCV-Python and 
face_recognition module. The first phase uses camera to capture the picture of our faces which 
generates a feature set in a location of your PC.

• The face_recognition command lets you recognize faces in a photograph or folder full for photographs.

It has two simple commands

Face_ recognition- Recognise faces in a photograph or folder full for photographs.
face_detection - Find faces in a photograph or folder full for photographs.
For face recognition, first generate a feature set by taking few image of your face and create 
a directory with the name of person and save their face image.


Then train the data by using the Face_ recognition module.By Face_ recognition module the trained 
data is stored as pickle file (.pickle).

By using the trained pickle data, we can recognize face.

The main flow of face recognition is first to locate the face in the picture and the compare the 
picture with the trained data set.If the there is a match, it gives the recognized label.
(Ref: https://github.com/sriram251/-face_recognition)
"""


import os
import cv2

face_cascade = cv2.CascadeClassifier('/home/narayan/Desktop/Forsk2019/Day_27/material/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
path = "/home/narayan/Desktop/Forsk2019/Day_27/"   # path were u want store the data set
id = input('enter user name')

try:
    # Create target Directory
    os.mkdir(path+str(id))
    print("Directory " , path+str(id),  " Created ") 
except FileExistsError:
    print("Directory " , path+str(id) ,  " already exists")

sampleN=0;

while 1:

    ret, img = cap.read()
    frame = img.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        sampleN=sampleN+1;

        cv2.imwrite(path+str(id)+ "//" +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.waitKey(100)

    cv2.imshow('img',img)

    cv2.waitKey(1)

    if sampleN > 100:

        break

cap.release()

cv2.destroyAllWindows()





