function [k]=otsu(a)
b=a;
[c,d]=size(b);
b=reshape(b,[],1);
[m,n]=size(b);
weightb=zeros(3,256);
weightf=zeros(3,256);
r=1;
l=1;
for T=0:255
    [wb,wf,mb,mf,vrb,vrf]=cal(T,b,m);
    weightb(1,r)=wb;
    weightb(2,r)=mb;
    weightb(3,r)=vrb;
    r=r+1;
    weightf(1,l)=wf;
    weightf(2,l)=mf;
    weightf(3,l)=vrf;
    l=l+1;
end
%Within class variance
wcv=zeros(1,256);
for g=1:256
wcv(1,g)=((weightb(1,g)*weightb(3,g))+((weightf(1,g)*weightf(3,g))));
end
% min(wcv)
[threshold_value,val]=min(wcv);
 tval=(val-1)/256;
%  b=imresize(b,[c d])
 a=im2bw(a,tval);
k= medfilt2(a,[25 25]);
end

