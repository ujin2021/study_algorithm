# 1260 DFS와 BFS
# https://velog.io/@i-zro/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%BD%94%ED%85%8C-%EB%8C%80%EB%B9%84-DFSBFS-%EB%B0%B1%EC%A4%80-1260%EB%B2%88-DFS%EC%99%80-BFS

N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
# print(matrix)

for _ in range(M) :
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V) :
    visited[V] = 1 # 방문한 노드는 1로
    print(V, end = ' ')
    for i in range(1, N + 1) :
        if(visited[i] == 0 and matrix[V][i] == 1) :
            dfs(i)

def bfs(V) :
    queue = [V] # 거쳐야 할 중앙 노드
    visited[V] = 0 # 방문한 노드는 0으로
    while queue :
        V = queue.pop(0)
        print(V, end = ' ')
        for i in range(1, N + 1) :
            if(visited[i] == 1 and matrix[V][i] == 1) :
                visited[i] = 0
                queue.append(i)

dfs(V)
print()
bfs(V)