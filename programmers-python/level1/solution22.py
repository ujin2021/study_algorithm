# 핸드폰 번호 가리기
def solution(phone_number):
    return '*' * len(phone_number[0:-4]) + phone_number[-4:]

print(solution("01033334444"))
print(solution("027778888"))