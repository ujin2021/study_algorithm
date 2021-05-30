# 2165 카드2

from collections import deque
n = int(input())
if(n == 1) :
    print(1)
else :
        q = deque([])
        for _ in range(1, n + 1) :
            q.append(_)

        while q :
            a = q.popleft() # 제일 위의 카드 버림
            if(len(q) == 1) :
                print(q.pop())
                break
            next_top = q.popleft() # 카드를 버린 후 가장 위에 있는 카드
            q.append(next_top) # 맨밑으로 옮긴다
