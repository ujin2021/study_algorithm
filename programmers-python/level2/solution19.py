# 기능개발
# import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque([])
    l = len(progresses)
    for i in range(l) :
        p = progresses[i]
        s = speeds[i]
        if((100 - p) % s != 0) :
            q.append((100 - p) // s + 1)
        else :
            q.append((100 - p) // s)
        # q.append(round((100 - p) / s))
    print('q : ', q)
    count = 1
    pre = q[0]
    for i in range(1, len(q)) :
        if(q[i] <= pre) :
            count += 1
        else :
            answer.append(count)
            count = 1
            pre = q[i]

    answer.append(count)
    # print('real answer : ', answer)
    return answer

print(solution([93, 30, 55], [1, 30, 5]) == [2, 1])
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2])
print(solution([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5]) == [3, 3])
print(solution([70], [20]) == [1])