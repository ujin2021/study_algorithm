# 1107 리모컨
# https://javaiyagi.tistory.com/585 참고하여 풀이

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
b = list(sys.stdin.readline().split())

current_ch = 100
min_cnt = abs(current_ch - N)

for c in range(1000000) :
    c = str(c)
    for j in range(len(c)) :
        if(c[j] in b) :
            break # 숫자버튼으로 이동할 수 없는 채널
        elif(len(c) - 1 == j): # 마지막 까지 탐색했는데 숫자버튼으로 갈 수 있는 곳이면
            min_cnt = min(min_cnt, abs(int(c) - N) + len(c)) # 현재의 min값과 비교

print(min_cnt)