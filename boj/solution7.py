# boj 18352 특정 거리의 도시 찾기 - BFS

from collections import deque

# 도시 갯수, 도로 갯수, 거리정보, 출발도시
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 도로 정보 입력
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([[x, 0]]) # 시작 노드와 시작노드 부터의 최단거리
visited = [False] * (n + 1)
check = False # q를 검사하는 동안 k와 같은 것이 없으면 False

while q :
    now = q.popleft()
    if(visited[now[0]] == False) : # 방문하지 않은 노드라면
        visited[now[0]] = True # 방문 했다고 표시
        if(now[1] == k) : # 최단거리가 k와 같으면
            print(now[0]) # 프린트
            check = True
    near = graph[now[0]]
    for _ in near :
        q.append([_, now[1] + 1]) # 최단거리를 1 증가하여 q에 추가

if(check == False) :
    print(-1)