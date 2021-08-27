# 튜플이 3개의 원소로 구성된다면 모든 원소가 첫 번째 원소의 순서에 맞게 정렬되고,
# 첫 번째 원소의 값이 같은 경우 두 번째 원소의 순서에 맞게 정렬되고, 두번째 원소의 값까지 같은 경우 세 번째 원소의 순서에 맞게 정렬된다.

n = int(input())
students = []

for i in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(students[i][0])
