# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:46:51 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""
img = input('Enter image name: ')
from PIL import Image
img = Image.open('sample1.jpg').convert('LA')
img.save('img_geyscale.png')
img.show()

img_rotate = img.transpose(Image.ROTATE_270)
img_rotate.save('img_rotate.png')

width, height = img_rotate.size   # Get dimensions

left = (width - 160)/2
top = (height - 204)/2
right = (width + 160)/2
bottom = (height + 204)/2

img_crop = img_rotate.crop((left, top, right, bottom))
img_crop.show()

img_Thumbnail = img_rotate.thumbnail((75,75))
img_Thumbnail.show()