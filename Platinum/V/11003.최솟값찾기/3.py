import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())

lst = list(map(int, input().split()))
md = deque()

for i in range(n):
    while md and md[-1][0] > lst[i]:
        md.pop()
    
    md.append((lst[i], i))

    if md[0][1] <= i-l:
        md.popleft()

    print(md[0][0], end=' ')
