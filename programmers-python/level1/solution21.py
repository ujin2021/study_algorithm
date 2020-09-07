# 하샤드 수
def solution(x):
    return (0 == x % sum(int(x) for x in str(x)))

print(solution(10))
print(solution(11))