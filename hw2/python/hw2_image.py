import math

import cv2
import numpy as np
a="img.png"
image = cv2.imread(a)
#cv2.imshow("original image window",image)
b=image[:,:,0]
g=image[:,:,1]
r=image[:,:,2]
#Horizontal Reflection-------------------------------------------------------------------------------------------------
ref1=r[::-1,:]
ref2=g[::-1,:]
ref3=b[::-1,:]

#Vertical Reflection-------------------------------------------------------------------------------------------------
ref1=r[:,::-1]
ref2=g[:,::-1]
ref3=b[:,::-1]
#Resize--------------------------------------------------------------------------------------------------------------
res=image[0:-1:4,0:-1:2]
#cv2.imshow("image window",res)
#Cropping------------------------------------------------------------------------------------------------------------
new= image[0:800, 0:200,:]
#cv2.imshow("image window",new)
#Shifting------------------------------------------------------------------------------------------------------------
[a,s,c]=image.shape
B1=np.zeros([a,s])
B2=np.zeros([a,s])
B3=np.zeros([a,s])
A=[45,47,89,56,41,21]
for  i in range(40,a):

    for  j in range(40,s):
        B1[i, j] = b[i-40+1,j-40+1]
        B2[i, j] = g[i - 40 + 1, j - 40 + 1]
        B3[i, j] = r[i - 40 + 1, j - 40 + 1]

image[:,:,0]=B1[:,:]
image[:,:,1]=B2[:,:]
image[:,:,2]=B3[:,:]

#cv2.imshow("image window",image)

#RGB to YIQ------------------------------------------------------------------------------------------------------------

img= cv2.imread("img.png")
YIQ=np.uint8(np.zeros(img.shape))
[a,s,c]=img.shape
for i in range(0,a):
  for j in range(0,s):
    YIQ[i,j,2]=0.299*img[i,j,2]+0.5870*img[i,j,1]+0.1140*img[i,j,0]
    YIQ[i,j,1]=0.596*img[i,j,2]-0.274*img[i,j,1]-0.322*img[i,j,0]
    YIQ[i,j,0]=0.211*img[i,j,2]-0.523*img[i,j,1]+0.312*img[i,j,0]
#YIQ to RGB------------------------------------------------------------------------------------------------------------
RGB=np.uint8(np.zeros(YIQ.shape))
[a,s,c]=YIQ.shape
for i in range(0,a):
  for j in range(0,s):
    RGB[i,j,2]=YIQ[i,j,2]+0.956*YIQ[i,j,1]+0.621*YIQ[i,j,0]
    RGB[i,j,1]=YIQ[i,j,2]-0.272*YIQ[i,j,1]-0.647*YIQ[i,j,0]
    RGB[i,j,0]=YIQ[i,j,2]-1.106*YIQ[i,j,1]+1.703*YIQ[i,j,0]

#resize bigger------------------------------------------------------------------------------------------------------------
def interpolate_pixel(image,points,axis=1):
    p1,p2,p3=points
    pixel1,pixel2=image[p1[0],p1[1]],image[p2[0],p2[1]]
    d1,d2=p3[axis]-p1[axis],p2[axis]-p3[axis]
    pixel12=pixel1*d2+pixel2*d1
    return pixel12


def interpolate(image,new_w,new_h):
    h,w=image.shape[:2]
    rescaled_image=np.zeros((new_h,new_w,3))
    mapped_h=np.arange(new_h)*(h/new_h)
    mapped_w = np.arange(new_w) * (w / new_w)
    mapped_h[mapped_h>h-1]=h-1
    mapped_w[mapped_w > w - 1] = w - 1

    for i in range(mapped_h.size):
        for j in range(mapped_w.size):
            mi,mj=mapped_h[i],mapped_w[j]
            if mi==int(mi) and mj==int(mj):
                rescaled_image[i,j]=image[int(mi),int(mj)]
            elif mi==int(mi):
                i1,j1=int(mi),int(mj)
                i2, j2 = int(mi), min(int(mj)+1,w-1)
                rescaled_image[i,j]=interpolate_pixel(image,[[i1,j1],[i2,j2],[i1,mj]],axis=1)
            elif mj==int(mj):
                i1, j1 = int(mi), int(mj)
                i2, j2 = min(int(mi)+1,h-1), int(mj)
                rescaled_image[i,j]=interpolate_pixel(image,[[i1,j1],[i2,j2],[mi,j1]],axis=0)
            else:
                i1, j1 = int(mi), int(mj)
                i2, j2 = int(mi), min(int(mj) + 1, w - 1)
                i3, j3 = min(int(mi) + 1, h - 1), int(mj)
                i4, j4 = min(int(mi) + 1, h - 1), min(int(mj) + 1, w - 1)
                pixelij1=interpolate_pixel(image,[[i1,j1],[i2,j2],[i1,mj]],axis=1)
                pixelij2 = interpolate_pixel(image, [[i3, j3], [i4, j4], [i3, mj]], axis=1)
                dy1,dy2=mi-i1,i3-mi
                rescaled_image[i,j]=pixelij1*dy2+pixelij2*dy1

    return rescaled_image

img=cv2.imread("img.png")
img=interpolate(img,800,600)
img=np.uint8(img)
#cv2.imshow("image window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()