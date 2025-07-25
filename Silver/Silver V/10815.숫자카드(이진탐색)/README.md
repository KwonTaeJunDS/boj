[문제링크](https://www.acmicpc.net/problem/10815)

# 문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 문제 접근 방법
+ 반복 비교를 통해 b의 수가 a에 존재하는지 확인해야 함
+ 단순 반복 비교는 시간 초과 발생
+ 정렬 + 이진 탐색 알고리즘을 사용해야 함
+ 이진 탐색이란?
  + 정렬된 배열에서 원하는 값을 O(log N) 시간에 찾는 알고리즘
  + 정렬 후 배열 중간값을 먼저 비교해 찾는 값이 중간값보다 작으면 왼쪽으로 탐색 범위 축소
  + 크면 오른쪽으로 탐색 범위 축소
  + 같으면 찾았으니 넘어감
