%Halime Özge KABAK
%180403001
%HW2- Image Processing


img=imread('img.png'); %we are reading image in here
im=imread('peppers.jpg'); 
figure
imshow(img) %showig the image
r=im2double(img(:,:,1));
g=im2double(img(:,:,2));
b=im2double(img(:,:,3));
%Reflection-Horizontal---------------------------------------------------------------
ref1=r(end:-1:1,:);
ref2=g(end:-1:1,:);
ref3=b(end:-1:1,:);
im=cat(3,ref1,ref2,ref3);
%figure
%imshow(im)
%Reflection-Vertical---------------------------------------------------------------
ref1=r(:,end:-1:1);
ref2=g(:,end:-1:1);
ref3=b(:,end:-1:1);
im=cat(3,ref1,ref2,ref3);
%figure
%imshow(im)
%Resize ------------------------------------------------------------------------------
 res1=r(1:2:end,1:4:end);
 res2=g(1:2:end,1:4:end);
 res3=b(1:2:end,1:4:end);
 im=cat(3,res1,res2,res3);
 new=bilinearInterpolation(img,[200,200]);
 figure
 imshow(new)
%Shifting-----------------------------------------------------------------------------
[a,s,c]=size(img);
B1=zeros(a,s); 
B2=zeros(a,s); 
B3=zeros(a,s); 
for i=40:a
for j=40:s 
    B1(i,j)=r(i-40+1,j-40+1); 
    B2(i,j)=g(i-40+1,j-40+1); 
    B3(i,j)=b(i-40+1,j-40+1); 
end 
end 
 im=cat(3,B1,B2,B3);
 %figure
% imshow(im)
%Cropping----------------------------------------------------------------------------------
%img=img(row_start:row_end,col_start:col_end,:);
im=img(300:500,300:500,:);
%imshow(im)
%RGB to YIQ----------------------------------------------------------------
YIQ=uint8(zeros(size(img)));
for i=1:size(img,1)
  for j=1:size(img,2)
    YIQ(i,j,1)=0.2989*img(i,j,1)+0.5870*img(i,j,2)+0.1140*img(i,j,3);
    YIQ(i,j,2)=0.596*img(i,j,1)-0.274*img(i,j,2)-0.322*img(i,j,3);
    YIQ(i,j,3)=0.211*img(i,j,1)-0.523*img(i,j,2)+0.312*img(i,j,3);
  end
end
% figure,imshow(YIQ);
%YIQ to RGB----------------------------------------------------------------
RGB=uint8(zeros(size(YIQ)));
for i=1:size(YIQ,1)
    for j=1:size(YIQ,2)
      RGB(i,j,1)=YIQ(i,j,1)+0.956*YIQ(i,j,2)+0.621*YIQ(i,j,3);
      RGB(i,j,2)=YIQ(i,j,1)-0.272*YIQ(i,j,2)-0.647*YIQ(i,j,3);
      RGB(i,j,3)=YIQ(i,j,1)-1.106*YIQ(i,j,2)+1.703*YIQ(i,j,3);
    end
end
% figure,imshow(RGB);
%RGB to HSI----------------------------------------------------------------
img=double(img)/255;
r2=img(:,:,1);
g2=img(:,:,2);
b2=img(:,:,3);
numi=1/2*((r2-g2)+(r2-b2));
denom=((r2-g2).^2+((r2-b2).*(g2-b2))).^0.5;
H=acosd(numi./(denom+0.000001));

%If B>G then H= 360-Theta
H(b2>g2)=360-H(b2>g2);

%Normalize to the range [0 1]
H=H/360;

%Saturation
S=1- (3./(sum(img,3)+0.000001)).*min(img,[],3);


%Intensity
I=sum(img,3)./3;
HSI=zeros(size(img));
HSI(:,:,1)=H;
HSI(:,:,2)=S;
HSI(:,:,3)=I;

% figure,imshow(HSI);
%HSI to RGB----------------------------------------------------------------
 H=H*360;                                               
    


 %Preallocate the R,G and B components  
 R1=zeros(size(H));  
 G1=zeros(size(H));  
 B1=zeros(size(H));  
 RGB1=zeros([size(H),3]);  
    


 %RG Sector(0<=H<120)  
 %When H is in the above sector, the RGB components equations are  


    
 B1(H<120)=I(H<120).*(1-S(H<120));  
 R1(H<120)=I(H<120).*(1+((S(H<120).*cosd(H(H<120)))./cosd(60-H(H<120))));  
 G1(H<120)=3.*I(H<120)-(R1(H<120)+B1(H<120));  


    
 %GB Sector(120<=H<240)  
 %When H is in the above sector, the RGB components equations are  


    
 %Subtract 120 from Hue  
 H2=H-120;  


    
 R1(H>=120&H<240)=I(H>=120&H<240).*(1-S(H>=120&H<240));  
 G1(H>=120&H<240)=I(H>=120&H<240).*(1+((S(H>=120&H<240).*cosd(H2(H>=120&H<240)))./cosd(60-H2(H>=120&H<240))));  
 B1(H>=120&H<240)=3.*I(H>=120&H<240)-(R1(H>=120&H<240)+G1(H>=120&H<240));  


    
 %BR Sector(240<=H<=360)  
 %When H is in the above sector, the RGB components equations are  


    
 %Subtract 240 from Hue  
 H2=H-240;  


    
 G1(H>=240&H<=360)=I(H>=240&H<=360).*(1-S(H>=240&H<=360));  
 B1(H>=240&H<=360)=I(H>=240&H<=360).*(1+((S(H>=240&H<=360).*cosd(H2(H>=240&H<=360)))./cosd(60-H2(H>=240&H<=360))));  
 R1(H>=240&H<=360)=3.*I(H>=240&H<=360)-(G1(H>=240&H<=360)+B1(H>=240&H<=360));  


    
 %Form RGB Image  
 RGB1(:,:,1)=R1;  
 RGB1(:,:,2)=G1;  
 RGB1(:,:,3)=B1;  


    
 %Represent the image in the range [0 255]  
 RGB1=im2uint8(RGB1);  
%  figure,imshow(RGB1);
    
%RGB to HSV---------------------------------------------------------------------------------------
% var_R = ( r / 255 );
% var_G = ( g / 255 );
% var_B = ( b / 255 );
% V=max(im,[],2);
% min=min(im,[],2);
% S=(V-min)/V;
% if V==min
%     H=0;
% elseif V==im(:,:,1)
%     H=60*((var_G-var_B)/(V-min));
% elseif V==im(:,:,2)
%     H=60*(2+(var_B-var_R)/(V-min));
% elseif V==im(:,:,3)
%     H=60*(4+(var_R-var_G)/(V-min));
% end
% if H<0
%    H=H+360;
% end
% 
% HSV=zeros(size(img));
% HSV(:,:,1)=H;
% HSV(:,:,2)=S;
% HSV(:,:,3)=V;
% 
% figure,imshow(HSV);
