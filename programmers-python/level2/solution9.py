# level2 조이스틱

# pad : 65
# end : 91
def solution(name):
    answer = 0
    n = len(name)
    for i in range(n) :
        c = name[i]
        if (c == 'A') :
            if(i <= n // 2 and i+1 >= n // 2) :
                answer -= 1
            else :
                pass
        if (ord(c) - 65 > 91 - ord(c)) :
            answer += 91 - ord(c)
        else :
            answer += ord(c) - 65
    return answer + len(name) - 1

print(solution('JEROEN')) # 56
print(solution('JAN')) # 23
print(solution('JAZ')) # 11
print(solution('AAA'))
print(solution('ZZZ')) 