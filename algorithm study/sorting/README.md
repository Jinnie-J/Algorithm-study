## Sorting

- 정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.
- 정렬 알고리즘으로 데이터를 정렬하면 이진 탐색(Binary Search)이 가능해진다.

### 선택 정렬
- 매번 '가장 작은 것을 선택'한다는 의미에서 선택정렬 알고리즘이라고 한다.
- 가장 작은 것을 선택해서 앞으로 보내는 과정을 반복해서 수행하다 보면, 전체 데이터의 정렬이 이루어진다.
  ```
  array = [7,5,9,0,3,1,6,2,4,8]
  
  for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
      if array[min_index] > array[j]:
        min_index=j
  array[i], array[min_index] = array[min_index], array[i] #스와프
- 선택 정렬은 N-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다. 시간복잡도는 O(N^2)이다.

### 삽입 정렬
- 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 삽입정렬이라고 부른다.
- 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다. 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽입된다는 점이 특징이다.
  ```
  array = [7,5,9,0,3,1,6,2,4,8]
  
  for i in range(1, len(array)):
    for j in range(i,0,-1):  #인덱스 i부터 1까지 감소하며 반복하는 문법
      if array[j] < array[j-1]:
        array[j], arraj[j-1] = array[j-1], array[j]
      else:
        break

- 삽입 정렬의 시간 복잡도는 O(N^2)인데, 선택 정렬과 마찬가지로 반복문이 2번 중첩되어 사용되었다.
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.

### 퀵 정렬
- 퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.
- 퀵 정렬에서는 피벗이 사용된다. 큰 숫자와 작은 숫자를 교활할 때, 교환하기 위한 '기준'을 바로 피벗이라고 표현한다.
- 피벗을 설정한 뒤에 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다. 그다음 큰 데이터와 작은 데이터의 위치를 서로 교환해준다.
- 피벗의 왼쪽에는 피벗보다 작은 데이터가 위치하고, 피벗의 오른쪽에는 피벗보다 큰 데이터가 위치하도록 하는 작업을 분할 혹은 파티션이라고 한다.
- 왼쪽 리스트와 오른쪽 리스트에서도 각각 피벗을 설정하여 동일한 방식으로 정렬을 수행하면 전체 리스트에 대하여 모두 정렬이 이루어진다.
- '재귀 함수'와 동작 원리가 같다. 실제로 퀵 정렬은 재귀 함수 형태로 작성했을 때 구현이 매우 간결해진다.
  ```
  array=[5,7,9,0,3,1,6,2,4,8]
  
  def quick_sort(array, start, ent):
    if start >= end:  #원소가 1개인 경우 종료
      return
    pivot = start  #피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
      while left <= end and array[left] <= array[pivot]:
        left+=1
      while right > start and array[right] >= array[pivot]:
        right+=1
      if left > right:
        array[right] , array[pivot] = array[pivot], array[right]
      else:
        array[left], array[right] = array[right], array[left] 
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
  
  quick_sort(array, 0, len(array)-1)
  
- 파이썬의 장점을 살린 퀵 정렬 소스코드
  ```
  array= [8,7,9,0,3,1,6,2,4,8]
  
  def quick_sort(array):
    if len(array) <= 1:
      return array
    
    pivot = array[0]  #피벗은 첫 번째 원소
    tail=array[1:]  #피벗을 제외한 리스트
  
    left_side= [x for x in tail if x<=pivot] #분할된 왼쪽 부분
    right_side= [s for s in tail if x>pivot] #분할된 오른쪽 부분
  
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
  
  quick_sort(array)

- 퀵 정렬의 평균 시간 복잡도는 O(NlogN)이다. 

### 계수 정렬
- 계수 정렬 알고리즘은 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.
- '데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때'만 사용할 수 있다.
- 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성한다. 처음에는 리스트의 모든 데이터가 0이 되도록 초기화한다. 그 다음 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시키면 계수 정렬이 완료된다.
- 결과적으로 리스트에는 각 데이터가 몇 번 등장했는지 그 횟수가 기록된다.
  ```
  array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
  count = [0] * (max(array)+1)
  
  for i in range(len(array)):
    count[array[i]]+=1
  
  for i in range(len(count)):
    for j in range(count[i]):
      print(i, end=' ')

- 모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최대값의 크기를 K라고 할 때, 계수 정렬의 시간 복잡도는 (O+K)이다.

### 파이썬의 정렬 라이브러리
1. sorted
  ```
  array= [7,5,9,0,3,1,6,2,4,8]
  result = sorted(array)
  ```
2. sort
  ```
  array= [7,5,9,0,3,1,6,2,4,8]
  array.sort()
  ```
3. 정렬 기준(key) 설정
  ```
  array= [('바나나',2), ('사과',5), ('당근',3)]
  
  def setting(data):
    return data[1]
  result = sorted(array, key=setting)
  ```
