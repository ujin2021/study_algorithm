# level2 h-index

def solution(citations):
    answer = 0
    n = len(citations)
    citations = sorted(citations) # [0, 1, 3, 5, 6]
    for h in citations :
        l = len(citations[citations.index(h):])
        if(h < n and l >= h) :
            answer = h
        elif(l >= answer) :
            answer = l
    return answer 

print(solution([3, 0, 6, 1, 5]))
print(solution([4, 4, 4, 5, 0, 1, 2, 3]) == 4)
print(solution([3, 0, 6, 1, 5]) == 3)
print(solution([0, 0 ,1 ,1]) == 1)
print(solution([0, 1]) == 1)
print(solution([2, 7, 5]) == 2)
print(solution([10, 11, 12, 13]) == 4)
print(solution([22, 42]) == 2)
print(solution([12, 11, 10, 9, 8, 1]) == 5)
print(solution([6, 6, 6, 6, 6, 1]), solution([6, 6, 6, 6, 6, 1]) == 5)
print(solution([4, 4, 4]) == 3)
print(solution([10, 9, 4, 1, 1]), solution([10, 9, 4, 1, 1]) == 3) 