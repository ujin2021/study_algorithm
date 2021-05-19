# 9205 맥주 마시면서 걸어가기

import sys
from collections import deque

# 맨하탄 거리 구하는 함수
def manhattan(loc1, loc2) :
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

# 갈 수 있는 곳(맨하탄 거리가 1000 이하)에 대한 양방향 그래프 만드는 함수
def beer_graph(loc, n) :
    global location
    graph = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(i + 1, n) :
            if(manhattan(location[i], location[j]) <= 1000) :
                graph[i][j] = True
                graph[j][i] = True
    return graph

# 목적지 까지 갈 수 있는지 확인하는 함수
def dfs(graph, visited) :
    n = len(graph)
    q = deque([0])
    while q :
        now = q.popleft()
        if(now == n - 1) : # 도착지 이면
            return True 
        move = graph[now]
        for _ in range(n) : # now에서 갈 수 있는 곳
            if(move[_] and visited[now][_] == False) : # now에서 갈 수 있고, 방문하지 않았으면
                visited[now][_] = True # 방문했다고 표시
                visited[_][now] = True
                q.append(_)
    return False

def beer(loc, n) :
    graph = beer_graph(loc, n)
    visited = [[False for _ in range(n)] for _ in range(n)]
    if(dfs(graph, visited)) : # 목적지 까지 갈 수 있으면
        return 'happy'
    return 'sad' # 목적지 까지 갈 수 없으면

t = int(input()) # test case
result = []
for _ in range(t) :
    location = [] # 좌표 저장
    c_n = int(sys.stdin.readline()) # 편의점 수
    for i in range(c_n + 2) : # 총 좌표 수는 편의점수(n) + 집(1) + 도착지(1)
        x, y = map(int, sys.stdin.readline().split())
        location.append((x, y)) 
    result.append(beer(location, c_n + 2))

print('\n'.join(result))