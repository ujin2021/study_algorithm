# 시저암호
def solution(s, n):
    # 65 ~ 90, 97 ~ 122, 32
    answer = ''
    for i in s : 
        if(i.islower()) :
            answer += chr((ord(i) + n) - 26*((ord(i)+n)//123))
        elif(i.isupper()): 
            answer += chr((ord(i) + n) - 26*((ord(i)+n)//91))
        else :
            answer += i
    return answer

print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))

# https://www.google.com/search?q=python+ascii&source=lmns&bih=722&biw=1536&safe=active&hl=ko&sa=X&ved=2ahUKEwjAr7Ksi8DrAhUVEIgKHbpIB_MQ_AUoAHoECAEQAA