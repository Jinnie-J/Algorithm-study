#include <stdio.h>

# input 값을 아스키 코드 값으로 변환 후, 다시 유니코드 문자 형태로 변환
n= ord(input());
print(chr(n+1));