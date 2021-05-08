# [greedy] 1931 회의실 배정
# 고려해야 할 것 : 회의 시작시간과 끝나는 시간이 같을 수 있음
import sys
n = int(input())
time = []
for _ in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    time.append((a, b))

time = sorted(time, key = lambda x : (x[1], x[0])) # 빨리 끝나는 것 중 빨리 시작하는 것
n = len(time)
end = 0 # 끝나는 시간은 0이상 자연수
result = 0 # 진행할 수 있는 회의의 갯수
for i in range(n) :
    # 다음 회의 시작시간이 이전 회의이 끝나는 시간보다 크거나 같으면
    if(time[i][0] >= end) : 
        end = time[i][1] # 다음 회의의 끝나는 시간을 end에 저장
        result += 1 # 진행할 수 있는 회의의 수 증가
print(result)