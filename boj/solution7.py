# boj 18352 특정 거리의 도시 찾기 - BFS

from collections import deque
import sys
# 도시 갯수, 도로 갯수, 거리정보, 출발도시
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

# 도로 정보 입력
for line in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited = [-1] * (n + 1)
visited[x] = 0 # 출발지에서 출발지 까지는 0

q = deque([x]) # 시작 노드와 시작노드 부터의 최단거리
while q :
    now = q.popleft()
    near = graph[now]
    for _ in near :
        if(visited[_] == -1) :
            q.append(_) # 최단거리를 1 증가하여 q에 추가
            visited[_] = visited[now] + 1


length = len(visited)
result = [i for i in range(length) if(visited[i] == k)]

if(len(result) == 0) :
    print(-1)
else :
    for _ in result :
        print(_)

'''
4 5 3 1
1 2
1 3
2 3
2 4
4 1

만약 visited를 초기화 시 False로 하면, visited[x] = 0 으로 설정한 곳에서 False로 인식하므로
시작노드인 1이 다시 업데이트 된다. 따라서 정답이 1이 나오게됨(정답은 -1)
'''

    