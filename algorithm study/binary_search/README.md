## binary search

### 순차 탐색
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 원소(데이터)를 찾을 수 있다는 장점이 있다.
- 리스트에 특정 값의 원소가 있는지 체크할 때도 순차 탐색으로 원소를 확인하고, 리스트 자료형에서 특정한 값을 가지는 원소의 개수를 세는 count() 메서드를 이용할 때도 내부에서는 순차 탐색이 수행된다.
  ```
  def sequential_search(n, target, array):
    for i in range(n):
      if array[i] == target:
        return i+1

### 이진 탐색
- 데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있다는 특징이 있다.
- 위치를 나타내는 변수 3개를 사용하는데 탐색하고자 하는 범위의 시작점, 끝점, 중간점이다.
- 찾으려는 데이터와 중간점위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 게 이진탐색의 과정이다.
- 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도가 O(logN)이다.
- 이진 탐색을 구현하는 방법은 재귀 함수를 이용하는 방법, 단순하게 반복문을 이용하는 방법 2가지 이다.
  ```
  #이진 탐색 소스코드 구현(재귀 함수)
  def binary_search(array, target, start, end):
    if start > end:
      return None
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      return binary_search(array, target, start, mid-1)
    else:
      return binary_search(array, target, mid+1, end)
  
  #이진 탐색 소스코드(반복문)
  def binary_search(array, target, start, end):
    while start <= end:
      mid= (start+end) //2
      if array[mid] == target:
        return mid
      elif array[mid] > target:
        end = mid+1
      else:
        start = mid+1
    return None

### 트리 자료구조
- 트리 자료구조는 노드와 노드의 연결로 표현하며 여기에서 노드는 정보의 단위로서 어떠한 정보를 가지고 있는 개체로 이해할 수 있다.
- 큰 데이터를 처리하는 소프트웨어는 대부분 데이터를 트리 자료구조로 저장해서 이진탐색과 같은 기법을 이용해 빠르게 탐색이 가능하다.

### 이진 탐색 트리
- 이진 탐색 트리의 특징
  1. 부모 노드보다 왼쪽 자식 노드가 작다.
  2. 부모 노드보다 오른쪽 자식 노드가 크다.
- 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다. 예를 들어 데이터의 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면 이진 탐색 알고리즘을 의심해보자.
- 입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다.
  ```
  inport sys
  input_data = sys.stdin.readline().rstrip()

