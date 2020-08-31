# 자릿수 더하기
def solution(n):
    return sum(int(x) for x in str(n))

print(solution(123))