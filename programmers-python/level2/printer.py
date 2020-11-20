# 프린터

def solution(priorities, location):
    answer = []
    priorities = list(enumerate(priorities))
    while len(priorities) > 1 :
        first = priorities[0][1]
        check = 0
        for i in range(1, len(priorities)) :
            if(first < priorities[i][1]) :
                priorities = priorities[1:] + [priorities[0]]
                break
            check += 1
            if(check == len(priorities) - 1) :
                answer.append(priorities[0])
                priorities = priorities[1:]
    
    answer.append(priorities[0])

    for i in range(len(answer)) :
        if(answer[i][0]== location) :
            return i + 1

print(solution([2, 1, 3, 2], 2))
print(solution([2, 1, 3, 2], 2) == 1)
print(solution([1, 1, 9, 1, 1, 1], 0) == 5)
