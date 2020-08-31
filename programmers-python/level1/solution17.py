# 이상한 문자 만들기
def solution(s):
    arr = s.lower().split(' ')
    answer = []
    for word in arr :
        tmp = ''
        for i in range(len(word)) :
            if (i % 2 == 0) :
                tmp += word[i].upper()
            else :
                tmp += word[i]
        answer.append(tmp)
    return ' '.join(answer)
    
print(solution('try hello world'))
# https://wikidocs.net/16045