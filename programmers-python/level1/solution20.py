# 정수 내림차순으로 배치하기
def solution(n):
    return int(''.join(sorted((x for x in str(n)), reverse=True)))

print(solution(118372))