import sys

n = int(sys.stdin.readline().strip())

k = int(sys.stdin.readline().strip())

# 그래프 값 받기 
lst = [list(map(int, sys.stdin.readline().split())) for i in range(k)]

# 빈 그래프 만들고
graph = [[] for i in range(n+1)]

# 그래프 구조 만들기 
for u, v in lst:
    graph[u].append(v)
    graph[v].append(u)


# 방문 유무 리스트 만들기 
visited = [0] * (n+1)

# 깊이 우선 탐색 함수 적용 
def dfs(now, graph):
    visited[now] = 1
    for val in graph[now]:
        if visited[val] == 0:
            dfs(val, graph)



dfs(1, graph)
print(sum(visited) - 1)
    
