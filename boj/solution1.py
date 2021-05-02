n, m, v = map(int, input().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited_dfs = [0 for _ in range(n + 1)]
visited_bfs = [0 for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 양방향 이라서

from collections import deque
def bfs(graph, visited, start) :
    q = deque([start])
    visited[start] = 1 # 1이 방문
    while q :
        now = q.popleft()
        print(now, end = ' ')
        for node in range(1, n + 1) :
            if(graph[now][node] == 1 and visited[node] == 0) : # 방문하지 않았을 때
                visited[node] = 1 # 방문했다고 표시
                q.append(node) # 탐색해야 하므로 q에 넣어준다

def dfs(graph, visited, start) :
    print(start, end = ' ')
    visited[start] = 1 # 방문했다고 표시
    for node in range(1, n + 1) :
       if(graph[start][node] == 1 and visited[node] == 0) : # 방문하지 않았으면
           dfs(graph, visited, node)

dfs(graph, visited_dfs, v)
print()
bfs(graph, visited_bfs, v)