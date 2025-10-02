import sys

n, hap = map(int, sys.stdin.readline().strip().split())

lst = list(map(int, sys.stdin.readline().strip().split()))

lst.sort()

best = 0


# 모든 경우의 수를 확인해야 되기 때문에 3중 for문 사용
# 해당 문제는 숫자 max값이 100이라 3중 for문 사용해도 충분함
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            s = lst[i] + lst[j] + lst[k]

            if s <= hap:
                if s >= best:
                    best = s

            else:
                break

print(best)
