import sys

n = int(sys.stdin.readline().strip())

# 몸무게, 키 받기 
lst = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# 등수 리스트 (처음에는 모두 1등)
ans = [1 for i in range(n)]


# 이중 for문 돌면서 만약 나보다 덩치가 큰 사람이 있다면 + 1
for i in range(n):
    
    for j in range(n):

        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            ans[i] += 1

print(*ans)
    

