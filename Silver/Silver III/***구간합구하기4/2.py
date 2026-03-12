import sys


n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

temp = 0
ans = [0]

for val in lst:
    temp += val
    ans.append(temp)

for c in range(m):
    i, j = map(int, sys.stdin.readline().split())

    print(ans[j] - ans[i-1])



