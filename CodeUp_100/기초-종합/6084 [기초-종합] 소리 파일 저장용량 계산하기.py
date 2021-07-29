#include<stdio.h>

h,b,c,s=input().split();
h=int(h); b=int(b); c=int(c); s=int(s);

print(round(h*b*s*c/8/1024/1024,1),"MB");