# boj 2667 단지번호붙이기(DFS)

n = int(input())
apt = [list(map(int, input())) for _ in range(n)]
answer = []

def find_connect(x, y, result) :
    if(x < 0 or y < 0 or x >= n or y >= n) : # 범위가 벗어났을 때
        return 0
    elif(apt[x][y] != 1) : # 집이 없는 곳, 이미 방문한 곳일 때
        return 0
    else :
        apt[x][y] = 6
        result += find_connect(x - 1, y, 1) # 위
        result += find_connect(x + 1, y, 1) # 아래
        result += find_connect(x, y - 1, 1) # 왼
        result += find_connect(x, y + 1, 1) # 오
        return result # 없으면 0, 있으면 1 반환

for x in range(n) :
    for y in range(n) :
        if(apt[x][y] == 1) :
            answer.append(find_connect(x, y, 1))
            
print(len(answer))
answer = sorted(answer)
for _ in answer :
    print(_)