import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("imagess/hw3_4_2.tif")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("image window",img)

[a,b]=img.shape
#a=np.double(img)
def hist(image):
    h=np.zeros(shape=(256,1))

    [x,y]=image.shape
    for i in range(x):
        for j in range(y):
            k=image[i,j]
            h[k,0]=h[k,0]+1
    return h


histg=hist(img)

plt.plot(histg)
plt.show()

pdf = (1 / (a * b)) * histg

cdf = np.zeros(shape=(256,1))
cdf[1]= pdf[1]
for i in range(2,256):

    cdf[i] = cdf[i-1] + pdf[i]

cdf =np.round(255*cdf)

ep = np.zeros(shape=(a,b))
for i in range(1,a):
    for j in range (1,b):                                  #loop tracing thes columns of image
        t=(img[i,j]+1)                          #pixel values in image
        ep[i,j]=cdf[t]                           #Making the ouput image using cdf as the transformation function
img=np.uint8(ep)

cv2.imshow("image window2",img)


cv2.waitKey(0)
cv2.destroyAllWindows()