# boj 3190 뱀

n = int(input()) # board size
board = [[0 for _ in range(n)] for _ in range(n)]

k = int(input()) # apple 
for _ in range(k) :
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

l = int(input()) # 방향 변환 횟수
turn = dict()
for _ in range(l) :
    a, b = input().split()
    turn[int(a)] = b

time = 0
head_x, head_y = 0, 0

move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오, 아, 왼, 위
h_dir = 0 # 처음 방향은 오른쪽
h_history = [[0, 0]]

while True :
    time += 1

    head_x += move[h_dir][0]
    head_y += move[h_dir][1]
    
    # head가 좌표를 벗어나거나 자기 몸에 부딪혔을 때
    if(head_x >= n or head_y >= n or head_x < 0 or head_y < 0 or [head_x, head_y] in h_history) :
        break

    h_history.append([head_x, head_y]) # head 전진

    if(board[head_x][head_y] == 1) : # 전진했을 때 사과가 있는 경우
        board[head_x][head_y] = 0 # 사과 사라짐
    else : # 전진했을 때 사과가 없는 경우
        h_history.pop(0) # 맨 처음 들어온 좌표 삭제(tail)

    if(time in turn) :
        if(turn[time] == 'D') :
            h_dir = (h_dir + 1) % 4
        else :
            h_dir = (h_dir + 3) % 4
    # print(f'time : {time}, head_x : {head_x}, head_y : {head_y}, h_dir : {h_dir}')
print(time)