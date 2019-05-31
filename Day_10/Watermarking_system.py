# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:07:06 2019

@author: Narayan Devpura
"""

"""

Code Challenge 3

Watermarking Application

Have some pictures you want copyright protected? Add your own logo or text lightly 
across the background so that no one can simply steal your graphics off your site. 
Make a program that will add this watermark to the picture.

"""
"""
from PIL import Image
from PIL import ImageDraw

##def create_watermark(image_path, final_image_path, watermark, hires=False):
#main = Image.open('water.jfif')
#mark = Image.open(watermark)
#mark = mark.rotate(30, expand=1)
#mask = mark.convert('L').point(lambda x: min(x, 25))
#mark.putalpha(mask)
#mark_width, mark_height = mark.size
#main_width, main_height = main.size
#aspect_ratio = mark_width / mark_height
#new_mark_width = main_width * 0.4
#mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.ANTIALIAS)
#tmp_img = Image.new('RGBA', main.size)
#for i in range(0, tmp_img.size[0], mark.size[0]):
#    for j in range(0, tmp_img.size[1], mark.size[1]):
#        main.paste(mark, (i, j), mark)
#if not hires:
#    main.thumbnail((758, 1000), Image.ANTIALIAS)
#    main.save(final_image_path, 'JPEG', quality=75)
#else:
#    main.thumbnail((2048, 2048), Image.ANTIALIAS)
#    main.save(final_image_path, 'JPEG', quality=85)
#

#if __name__ == '__main__':
#    create_watermark('main_image.jpg', 'main_with_watermark.jpg', 'watermark.png', True)

new = Image.new(mode = 'RGB', size = (200,50),color = 'white')

drwa = ImageDraw.Draw(new)

drwa.text((0,0), text='who am i',size = (45), color = (255,0,0))

"""


from PIL import Image
image = Image.open('apple.png') 
print(image.size, image.format)


from PIL import Image, ImageDraw, ImageFont

image = Image.open('apple.png')
width, height = image.size


tag = Image.open('tag.png')
t_width, t_height = tag.size
tag = tag.rotate(45)

x = width - t_width
y = height - t_height

image.paste(tag, (x,y))

image.save('appless.png')