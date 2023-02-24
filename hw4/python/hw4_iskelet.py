import math

import cv2
import numpy as np

img=cv2.imread("imagess/HW4_2.tif")
cv2.imshow("original window",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
[a,b]=img.shape
filter=[[-0.125, -0.125, -0.125],[-0.125 ,1, -0.125],[-0.125, -0.125, -0.125]]
filter=np.double(filter)
array=np.zeros(shape=(a+2,b+2))
array2=np.zeros(shape=(a+2,b+2))
array3=np.zeros(shape=(a+2,b+2))
for i in range(a):
    for j in range(b):
        x=img[i,j]
        array[i+1,j+1]=x
        array2[i + 1, j + 1] = x
        array3[i + 1, j + 1] = x
array=np.double(array)
array2=np.double(array2)
output1=np.zeros([a,b])
output2=np.zeros([a,b])
for i in range(a-2):
     for j in range(b-2):
         temp1=np.multiply(array[i:i+3,j:j+3],filter)
         output1[i,j]=temp1.sum()

image_b=np.uint8(output1)
cv2.imshow("image b window",image_b)

image_c=image_b+img
cv2.imshow("image c window",image_c)

for i in range(1,a-2):
    for j in range(1,b-2):
       Gx=((2*array2[i+2,j+1]+array2[i+2,j]+array2[i+2,j+2])-(2*array2[i,j+1]+array2[i,j]+array2[i,j+2]))
       Gy=((2*array2[i+1,j+2]+array2[i,j+2]+array2[i+2,j+2])-(2*array2[i+1,j]+array2[i,j]+array2[i+2,j]));
       output2[i,j]=math.sqrt(pow(Gx,2)+pow(Gy,2))

image_d=np.uint8(output2)
cv2.imshow("image d window",image_d)
#mean filtering
filter=np.ones([5,5])
filter=(filter)/25
filter=np.double(filter)
array3=np.double(array3)
output3=np.zeros([a,b])
for i in range(a-4):
     for j in range(b-4):
         temp1=np.multiply(array3[i:i+5,j:j+5],filter)
         output3[i,j]=temp1.sum()



image_e=np.uint8(output3)
cv2.imshow("image e window",image_e)
image_f=np.multiply(np.double(image_e),np.double(image_c))
image_f=image_f/255
image_f=np.uint8(image_f)
cv2.imshow("image f window",image_f)
image_g=image_f+img
cv2.imshow("image g window",image_g)
image_h=np.double(image_g)**1.0
cv2.imshow("image h window",np.uint8(image_h))
cv2.waitKey(0)
cv2.destroyAllWindows()