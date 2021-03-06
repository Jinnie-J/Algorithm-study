## Implementation

- 코딩 테스트에서 구현이란 '머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정'이다.
- 문제 해결 분야에서 구현 유형의 문제는 '풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제'를 의미한다.
- 완전 탐색 - 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
- 시뮬레이션 - 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형

 ### 구현 관련 팁
- 탐색해야 할 전체 데이터의 개수가 100만 개 이하일 때 완전 탐색을 사용하면 적절하다.
- 좌표평면에서 '상하좌우'로 이동해야 하는 경우 dx, dy 리스트를 선언해 이동할 방향을 기록한다.    
이 외에 '상하좌우+대각선4방향' 으로 이동한다면 steps=[(-2,-1),(-2.1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)] 로 표현하는 것이 좋다.
- 2차원 리스트를 선언할 때는 리스트 컴프리헨션 문법을 사용하는 것이 효율적이다.
    ```
  d = [[0]] * m for _ in range(n)]