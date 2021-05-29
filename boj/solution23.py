# 1697 숨바꼭질 [dfs]
from collections import deque

a, b = map(int, input().split())
visited = [0] * 100001 # 0 ≤ N, K ≤ 100,000

q = deque([a])
visited[a] = 0
while q :
    now = q.popleft()
    if(now == b) :
        print(visited[now])
        break
    if(now - 1 >= 0 and visited[now - 1] == 0) :
        q.append(now - 1)
        visited[now - 1] = visited[now] + 1
    if(now + 1 < 100001 and visited[now + 1] == 0) :
        q.append(now + 1)
        visited[now + 1] = visited[now] + 1
    if(now * 2 < 100001 and visited[now * 2] == 0) :
        q.append(now * 2)
        visited[now * 2] = visited[now] + 1