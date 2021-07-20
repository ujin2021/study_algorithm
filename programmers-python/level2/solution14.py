# 프로그래머스 더 맵게 -> tistory

import heapq

def solution(scoville, K):
  h = []
  c = 0

  for i in scoville :
    heapq.heappush(h, i)

  while True :
    a = heapq.heappop(h)
    if(a >= K) :
      break
    elif(len(h) == 0 and a < K) :
      return -1
    b = heapq.heappop(h)
    new = a + b * 2
    heapq.heappush(h, new)
    c += 1
    
  return c