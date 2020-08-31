# 문자열 다루기 기본 - 실패
def solution(s) :
    try :
        if(int(s) > -1 and len(s) == 4 or len(s) == 6) : return True
        else : return False
    except Exception :
        return False

# s.isdigit()
        
print(solution('a234')) # false
print(solution('1234')) # true
print(solution('0000')) # true
print(solution('-1')) # false (숫자로만 이루어져 있어야 하므로)