import cv2
import numpy as np
a="img.png"
image = cv2.imread(a)
cv2.imshow("original image window",image)
black_value=50
white_value=180
[a,s,c]=image.shape
formula=255/(white_value-black_value)
def f(x):
    return ((x-white_value)*formula)+255

for i in range(a):
    for j in range(s):

        if black_value < image[i, j, 1] and white_value > image[i, j, 1]:
            new = np.double(image[i, j, 1])
            image[i, j, 1] = np.uint8(f(new))

        if black_value < image[i, j, 0] and white_value > image[i, j, 0]:
            new = np.double(image[i, j, 0])
            image[i, j, 0] = np.uint8(f(new))

        if black_value < image[i, j, 2] and white_value > image[i, j, 2]:
            new = np.double(image[i, j, 2])
            image[i, j, 2] = np.uint8(f(new))



        if image[i,j,0]<=black_value:
            image[i,j,0]=0
        if image[i,j,0]>=white_value:
            image[i,j,0]=255

        if image[i,j,1]<=black_value:
            image[i,j,1]=0
        if image[i,j,1]>=white_value:
            image[i,j,1]=255

        if image[i,j,2]<=black_value:
            image[i,j,2]=0
        if image[i,j,2]>=white_value:
            image[i,j,2]=255





cv2.imshow("image window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()