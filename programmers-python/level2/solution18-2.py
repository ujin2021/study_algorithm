# 메뉴리뉴얼 - 내 풀이에 counter 적용시켜보기

from itertools import combinations
from collections import Counter

# 만들고자 하는 course의 menu수로 조합을 만든다
def makeCourse(menu, n) :
    l = len(menu)
    result = []
    for i in range(l) :
        result += list(combinations(tuple(sorted(menu[i])), n))
    return result

def solution(orders, course):
    answer = []
    for i in course :
        course_comb = makeCourse(orders[:], i)
        if(len(course_comb) <= 1) : # 조합을 구했는데 1개 : 최소 2개는 있어야 메뉴로 선정하므로 넘어간다
            continue

        most_ordered = Counter(course_comb).most_common()
        # print('most_ordered : ', most_ordered)

        answer += [''.join(k) for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
        
        
        # count_result = countMenu(course_comb)
        # if(len(count_result) == 0) : # 만약 조합의 count가 1이 넘지 않으면
        #     continue
        # answer += findMax(count_result)

    # print('answer : ', answer)
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]) == ["WX", "XY"])
