# 2018 카카오 프렌즈 4블록

# 2x2 블록을 찾기위해 탐색해야 하는 범위
dx = [[-1, -1, 0], [-1, -1, 0], [0, 1, 1], [0, 1, 1]]
dy = [[-1, 0, -1], [0, 1, 1], [-1, -1, 0], [1, 0, 1]]

# 2x2 블록 존재여부
def findFour(graph, start) :
  x, y = start
  m, n = len(graph), len(graph[0])
  icon = graph[x][y]
  for i in range(4) :
    result = []
    for j in range(3) :
      go_x, go_y = x + dx[i][j], y + dy[i][j]
      if(go_x >= m or go_x < 0 or go_y >= n or go_y < 0) : # 범위가 넘어가면
        break
      elif(graph[go_x][go_y] == "0") : # 이미 당겨서 icon이 없는 부분이면
        break
      elif(graph[go_x][go_y] == icon) :
        result.append((go_x, go_y))
    if(len(result) == 3) : # 2x2에서 자신제외하고 3개 찾으면
      result.append(start)
      return tuple(sorted(result, key = lambda x : (x[0], x[1])))
  return False

# board 탐색(2x2가 있는지) -> 있으면 2x2 좌표 반환
def searchBoard(m, n, board) :
  result = []
  for i in range(m) :
    for j in range(n) :
      if(board[i][j] == "0") :
        continue
      tmp = findFour(board, (i, j))
      if(tmp) :
        result.append(tmp)
  result = list(set(result))
  return result

# board 빈부분 채우기
def pullBoard(m, n, board) :
  for j in range(n) :
    tmp = []
    for i in range(m) :
      tmp.append(board[i][j])
    if(tmp.count("0") == m or tmp.count("0") == 0) :
      continue
    c = tmp.count("0")
    tmp_s = ''.join(tmp).replace("0", '')
    pull_s = "0" * c + tmp_s
    for i in range(m) :
      # print(f'{board[i]} = {board[i][:j]} + {pull_s[i]} + {board[i][j+1:]}')
      board[i] = board[i][:j] + pull_s[i] + board[i][j+1:]
  return board

# 2x2에 해당한 좌표들 count하기
def count(result) :
  answer = []
  for i in result :
    for j in range(4) :
      answer.append(i[j])
  return len(set(answer))

def solution(m, n, board):
    answer = 0
    while True :
      search_result = searchBoard(m, n, board)
      answer += count(search_result) # 여기서 count해줘야 함(다 끝나고 하면 당겨진 부분 좌표가 원래 좌표와 같게나오기 때문)
      if(len(search_result) == 0) :
        break
      for i in search_result :
        for j in range(4) :
          x, y = i[j][0], i[j][1]
          board[x] = board[x][:y] + "0" + board[x][y+1:]
      board = pullBoard(m, n, board)
    return answer


# testcase
print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"]) == 12) 
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]) == 14)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15)
print(solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]) ==24)
print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]) == 4)
print(solution(4, 5, ["AAAAA","AUUUA","AUUAA","AAAAA"]) == 14)
print(solution(2,2,["AA", "AA"]) == 4)
print(solution(2,2, ["AA", "AB"]) == 0)
print(solution(3,2, ["AA", "AA", "AB"]) == 4)
print(solution(4,2, ["CC", "AA", "AA", "CC"]) == 8)
print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]) == 8)
print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"]) == 8)