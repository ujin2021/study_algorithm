# 자연수 뒤집어 배열로 만들기
def solution(n) :
    return [int(x) for x in reversed(str(n))]

print(solution(13245))