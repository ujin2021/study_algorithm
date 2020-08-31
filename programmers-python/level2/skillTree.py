def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees :
        tmp = ''.join(list(x for x in i if x in skill)) # skill 에 해당하는 것만 빼와서 string으로 만들기
        
        if(tmp == skill[0:len(tmp)]) :
                answer = answer + 1
        
    return answer