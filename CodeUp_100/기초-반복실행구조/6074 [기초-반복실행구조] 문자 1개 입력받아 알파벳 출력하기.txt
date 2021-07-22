#include<stdio.h>

# print(..., end=' ') 와 같이 작성하면 값 출력 후 공백문자 ' '를 출력한다. 즉, 마지막에 줄을 바꾸지 않고 빈칸만 띄운다.
c= ord(input());
t= ord('a');
while t<=c:
    print(chr(t),end=' ');
    t+=1;