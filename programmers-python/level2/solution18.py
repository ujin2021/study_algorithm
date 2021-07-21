# 메뉴리뉴얼
# https://computer-choco.tistory.com/80 (python list)
# https://jinisbonusbook.tistory.com/50

from itertools import combinations

# 만들고자 하는 course의 menu수로 조합을 만든다
def makeCourse(menu, n) :
    l = len(menu)
    result = []
    for i in range(l) :
        result += list(combinations(tuple(sorted(menu[i])), n))
    return result

# 해당 조합이 order에 2개 이상 존재하는지 count한다
def countMenu(menu) :
    o = list(set(menu))
    result = []
    l = len(o)
    for i in range(l) :
        if(menu.count(o[i]) == 1) :
            continue
        result.append((o[i], menu.count(o[i])))
    
    return sorted(result, key= lambda x : x[1], reverse=True)

# 2개 이상 존재하는 조합 중 가장 많이 나온 메뉴조합을 고른다
def findMax(menu) :
    result = []
    m = menu[0][1]
    for i in menu : 
        if(i[1] == m) :
            result.append(''.join(i[0]))
        elif(i[1] < m) :
            break
    return result

def solution(orders, course):
    answer = []
    for i in course :
        course_comb = makeCourse(orders[:], i)
        if(len(course_comb) <= 1) : # 조합을 구했는데 1개 : 최소 2개는 있어야 메뉴로 선정하므로 넘어간다
            continue
        
        count_result = countMenu(course_comb)
        if(len(count_result) == 0) : # 만약 조합의 count가 1이 넘지 않으면
            continue
        answer += findMax(count_result)
    
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]) == ["WX", "XY"])
