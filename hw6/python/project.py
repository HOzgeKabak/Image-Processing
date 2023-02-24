# Python program to illustrate
# template matching
import numpy as np
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from skimage import transform
from skimage.color import rgb2gray
from skimage.feature import match_template
from skimage.feature import peak_local_max
import cv2
import numpy as np
from skimage.feature import match_template
# Read the main image
img_rgb = imread('cobb2.jpg')
#img_rgb = cv2.resize(img_rgb,(256,256))
# Convert it to grayscale
img_gray = rgb2gray(img_rgb)

# Read the template
template = imread('cropped_cobble/6.jpg')
#template = rgb2gray(template)
#template = cv2.resize(template,(256,256))
# Store width and height of template in w and h
img = match_template(img_gray, template)
print(img)
plt.figure(num=None, figsize=(8, 6), dpi=80)
imshow(img)
plt.show()
x, y = np.unravel_index(np.argmax(img), img.shape)
template_width, template_height = template.shape
rect = plt.Rectangle((y, x), template_height, template_width,
                     color='r', fc='none')
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.gca().add_patch(rect)
imshow(img_gray)
plt.show()
