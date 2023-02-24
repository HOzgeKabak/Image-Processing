img=imread('HW4_1.tif'); %we are reading image in here
figure
imshow(img)
% [a,b,c]=size(img);
% f=8;
% filter=ones(f,f);
% filter=(filter)/sum(filter(:));
% filter=double(filter);
% array=padarray(img,[6 6]);
% array=double(array);
% array1=array(:,:,1);
% array2=array(:,:,2);
% array3=array(:,:,3);
% output1=zeros(a,b);
% output2=zeros(a,b);
% output3=zeros(a,b);
% for i=1:size(array,1)-f-1
%     for j=1:size(array,2)-f-1
%     temp1=array1(i:i+f-1,j:j+f-1).*filter;
%     output1(i,j)=sum(temp1(:));
%     temp2=array2(i:i+f-1,j:j+f-1).*filter;
%     output2(i,j)=sum(temp2(:));
%     temp3=array3(i:i+f-1,j:j+f-1).*filter;
%     output3(i,j)=sum(temp3(:));
%     end
% end
% 
%  im=cat(3,output1,output2,output3);
%  figure
%  imshow(uint8(im))
%  disp(im)

[a,b]=size(img);
%Mean Filter
% f=3;
% filter=ones(f,f);
% filter=(filter)/sum(filter(:));
% filter=double(filter);
% array=padarray(img,[1 1]);
% array=double(array);
% output1=zeros(a,b);
% for i=1:size(array,1)-f-1
%     for j=1:size(array,2)-f-1
%     temp1=array1(i:i+f-1,j:j+f-1).*filter;
%     output1(i,j)=sum(temp1(:));
%     end
% end
%   figure
% imshow(uint8(output1))
%------------------------------------------------------------------------
%median filter
mf=ones(3,3);
output=zeros(size(img)-2);
for i=1:size(img,1)-2
    for j=1:size(img,2)-2
    temp1=double(img(i:i+2,j:j+2)).*mf;
    output(i,j)=median(temp1(:));
    end
end

imshow(uint8(output))
%------------------------------------------------------------------------
%max filter
A=img;
B=zeros(size(A));
modifyA=padarray(A,[1 1]);
x=[1:3]';
y=[1:3]'; 
for i= 1:size(modifyA,1)-2
    for j=1:size(modifyA,2)-2
       window=reshape(modifyA(i+x-1,j+y-1),[],1);
       B(i,j)=max(window);
    end
end
B=uint8(B);
figure
imshow(B)
%------------------------------------------------------------------------
%min filter
A=img;
B=zeros(size(A));
modifyA=padarray(A,[1 1]);
x=[1:3]';
y=[1:3]'; 
for i= 1:size(modifyA,1)-2
    for j=1:size(modifyA,2)-2
       window=reshape(modifyA(i+x-1,j+y-1),[],1);
       B(i,j)=min(window);
    end
end
B=uint8(B);
figure
imshow(B)
