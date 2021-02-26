# level2 소수찾기
from itertools import permutations
import math

def check(i) :
    if i < 2 :
        return False
    k = math.sqrt(i) # 소수는 제곱근 까지만 검사하면 된다
    for j in range(2, int(k) + 1) :
        if(i % j == 0) :
            return False
    return True

def solution(numbers):
    answer = 0
    per = []
    for k in range(1, len(numbers) + 1) :
        perlist = list(map(int, map(''.join, permutations(list(numbers), k))))
        per += perlist
    per = set(per)
    for i in per :
        # print(f'i : {int(i)}, result : {check(int(i))}')
        if check(int(i)) :
            answer += 1
    return answer

print(solution('17'))
print(solution('011'))