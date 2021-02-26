# level2 카펫
import math
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    k = int(math.sqrt(total)) + 1
    for i in range(3, k) :
        if(total % i == 0) :
            h = i
            w = total // i
            if (2 * (h+w) - 4 == brown) :
                return [w, h]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))