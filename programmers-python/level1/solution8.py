# 문자열 내마음대로 정렬하기
def solution(strings, n):
    return sorted(sorted(strings), key = lambda x : x[n])
print(solution(['abce', 'abcd', 'cdx'], 1))
# sorted에서의 key function(lambda) 다시공부