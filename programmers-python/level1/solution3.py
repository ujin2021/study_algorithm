# 같은숫자는 싫어
def solution(arr):
    answer = []
    i = 0
    while (i < len(arr) - 1):
        if (arr[i] != arr[i+1]) :
            answer.append(arr[i])
        i = i + 1
    answer.append(arr[-1])
    return answer