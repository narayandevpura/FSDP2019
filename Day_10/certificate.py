# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:45:06 2019

@author: Narayan Devpura
"""

"""
Code Challenge 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts
"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv

with open('students.csv', 'r') as stu:
    reader = csv.reader(stu, delimiter = ',')
    next(reader)
    for row in reader:
        name = row[0]
        college = row[1]
        branch = row[2]
        if int(row[3]) == 2:
            year = row[3] + 'nd year'
        elif int(row[3]) == 3:
            year = row[3] + 'rd year'
        else:
            year = row[3] + 'th year'
        _class = year + '  ' + branch  
        
        img = Image.open("c_temp.jpg")
        draw = ImageDraw.Draw(img)
        selectFont1 = ImageFont.truetype(font = "georgiab.ttf", size = 28, layout_engine = None)
        selectFont2 = ImageFont.truetype(font = "georgiab.ttf", size = 24, layout_engine = None)
        
        draw.text( (400,343), name, (20,20,20), font = selectFont1)
        
        if len(college) < 8:
           draw.text( (270,398), college, (20,20,20), font = selectFont2)
        else:
            draw.text( (235,398), college, (20,20,20), font = selectFont2)
        
        if len(_class) < 15 : 
           draw.text( (640,398), _class, (20,20,20), font = selectFont2)
        else:
            draw.text( (595,398), _class, (20,20,20), font = selectFont2)
            
        img.save( name.split()[0]+name.split()[1][0]+'.jpg', "JPEG", resolution=100.0)