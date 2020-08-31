# 문자열 내림차순으로 정렬하기
def solution(s):
    return ''.join(sorted(s, reverse=True))

print(solution('Zbcdefg'))