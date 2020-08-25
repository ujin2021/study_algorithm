'''
array	                commands	                        return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3] 
'''
def solution(array, commands):
    answer = []
    for com in commands:
        tmp = array[com[0]-1:com[1]]
        answer.append(sorted(tmp)[com[2]-1])
    return answer