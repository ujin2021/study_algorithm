# 2559 수열
import sys
n, k = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))
result = pre = sum(c[:k])
for i in range(1, n - k + 1) :
    tmp = pre - c[i - 1] + c[i + k - 1]
    pre = tmp # 이전 온도의 합 저장
    result = max(tmp, result) # 합 들 중에서 가장 큰 합
print(result)