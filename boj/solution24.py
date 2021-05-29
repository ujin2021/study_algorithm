# 1158 요세푸스 문제
n, k = map(int, input().split())
k -= 1
idx = 0
num = [i for i in range(n)]
result = []
while n > 0 :
    idx = (idx + k) % n
    result.append(num[idx] + 1)
    num.pop(idx)
    n -= 1

if(len(result) == 1) :
    print(f'<{result[0]}>')
else :
    print(f'<{result[0]}', end = '')
    for i in result[1 : -1] :
        print(f', {i}', end = '')
    print(f', {result[-1]}>')