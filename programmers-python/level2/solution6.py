# 위장
def solution(clothes):
    answer = 1
    clothes_dic = {}
    for i in clothes :
        if(i[1] in clothes_dic.keys()) :
            clothes_dic[i[1]] += 1
        else :
            clothes_dic[i[1]] = 1

    for i in clothes_dic.values() :
        answer *= (i + 1)
    return answer - 1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))