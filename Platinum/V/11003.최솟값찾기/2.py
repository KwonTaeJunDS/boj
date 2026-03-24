import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())

lst = list(map(int, input().split()))

dl = deque()

for c in range(n):

    while dl and dl[-1][0] > lst[c]:
        dl.pop()

    dl.append((lst[c], c))


    if dl[0][1] <= c-l:
        dl.popleft()

    print(dl[0][0], end=' ')
