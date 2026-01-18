import sys
from collections import deque


n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

lst = [list(map(int, sys.stdin.readline().split())) for i in range(k)]

graph = [[] for i in range(n+1)]

for u, v in lst:
    graph[u].append(v)
    graph[v].append(u)


visitied = [0] * (n+1)

# bfs 함수 
def bfs(now, graph):
    # 큐 이용 
    q = deque([now])
    visitied[now] = 1

    # q가 빌 때까지
    while q:
        now = q.popleft()

        for val in graph[now]:
            # 만약 방문을 안했다면
            if visitied[val] == 0:

                visitied[val] = 1
                q.append(val)


bfs(1, graph)
print(sum(visitied)-1)
