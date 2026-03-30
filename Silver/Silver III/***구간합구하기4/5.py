import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))

ans = [0]
temp = 0

for val in lst:
    temp += val
    ans.append(temp)
# print(ans)


for c in range(m):
    i, j = map(int, input().split())
    print(ans[j] - ans[i-1])

