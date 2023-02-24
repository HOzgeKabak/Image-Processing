%Halime Özge KABAK
%180403001
% Image Processing HW6
%Add Noise
%--------------------------------------------------------------------------
%Salt and Pepper Noise
% f=imread('lenna.png');
% figure
% imshow(f)
% [M, N]= size(f);
% R = saltpepper(M, N, 0.05, 0.05);
% c = find (R==0);
% gp = f;
% gp(c) = 0;
% d = find (R==1);
% gp(d) = 255;
% figure
% imshow(gp)
%For eliminating noise ==> median filter (min filter for pepper) (max filter for salt)
% %--------------------------------------------------------------------------
% % %Gaussian Noise
% S = 20; %standart deviation
% I = imread('cameraman.jpg');
% [M, N]= size(I);
% Gframe=double(I);
% Gframe = Gframe - min(Gframe(:));
% Gframe = Gframe / max(Gframe(:));
% figure;
% imshow((I))
% % J = double(I) + S.*randn(size(I));
% % figure;
% % imshow(J./255)
% n=0.1*noises('gaussian', M,N);
% J=n+Gframe;
% figure;
% imshow((J))
% % For eliminating noise ==>image averaging/ Arithmetic/Geometric/ Harmonic Mean Filter
% Kr=3;
% Kc=3;
% J=im2double(J);
% %J=(Kr*Kc)./imfilter(1./(J+eps),ones(Kr,Kc),"replicate"); %Harmonic filter
% %J=exp(imfilter(log(J),ones(Kc,Kr),"replicate")).^(1/(Kr*Kc)); %Geometric Mean Filter
% %J=wiener2(J,[3,3]); %Adaptive Filter
% figure;
% imshow((J))
% %--------------------------------------------------------------------------
% %Erlang Noise
% n=0.1*noises('erlang', M,N);
% Gframe=imread('cameraman.jpg');
% Gframe=double(Gframe);
% Gframe = Gframe - min(Gframe(:));
% Gframe = Gframe / max(Gframe(:));
% J = Gframe + n;
% figure
% imshow(J)
% %--------------------------------------------------------------------------
% %Uniform Noise
% n2=0.3*noises('uniform', M,N);
% J = Gframe + n2;
% figure
% imshow(J)
% %--------------------------------------------------------------------------
% %Rayleigh Noise
% n3=0.3*noises('rayleigh', M,N);
% J = Gframe + n3;
% figure
% imshow(J)
% %--------------------------------------------------------------------------
% %Exponential Noise
% n4=0.2*noises('exponential', M,N);
% J = Gframe + n4;
% figure
% imshow(J)
% %--------------------------------------------------------------------------
% %Lognormal Noise
% n5=0.3*noises('lognormal', M,N);
% J = Gframe + n5;
% figure
% imshow(J)
%--------------------------------------------------------------------------
%Periodic Noise
 t = imread ('cameraman.jpg');
s = size (t); % It assigns the size of t to s.
[x, y] = meshgrid (1: s (1), 1: s (2)); % x, y dimensional matrix.
p = sin (x / 3 + y / 5) +1; % sins
imshow (p)
k = (im2double (t) + p / 2) / 2;
imshow (k)
[x, y] = meshgrid (1: 256,1: 256);
p = 1 + sin (x + y / 1.5);
tp = (double (k) / 128 + p) / 8;
imshow (tp);
af = fftshift (fft2 (tp));
imshow (mat2gray (log (1 + abs (af))));
tp(88,:)=0;
tp(171,:)=0;
tp(:,156)=0;
tp(:,102)=0;
af = fftshift (fft2 (tp));
imshow (mat2gray (log (1 + abs (af))));
s=ifftshift(ifft2(af));
imshow(mat2gray((1+abs(s))))
%--------------------------------------------------------------------------
%SNR
img=f;
img=double(img(:));
ima=max(img(:));
imi=min(img(:));
ims=std(img(:));
snr=10*log((ima-imi)./ims);
disp(snr)