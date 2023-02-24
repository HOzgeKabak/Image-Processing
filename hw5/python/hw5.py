import math

import numpy as np
import cv2
from matplotlib import pyplot as plt
import freq_filters

img = cv2.imread('imagess/HW5_2.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=cv2.imread("imagess/HW5_1.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
A=np.zeros([474,630])
for i in range(1,474):
    for j in range(1,630):
        ycap = math.sqrt((i-250)^2 + (j-300)^2)
        if ycap < 50 :
            A[i,j] = 1
        else :
            A[i,j] = 0

M, N = img.shape
P = 2*M
Q = 2*N

# Take the fourier transform of the image, with padding to shape P X Q
F = np.fft.fft2(img, s=(P,Q))

# Shift the low frequencies to the center.
F = np.fft.fftshift(F)
G = np.multiply(F,A)

# Shift frequencies back
G = np.fft.ifftshift(G)

# Inverse fourier transform to get output image in spatial domain
G = np.fft.ifft2(G)

# Get real values
G = np.abs(G)

# Extract M x N image from top left quadrant
G = G[0:M, 0:N]
output=G









output5,H2,spectrum2=freq_filters.filter_image_freq(img2, fclass='highpass', ftype='butterworth', d0=50, w=0, n=4, u_k=0, v_k=0)
[a,b]=output5.shape
for i in range(a):
    for j in range(b):
        if output5[i,j]<=20:
            output5[i,j]=255
plt.subplot(221)
plt.imshow(img2, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222)
plt.imshow(output5, cmap = 'gray')
plt.title('Output Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223)
plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224)
plt.imshow(output, cmap = 'gray')
plt.title('Output Image'), plt.xticks([]), plt.yticks([])
plt.show()
