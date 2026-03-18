import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())

# 덱 선언 
md = deque()
lst = list(map(int, input().split()))

for i in range(n):
    # 현재 숫자가 덱 맨 뒤보다 작은지 확인
    while md and md[-1][0] > lst[i]:
        # 만약 작다면 덱 맨 뒤 날림
        # 이를 통해 덱에는 가장 최소값 데이터만 남게됨
        md.pop()

    # 그 이후 새로운 값과 현재 인덱스를 추가
    md.append((lst[i], i))

    # 인덱스가 윈도우보다 작으면 popleft로 왼쪽값 버림
    if md[0][1] <= i-l:
        md.popleft()
    
    print(md[0][0], end=' ')



