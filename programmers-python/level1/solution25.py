# 행렬의 덧셈
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)) :
        tmp = []
        for j in range(len(arr1[i])) :
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer
    
    '''
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
    return answer

    https://itinerant.tistory.com/2
    zip 공부
    '''

print(solution([[1,2,3], [2,3,5], [3,4,2]], [[3,4,5], [5,6,4], [6,7,4]]))