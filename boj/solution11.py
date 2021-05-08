# [greedy] 1941 소문난 칠공주
import sys
from itertools import combinations

graph = []
for _ in range(5) :
    graph.append(sys.stdin.readline().strip())

std = [(i, j) for i in range(5) for j in range(5)] # 모든 좌표 생성
total_comb = list(combinations(std, 7)) # 모든좌표중 7개 조합

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y, visited) :
    if(len(set(sum(visited, []))) == 1) : # 모두 방문했다면
        return True
    if(x < 0 or y < 0 or x > 4 or y > 4 or visited[x][y]) : # 좌표 범위를 벗어나거나 이미 방문했다면
        # print('over')
        return False
    visited[x][y] = True
    for _ in range(4) :
        if(dfs(x + dx[_], y + dy[_], visited)) :
            return True
    return False

# 좌표 7개가 다 붙어있는지 확인
def check(location) :
    visited = [[True for i in range(5)] for j in range(5)]
    for _ in location :
        visited[_[0]][_[1]] = False # 확인해야 할 좌표만 False로
    return dfs(location[0][0], location[0][1], visited)

result = 0
for comb in total_comb:
    tmp = [graph[_[0]][_[1]] for _ in comb]
    if(tmp.count('Y') > 3) : # C가 4개 이상이어야 함
        continue
    if(check(comb)) : # C가 4개이상인 경우에만 좌표가 모두 붙어있는지 확인
        result += 1
print(result)