#include<stdio.h>

# python 언어에서 정수값 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)로 평가된다

n=int(input());
print(not bool(n));