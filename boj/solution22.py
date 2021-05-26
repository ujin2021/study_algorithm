# 2644 촌수계산
import sys
from collections import deque

n = int(sys.stdin.readline()) # 사람수
graph = [[False for _ in range(n)] for _ in range(n)] # 부모 자식 관계 그래프
a, b = map(int, sys.stdin.readline().split())
a, b = a - 1, b - 1
m = int(sys.stdin.readline())
for _ in range(m) :
    p, c = map(int, sys.stdin.readline().split())
    graph[p - 1][c - 1] = True
    graph[c - 1][p - 1] = True

def bfs(start, end, visited) :
    global graph
    check = False # 도착지를 찾았는지 여부
    q = deque([start])
    visited[start] = 0 # 자기자신은 0촌
    while q :
        now = q.popleft()
        if(now == end) :
            check = True
            break
        go = graph[now]
        for i in range(n) :
            if(go[i] and visited[i] == -1) : # 갈 수 있고, 방문하지 않은 곳
                visited[i] = visited[now] + 1 # now촌수 + 1
                q.append(i)
    if(check) :
        return visited[end]
    else :
        return -1

visited = [-1 for _ in range(n)] # 노드 방문 여부 및 자신이 start로 부터 몇촌인지 나타냄
print(bfs(a, b, visited))

