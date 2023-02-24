# Python program to illustrate
# template matching
import xlsxwriter as xlsxwriter
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import match_template
# Read the main image
import cv2
import os
import glob
import openpyxl




img_dir = "cropped_tree" # Enter Directory of all images
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
for f1 in files:
    img = cv2.imread(f1)
    data.append(img)


max_array=[]
img_rgb = imread('cropped_tree/90.jpg')
img_rgb = cv2.resize(img_rgb,(256,256))
# Convert it to grayscale
img_gray = (img_rgb)



for i in range(len(data)):
   # print(data[3][0])


    # Read the template
    template =data[i][0]
    #template = rgb2gray(template)
            #template = cv2.resize(template,(256,256))
            # Store width and height of template in w and h
    img = match_template(img_gray, template)
    max_array.append((img.max()))

print(max(max_array))
max_value=max(max_array)
max_index = max_array.index(max_value)
print(max_index)
workbook = xlsxwriter.Workbook("Kitap1.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write_row(0, 2, max_array)
workbook.close()
plt.figure(num=None, figsize=(8, 6), dpi=80)
imshow(img)
plt.show()


x, y = np.unravel_index(np.argmax(img), img.shape)
template_width, template_height = template.shape
rect = plt.Rectangle((y, x), template_height, template_width,
                     color='r', fc='none')
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.gca().add_patch(rect)
imshow(img_rgb)
plt.show()
