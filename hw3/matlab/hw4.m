%Halime Özge KABAK
%180403001
%HW2- Image Processing


img=imread('hw4.tif'); %we are reading image in here
figure
imshow(img) %showig the image
r=double(img(:,:,1));
g=double(img(:,:,2));
b=double(img(:,:,3));
min1=double(min(r(:)));
min2=double(min(g(:)));
min3=double(min(b(:)));
max1=double(max(r(:)));
max2=double(max(g(:)));
max3=double(max(b(:)));
o=r;
o2=g;
o3=b;
[m,n]=size(r);
minp=min(min(r));
maxp=max(max(r));
minp2=min(min(g));
maxp2=max(max(g));
minp3=min(min(b));
maxp3=max(max(b));
for i=1:m
    for j=1:n
        o(i,j)=((250/(maxp-minp))*(r(i,j)-minp));
        o2(i,j)=((250/(maxp2-minp2))*(g(i,j)-minp2));
        o3(i,j)=((250/(maxp3-minp3))*(b(i,j)-minp3));
    end
end
img=cat(3,o,o2,o3);
figure
imshow(uint8(img))
for i=1:m
    for j=1:n
      Cp=double(r(i,j));
      Cp2=double(g(i,j));
      Cp3=double(b(i,j));
      o(i,j)=((Cp-min1)*255/(max1-min1));
      o2(i,j)=((Cp2-min2)*255/(max2-min2));
      o3(i,j)=((Cp3-min3)*255/(max3-min3));
    end
end
img=cat(3,o,o2,o3);
figure
imshow(uint8(img))