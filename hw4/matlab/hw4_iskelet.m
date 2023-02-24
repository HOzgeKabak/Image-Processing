img=imread('HW4_2.tif'); %we are reading image in here
subplot(2,4,1)
imshow(img)
[a,b,c]=size(img);
f=3;
filter=[-1 -1 -1;-1 8 -1;-1 -1 -1];
%filter=(filter)/sum(filter(:));
%filter=double(filter);
array=padarray(img,[1 1]);
array=double(array);
output1=zeros(a,b);
output2=zeros(a,b);
output3=zeros(a,b);
for i=1:size(array,1)-2
    for j=1:size(array,2)-2
    temp1=array(i:i+f-1,j:j+f-1).*filter;
    output1(i,j)=sum(temp1(:));
    end
end
subplot(2,4,2)
imshow(uint8(output1))
image_c=img+uint8(output1);

subplot(2,4,3)
imshow(image_c)

for i=1:size(array,1)-2
    for j=1:size(array,2)-2
       Gx=((2*array(i+2,j+1)+array(i+2,j)+array(i+2,j+2))-(2*array(i,j+1)+array(i,j)+array(i,j+2)));
       Gy=((2*array(i+1,j+2)+array(i,j+2)+array(i+2,j+2))-(2*array(i+1,j)+array(i,j)+array(i+2,j)));
       output2(i,j)=sqrt(Gx.^2+Gy.^2);
    end
end
image_d=uint8(output2);
subplot(2,4,4)
imshow(image_d)
image_e=mean_filter(image_d,5);
image_e=uint8(image_e);
subplot(2,4,5)
imshow(image_e)
image_f=medfilt2(double(image_e) .* double(image_c))/255;
subplot(2,4,6)
imshow(uint8(image_f))
image_g=uint8(output1)+img;
subplot(2,4,7)
imshow(image_g)
gamma=exp(0.1);
r=(double(image_g).^gamma);
subplot(2,4,8)
imshow(uint8(r))