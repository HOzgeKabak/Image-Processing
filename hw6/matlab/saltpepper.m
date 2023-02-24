function R=saltpepper(M,N,a,b)
if nargin<=2
    a=0.05;
    b=0.05;
end

R(1:M,1:N)=0.5;
X=rand(M,N);
c=find(X<=a);
R(c)=0;
u=a+b;
c=find(X>a & X<=u);
R(c)=1;
end