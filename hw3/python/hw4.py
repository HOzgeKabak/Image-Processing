import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("imagess/hw4.jpg")

def hist(image):
    h=np.zeros(shape=(256,1))
    h1 = np.zeros(shape=(256, 1))
    h2 = np.zeros(shape=(256, 1))
    [x,y,z]=image.shape
    for i in range(x):
        for j in range(y):
            k=image[i,j,0]
            h[k,0]=h[k,0]+1
            k1= image[i, j, 1]
            h1[k1, 0] = h1[k1, 0] + 1
            k2 = image[i, j, 2]
            h2[k2, 0] = h2[k2, 0] + 1
    return h,h1,h2

histg,histg2,histg3=hist(img)
plt.plot(histg3)
plt.plot(histg2)
plt.plot(histg)
plt.show()

x1=histg.reshape(1,256)
y1=np.zeros((1,256))
x2=histg2.reshape(1,256)
y2=np.zeros((1,256))
x3=histg3.reshape(1,256)
y3=np.zeros((1,256))
for i in range(256):
    if x1[0,i]==0:
        y1[0,i]=0
    else:
        y1[0, i] = i

    if x2[0,i]==0:
        y2[0,i]=0
    else:
        y2[0, i] = i

    if x3[0,i]==0:
        y3[0,i]=0
    else:
        y3[0, i] = i

min1=np.min(y1[np.nonzero(y1)])
max1=np.max(y1[np.nonzero(y1)])
min2=np.min(y2[np.nonzero(y2)])
max2=np.max(y2[np.nonzero(y2)])
min3=np.min(y3[np.nonzero(y3)])
max3=np.max(y3[np.nonzero(y3)])
strech1=np.round((255/(max1-min1)*(y1-min1)))
strech1[strech1<0]=0
strech1[strech1>255]=255
strech2=np.round((255/(max2-min2)*(y2-min2)))
strech2[strech2<0]=0
strech2[strech2>255]=255
strech3=np.round((255/(max3-min3)*(y3-min3)))
strech3[strech3<0]=0
strech3[strech3>255]=255
[x,y,z]=img.shape
for i in range(x):
    for j in range(y):
        k = img[i, j, 0]
        k1 = img[i, j, 1]
        k2 = img[i, j, 2]
        img[i,j,0]=strech1[0,k]
        img[i, j, 1] = strech2[0, k1]
        img[i, j, 2] = strech3[0, k2]


histg1,histg22,histg33=hist(img)
plt.plot(histg33)
plt.plot(histg22)
plt.plot(histg1)
plt.show()
cv2.imshow("image window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()