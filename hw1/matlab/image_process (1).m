% Halime Özge KABAK 180403001
% Image Processing HW1
%----------------------------------------------------------------------
img=imread('flora.jpg'); %we are reading image in here
figure
imshow(img) %showig the image
% matrix=img; %matrix version of the image
% gray=rgb2gray(img); %we are transforming image rgb to gray image
% figure
% imshow(gray)
[s1,s2,s3]=size(img); %we are finding the size of the image if it is (k x m x n) then it is a rgb image but if it is (k x m) then its gray picture 
% [a,b,c]=size(gray); %with this way we can store the matrix sizes in a values a,b and c
% k=size(img,1); %we can find the a value like this
% k2=size(img,2); %we can find the b value like this 
% k3=size(img,3);  %we can find the c value like this
% figure
% imhist(gray) %this function shows histogram of the images
% g=imadjust(gray,[0.5,0.9],[0.3,0.4]); %we are changing intensity of the image
% figure
% imshow(g)
% n=imadjust(gray,[0,1],[1,0]); %it transforms the image to negative
% figure
% imshow(n)
% bw=im2bw(img); %#ok<IM2BW> %it makes the image black white and matrix values turns to 0 and 1
% figure
% imshow(bw)
% d=im2double(gray); %with this command image doesnt change but the matrix values become double
% change_size=imresize(img,[400,400]); % changes the image size to 400x400
% imshow(change_size)
% imwrite(change_size,'saved image.jpg','Quality',100); %saves the image
%we are filtering each channel seperately
r=im2double(img(:,:,1));
g=im2double(img(:,:,2));
b=im2double(img(:,:,3));
%----------------------------------
%first way
% f=ones(2,2)/4;
% img1=filter2(f,r);
% img2=filter2(f,g);
% img3=filter2(f,b);
% im=cat(3,img1,img2,img3);
%----------------------------------
%second way
a=80;
a2=60;
filter=ones(a,a2);
filter=double(filter/sum(filter(:)));
finak=zeros((size(r)));
final2=zeros((size(r)));
final3=zeros((size(r)));
endpoint=size(r,1);
endpoint2=size(r,2);
extra=rem(s1,a);
extra2=rem(s2,a2);
for i=1:a:endpoint-extra
    for j=1:a2:endpoint2-extra2
       
        filtering1=r(i:i+(a-1),j:j+(a2-1)).*filter;
        for z=1:a
            for z2=1:a2
              finak(i+z-1,j+z2-1)=sum(filtering1(:));
            end
        end
        filtering2=g(i:i+(a-1),j:j+(a2-1)).*filter;
        for z=1:a
            for z2=1:a2
               final2(i+z-1,j+z2-1)=sum(filtering2(:));
            end
        end
        filtering3=b(i:i+(a-1),j:j+(a2-1)).*filter;
        for z=1:a
            for z2=1:a2
              final3(i+z-1,j+z2-1)=sum(filtering3(:));
            end
        end
    end
end
a3=extra;
a4=a2;
filter2=ones(a3,a4);
filter2=double(filter2/sum(filter2(:)));
if extra~=0
   if extra~=1
       for i=endpoint-extra:a3:endpoint-a3+1
        for j=1:a4:endpoint2-a4+1
            filtering1=r(i:i+(a3-1),j:j+(a4-1)).*filter2;
        for z=1:a3
            for z2=1:a4
              finak(i+z-1,j+z2-1)=sum(filtering1(:));
            end
        end
        filtering2=g(i:i+(a3-1),j:j+(a4-1)).*filter2;
        for z=1:a3
            for z2=1:a4
               final2(i+z-1,j+z2-1)=sum(filtering2(:));
            end
        end
        filtering3=b(i:i+(a3-1),j:j+(a4-1)).*filter2;
        for z=1:a3
            for z2=1:a4
              final3(i+z-1,j+z2-1)=sum(filtering3(:));
            end
        end
        end
       
            
       end
   end
end
 


a5=a;
a6=extra2;
filter3=ones(a5,a6);
filter3=double(filter3/sum(filter3(:)));

if extra2~=0
   if extra2~=1
       for i=1:a5:endpoint-a5+1
        for j=endpoint2-extra2:a6:endpoint2-a6+1
            filtering1=r(i:i+(a5-1),j:j+(a6-1)).*filter3;
        for z=1:a5
            for z2=1:a6
              finak(i+z-1,j+z2-1)=sum(filtering1(:));
            end
        end
        filtering2=g(i:i+(a5-1),j:j+(a6-1)).*filter3;
        for z=1:a5
            for z2=1:a6
               final2(i+z-1,j+z2-1)=sum(filtering2(:));
            end
        end
        filtering3=b(i:i+(a5-1),j:j+(a6-1)).*filter3;
        for z=1:a5
            for z2=1:a6
              final3(i+z-1,j+z2-1)=sum(filtering3(:));
            end
        end
        end
       
            
       end
   end
end
 if extra~=0 && extra2~=0
     if extra~=1 && extra2~=1
        for i=endpoint-extra+1:extra:endpoint
            for j=endpoint2-extra2+1:extra2:endpoint2
                a=extra;
                a2=extra2;
                filter=ones(a,a2);
                filter=double(filter/sum(filter(:)));

                filtering1=r(i:i+(a-1),j:j+(a2-1)).*filter;
        for z=1:a
            for z2=1:a2
              finak(i+z-1,j+z2-1)=sum(filtering1(:));
            end
        end
        filtering2=g(i:i+(a-1),j:j+(a2-1)).*filter;
        for z=1:a
            for z2=1:a2
               final2(i+z-1,j+z2-1)=sum(filtering2(:));
            end
        end
        filtering3=b(i:i+(a-1),j:j+(a2-1)).*filter;
        for z=1:a
            for z2=1:a2
              final3(i+z-1,j+z2-1)=sum(filtering3(:));
            end
        end
                
            end
        end
     end
 end

 im=cat(3,finak,final2,final3);
 figure
 imshow(im)

