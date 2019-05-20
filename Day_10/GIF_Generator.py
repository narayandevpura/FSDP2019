# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:13:48 2019

@author: Narayan Devpura
"""

"""

Code Challenge 4
GIF Creator

A program that puts together multiple images (PNGs, JPGs, TIFFs) to make a smooth 
GIF that can be exported. Make the program convert small video files to GIFs as 
well.

"""

from PIL import Image
images = []
names=['apple.png','crown.jfif','egg.jfif','food.jfif','happy.jfif','what.jfif']
for n in names:
    frame = Image.open(n)
    images.append(frame)

# Save the frames as an animated GIF
images[0].save('newgif.gif',
               save_all=True,
               append_images=images[1:],
               duration=200,
               loop=0)

