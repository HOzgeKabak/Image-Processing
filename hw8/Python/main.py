import cv2

#Part-1-----------------------------------------------------------------------------------------------------------------
"""img=cv2.imread("HW8_1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('original image',img)
r=10 #diameter of the disk
kernel= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r,r))
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('after opening image',opening)
closing=cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow('after closing image',closing)
#Part-2-----------------------------------------------------------------------------------------------------------------
img=cv2.imread("HW8_2.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('original image',img)
kernel= cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('after dilation image',dilation)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('after erosion image',erosion)
# subtract the images
gradien = cv2.subtract(dilation, erosion)
cv2.imshow(' gradien image',gradien)
#Part-3-----------------------------------------------------------------------------------------------------------------
img=cv2.imread("HW8_3.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('original image',img)
# Otsu's thresholding
ret,th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('after Otsu image',th)
r=80 #diameter of the disk
kernel= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r,r))
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('after opening image',opening)
tophat = cv2.subtract(img, opening)
cv2.imshow('after tophat image',tophat)
ret2,th2 = cv2.threshold(tophat,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('after tophat OTSU image',th2)"""
#Part-4-----------------------------------------------------------------------------------------------------------------
img=cv2.imread("HW8_4.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('original image',img)
r=60 #diameter of the disk
kernel= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r,r))
closing=cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('after closing image',closing)
r2=120 #diameter of the disk
kernel2=kernel= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r2,r2))
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
cv2.imshow('after opening image',opening)
kernel3=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
gradient = cv2.morphologyEx(opening, cv2.MORPH_GRADIENT, kernel3)
cv2.imshow(' gradien image',gradient)
final=cv2.add(gradient,img)
cv2.imshow(' final image',final)
# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)

# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()