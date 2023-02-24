import cv2
from noises import noises, salt_papper, add_periodic
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('cameraman.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('original image',img)
Gframe=np.double(img)
Gframe = Gframe - Gframe.min()
Gframe = Gframe / Gframe.max()
[M,N]=img.shape
#R=0.3*noises('uniform', M,N,0,1)
#R=0.1*noises('gaussian', M,N,0,1)
#R=0.3*noises('lognormal', M,N,1,0.25)
#R=0.3*noises('rayleigh', M,N,0,1)
#R=0.2*noises('exponential', M,N,1,1)
#R=0.1*noises('erlang', M,N,2,5)
#R=R+Gframe
#R=salt_papper(img,0.05)










periodic = add_periodic(img).astype(int)
plt.figure(figsize=(6,6))
plt.imshow(periodic,cmap="gray")
plt.title("Periodic Noise")
plt.show()
from scipy import fftpack
import numpy.fft as fp
w = 10
h = 10

im = periodic
F1 = fftpack.fft2((im).astype(float))
F2 = fftpack.fftshift(F1)
for i in range(60, w, 135):
    for j in range(100, h, 200):
        if not (i == 330 and j == 500):
            F2[i-10:i+10, j-10:j+10] = 0
    for i in range(0, w, 135):
        for j in range(200, h, 200):
            if not (i == 330 and j == 500):
                F2[max(0,i-15):min(w,i+15), max(0,j-15):min(h,j+15)] = 0

plt.figure(figsize=(6,6))
plt.title("Spectrum")
plt.imshow( (20*np.log10( 0.1 + F2)).astype(int), cmap=plt.cm.gray)
plt.show()
F1[88,:]=0
F1[171,:]=0
F1[:,156]=0
F1[:,102]=0
F2 = fftpack.fftshift(F1)
im1 = fp.ifft2(fftpack.ifftshift(F2)).real
plt.figure(figsize=(6,6))
plt.title("Recovered Image")
plt.imshow(im1, cmap='gray')
plt.show()













# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)

# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()
