# 이것이 취업을 위한 코딩테스트다
# boj 18352 특정 거리의 도시 찾기 - BFS
# 정답코드
# 모든 간선의 가중치가 동일(1) => BFS 사용
# deque : 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조

from collections import deque

# 도시 개수, 도로 개수, 거리정보, 출발도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 도시가 1 ~ N 이니까

# 도로 정보 입력받기
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 자기 자신까지 거리는 0

# BFS
q = deque([x])
# print('q : ', q)
# print('graph : ', graph)
while q :
    now = q.popleft()
    print(f'---now({now})---')
    # 현재 도시에서 이동할 수 있는 모든 노드 확인
    for next_node in graph[now] :
        if(distance[next_node] == -1) :
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            print(f'q : {q}')
            print(f'distance : {distance}')

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1) :
    if(distance[i] == k) :
        print(i)
        check = True

# 최단거리가 k인 도시가 없다면
if(check == False) :
    print(-1)

