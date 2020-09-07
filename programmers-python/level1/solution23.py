# 콜라츠 추측 (1일때도 처리해줘야 했다.)
def solution(num):
    answer = 0
    if(num == 1) :
        return 0
    for i in range(500) :
        if(num % 2 == 0) :
            num /= 2
        else: 
            num = num * 3 + 1

        if(num == 1) :
            return i+1 # i는 0부터 시작하니까
    return -1

print(solution(6))
print(solution(16))
print(solution(626331))
