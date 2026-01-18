import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# 미로 만들기 
lst = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]
# print(lst)

# 방향 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


q = deque([[0, 0]])


# 큐가 빌 때까지
while q:
    # 큐의 현재 위치를 꺼냄 
    x, y = q.popleft()
   
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 벽이거나 인덱스를 넘어서면 패스 
        if nx < 0 or nx >= n or ny <0 or ny >= m:
            continue

        # 1 이라면 방문 
        if lst[nx][ny] == 1:
            lst[nx][ny] = lst[x][y] + 1
            # 해당 위치를 큐에 다시 넣어줌 
            q.append([nx, ny])


print(lst[n-1][m-1])


