import cv2
import os
import numpy as np
import random
from PIL import ImageFont, ImageDraw, Image
import arabic_reshaper
import math


def dist_between_points(pt1,pt2):
    return (pt1[0]-pt2[0],pt1[1]-pt2[1])
def xyxy_center(xyxy):
    return ((xyxy[0]+xyxy[2])//2,(xyxy[1]+xyxy[3])//2)

def put_text_to_img(img:Image,text:str,font:ImageFont.FreeTypeFont,origin:tuple):
    img=img.copy()
    xyxy=font.getbbox(text)
    xyxy=(xyxy[0]+origin[0],xyxy[1]+origin[1],xyxy[2]+origin[0],xyxy[3]+origin[1])
    origin_trans=dist_between_points(origin,xyxy_center(xyxy))
    # print(origin_trans)
    new_origin=(origin[0]+origin_trans[0],origin[1]+origin_trans[1])
    # print(origin,new_origin)
    draw=ImageDraw.Draw(img)
    draw.text(new_origin,text,(0,0,0),font)
    # img.show()
    return img

letters=[u'أ',u'ب',u'ج',u'د',u'ر',u'س',u'ص',
         u'ط',u'ع',u'ل',u'م',u'ن',u'ه',u'و',
         u'ى',u'ف',u'ق']

ar_to_en_letters={
    u'أ':'A',
    u'ب':'B',
    u'ج':'G',
    u'د':'D',
    u'ر':'R',
    u'س':'S',
    u'ص':'C',
    u'ط':'T',
    u'ع':'E',
    u'ل':'L',
    u'م':'M',
    u'ن':'N',
    u'ه':'H',
    u'و':'W',
    u'ى':'Y',
    u'ف':'F',
    u'ق':'K'
}
numbers=[u'١',u'٢',u'٣',u'٤',u'٥',u'٦',u'٧',u'٨',u'٩']
ar_to_en_numbers={
    u'١':'1',
    u'٢':'2',
    u'٣':'3',
    u'٤':'4',
    u'٥':'5',
    u'٦':'6',
    u'٧':'7',
    u'٨':'8',
    u'٩':'9'
}
ar_sub_letters=np.random.choice(letters,3)
print(ar_sub_letters)
ar_sub_numbers=np.random.choice(numbers,3)
print(ar_sub_letters)
img_path='templates/bus.png'
font_path='fonts/Almarai/Almarai-Bold.ttf'

img=Image.open(img_path)
font = ImageFont.truetype(font_path, 64)
draw = ImageDraw.Draw(img)
print(img.size)
numbers_orig=(int(img.size[0]*0.25),190)
letters_orig=(int(img.size[0]*0.75),190)
print(numbers_orig,letters_orig)
str_l=''
str_n=''
for l in ar_sub_letters:
    str_l+=l+' '
for n in ar_sub_numbers:
    str_n+=n+' '
img=put_text_to_img(img,str_l,font,letters_orig)
img=put_text_to_img(img,str_n,font,numbers_orig)
img.show()
