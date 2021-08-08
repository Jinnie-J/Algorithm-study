#sort 사용한 풀이
n= int(input())

array=[]
for i in range(n):
    array.append(int(input()))

array.sort()
array.reverse()

for i in array:
    print(i, end=' ')


#sorted 사용한 풀이
n= int(input())

array=[]
for i in range(n):
    array.append(int(input()))

array=sorted(array, reverse=True)

for i in array:
    print(i, end=' ')