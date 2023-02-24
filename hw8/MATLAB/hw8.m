%Halime Özge KABAK
%180403001
%Image Processing HW8
%--------------------------------------------------------------------------
close all;
%Part 1--------------------------------------------------------------------
% original = imread('HW8_1.tif');
% imshow(original);
% r=5;
% se1 = strel('disk',r);
% afterOpening = imopen(original,se1);
% figure
% imshow(afterOpening);
% closeBW = imclose(afterOpening,se1);
% figure, imshow(closeBW)
%Part 2--------------------------------------------------------------------
% original = imread('HW8_2.tif');
% imshow(original);
% se = strel('square',3);
% BW2 = imdilate(original,se);
% figure,imshow(BW2), title('Dilated')
% erodedBW = imerode(original,se);
% imshow(erodedBW), title('Eroded')
% gradien=imsubtract(BW2,erodedBW);
% imshow(gradien)
%Part 3--------------------------------------------------------------------
% original = imread('HW8_3.tif');
% figure
% imshow(original);
% [counts,x] = imhist(original,32);
% T = otsuthresh(counts);
% BW = imbinarize(original,T);
% figure
% imshow(BW)
% se1 = strel('disk',40);
% afterOpening = imopen(original,se1);
% figure
% imshow(afterOpening);
% tophat=imsubtract(original,afterOpening);
% figure
% imshow(tophat);
% [counts2,x2] = imhist(tophat,32);
% T = otsuthresh(counts2);
% BW2 = imbinarize(tophat,T);
% figure
% imshow(BW2)
%Part 4--------------------------------------------------------------------
original = imread('HW8_4.jpg');
figure
imshow(original);
se1 = strel('disk',30);
closeBW = imclose(original,se1);
figure, imshow(closeBW)
se2 = strel('disk',60);
I = imopen(closeBW,se2);
figure
imshow(I);
se = strel(ones(3,3));
gradient = imdilate(I, se) - imerode(I, se);
imshow(gradient)
final=imadd(original,gradient);
imshow(final)
