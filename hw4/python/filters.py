import cv2
import numpy as np
import statistics
img=cv2.imread("imagess/HW4_1.tif")
cv2.imshow("original window",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
[a,b]=img.shape
array=np.zeros(shape=(a+2,b+2))
array2=np.zeros(shape=(a+2,b+2))
array3=np.zeros(shape=(a+2,b+2))
array4=np.zeros(shape=(a+2,b+2))
for i in range(a):
    for j in range(b):
        x=img[i,j]
        array[i+1,j+1]=x
        array2[i + 1, j + 1] = x
        array3[i + 1, j + 1] = x
        array4[i + 1, j + 1] = x


#mean filtering
filter=np.ones([3,3])
filter=(filter)/9
filter=np.double(filter)
array=np.double(array)
output1=np.zeros([a,b])
for i in range(a-2):
     for j in range(b-2):
         temp1=np.multiply(array[i:i+3,j:j+3],filter)
         output1[i,j]=temp1.sum()



image=np.uint8(output1)
cv2.imshow("image window",image)

#median filtering
filter2=np.ones([3,3])
filter2=np.double(filter2)
array2=np.double(array2)
output2=np.zeros([a,b])
output3=np.zeros([a,b])
output4=np.zeros([a,b])
for i in range(a-2):
     for j in range(b-2):
         temp1=np.multiply(array2[i:i+3,j:j+3],filter2)
         output2[i,j]=np.median(temp1)


image=np.uint8(output2)
cv2.imshow("image 2 window",image)



for i in range(a-2):
     for j in range(b-2):
         temp1=array3[i:i+3,j:j+3]
         output3[i,j]=np.max(temp1)

image=np.uint8(output3)
cv2.imshow("image 3 window",image)

for i in range(a-2):
     for j in range(b-2):
         temp1=array4[i:i+3,j:j+3]
         output4[i,j]=np.min(temp1)

image=np.uint8(output4)
cv2.imshow("image 4 window",image)


cv2.waitKey(0)
cv2.destroyAllWindows()