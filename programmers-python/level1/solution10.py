# 문자열 다루기 기본 - 실패
def solution(s) :
    try :
        if(int(s)) : return True
    except Exception :
        return False
print(solution('a234'))
print(solution('1234'))
print(solution('0000'))
print(solution('00-1'))