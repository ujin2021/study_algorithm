# 메뉴리뉴얼 - 다른사람 풀이 (counter 사용)

import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)
        print('order_combination : ', order_combinations)

        most_ordered = collections.Counter(order_combinations).most_common()
        print('Counter(order_combinations) : ', collections.Counter(order_combinations)) # ('A', 'C') : 4 이렇게 dict형태로
        print('most_ordered : ', most_ordered) # (('A', 'C'), 4) tuple로 묶어줌
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]] # count수가 제일큰게 1일수도 있으니까 v > 1도 넣어준다

    return [ ''.join(v) for v in sorted(result) ]

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"])
print()
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"])
print()
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]) == ["WX", "XY"])