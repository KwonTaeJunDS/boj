import sys

input = sys.stdin.readline

m, n = map(int, input().split())

lst = list(map(int, input().split()))

temp = 0

ans = [0]

for val in lst:
    temp += val
    ans.append(temp)


for c in range(n):
    i, j = map(int, input().split())

    print(ans[j] - ans[i-1])

    
