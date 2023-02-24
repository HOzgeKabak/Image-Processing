# Python program to illustrate
# template matching
import xlsxwriter as xlsxwriter
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import match_template
# Read the main image
import cv2


max_array=[]
img_rgb = imread('cropped_tree/5.jpg')
img_rgb = cv2.resize(img_rgb,(256,256))
# Convert it to grayscale
img_gray = (img_rgb)



template1 =imread("cropped_cobble/35.jpg")
template2 =imread("cropped_cobble/120.jpg")
template3 =imread("cropped_cobble/123.jpg")
template4 =imread("cropped_cobble/120.jpg")
template5 =imread("cropped_cobble/125.jpg")
template6 =imread("cropped_cobble/129.jpg")
template7 =imread("cropped_cobble/130.jpg")
template8 =imread("cropped_cobble/189.jpg")
template9 =imread("cropped_tree/59.jpg")
template10 =imread("cropped_tree/81.jpg")
template11 =imread("cropped_tree/92.jpg")
template12 =imread("cropped_tree/96.jpg")
template13 =imread("cropped_tree/7.jpg")
template14 =imread("cropped_tree/39.jpg")
template15 =imread("cropped_tree/72.jpg")
template16 =imread("cropped_tree/75.jpg")



img1 = match_template(img_gray, template1)
img2 = match_template(img_gray, template2)
img3 = match_template(img_gray, template3)
img4 = match_template(img_gray, template4)
img5 = match_template(img_gray, template5)
img6 = match_template(img_gray, template6)
img7 = match_template(img_gray, template7)
img8 = match_template(img_gray, template8)
img9 = match_template(img_gray, template9)
img10 = match_template(img_gray, template10)
img11 = match_template(img_gray, template11)
img12 = match_template(img_gray, template12)
img13= match_template(img_gray, template13)
img14 = match_template(img_gray, template14)
img15 = match_template(img_gray, template15)
img16 = match_template(img_gray, template16)

max1=(img1.max())
max2=(img2.max())
max3=(img3.max())
max4=(img4.max())
max5=(img5.max())
max6=(img6.max())
max7=(img7.max())
max8=(img8.max())
max9=(img9.max())
max10=(img10.max())
max11=(img11.max())
max12=(img12.max())
max13=(img13.max())
max14=(img14.max())
max15=(img15.max())
max16=(img16.max())

liste=[]
liste.append(max1)
liste.append(max2)
liste.append(max3)
liste.append(max4)
liste.append(max5)
liste.append(max6)
liste.append(max7)
liste.append(max8)
liste.append(max9)
liste.append(max10)
liste.append(max11)
liste.append(max12)
liste.append(max13)
liste.append(max14)
liste.append(max15)
liste.append(max16)



sum1=max1+max2+max3+max4+max5+max6+max7+max8
mean1=sum1/8
sum2=max9+max10+max11+max12+max13+max14+max15+max16
mean2=sum2/8

print(mean1)
print(mean2)

for i in range(len(liste)):
    print(liste[i])


max_value=max(liste)
max_index = liste.index(max_value)

if max_index<8:
    print("Pattern is Cobblestone.")
else:
    print("Pattern is Tree.")



