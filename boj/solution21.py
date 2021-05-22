# 17128 소가 정보섬에 올라온 이유 [구현]

import sys
n, q = map(int, sys.stdin.readline().strip().split())
quality = list(map(int, sys.stdin.readline().strip().split()))
w = list(map(int, sys.stdin.readline().strip().split()))

tmp = []
for _ in range(n) :
    tmp.append(quality[_ % n] * quality[(_ + 1) % n] * quality[(_ + 2) % n] * quality[(_ + 3) % n])

result = sum(tmp)
for i in w :
    i -= 1
    for j in range(i - 3, i + 1) :
        result -= tmp[j] * 2
        tmp[j] *= -1
    print(result)