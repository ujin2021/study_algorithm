def solution(arr, divisor):
    answer = sorted(list(filter(lambda x: (x % divisor == 0), arr)))
    # if len(answer) > 0 :
    #     return answer
    # else :
    #     return [-1]
    return answer or [-1]

# lambda, list 표현식 공부