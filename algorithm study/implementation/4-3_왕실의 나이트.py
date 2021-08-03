
input_data= input()
row= int(input_data[1])
column= int(ord(input_data[0])) - int(ord('a'))+1

#나이트가 이동할 수 있는 8가지 방향 정의
steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
count=0

for step in steps:
    next_row=row+step[0]
    next_column=column+step[1]
    if next_row>0 and next_row<9 and next_column>0 and next_column<9:
        count+=1

print(count)
