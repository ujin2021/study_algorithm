'''
v	result
[[1, 4], [3, 4], [3, 10]]	[1, 10]
[[1, 1], [2, 2], [1, 2]]	[2, 1]
'''
def solution(v):
    answer = []
    x = sorted(list(map(lambda x:x[0], v)))
    y = sorted(list(map(lambda y:y[1], v)))
    # print('x : ', x, ', y : ', y)
    # if (x[0] != x[1]):
    #     answer.append(x[0])
    # elif (x[0] == x[1]) :
    #     answer.append(x[2])
    # if (y[0] != y[1]) :
    #     answer.append(y[0])
    # elif(y[0] == y[1]):
    #     answer.append(y[2])
    # return answer
    answer.append(x[0]^x[1]^x[2])
    answer.append(y[0]^y[1]^y[2]) 
    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))