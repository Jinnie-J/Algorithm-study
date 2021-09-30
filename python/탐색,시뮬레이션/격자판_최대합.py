
n= int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

dy=[]

for i in range(n):
    rowsum=0
    columnsum=0
    for j in range(n):
        rowsum+=arr[i][j]
        columnsum+=arr[j][i]
    dy.append(rowsum)
    dy.append(columnsum)

diagonalsum1=0
diagonalsum2=0

for i in range(n):
    diagonalsum1+=arr[i][i]
    diagonalsum2+=arr[i][n-i-1]

dy.append(diagonalsum1)
dy.append(diagonalsum2)


print(max(dy))
