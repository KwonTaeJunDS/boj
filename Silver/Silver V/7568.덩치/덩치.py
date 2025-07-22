import sys


n = int(sys.stdin.readline().strip())

# 키와 몸무게 받음 
lst = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]

# 모두 1등으로 rank 초기화 
rank = [1 for i in range(len(lst))]

# 맨 첫번째 사람부터 끝까지 전부 비교 
for i in range(len(lst)):
    for j in range(len(lst)):
        # 이때 같은 사람은 비교할 필요 없음 
        if i == j:
            continue

        # j의 키와 몸무게가 i보다 전부 크다면 i번째 rank는 + 1 
        if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
            rank[i] += 1
            
print(*rank)
