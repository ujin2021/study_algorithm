# 2018 KAKAO BLIND RECRUITMENT 뉴스 클러스터링
# 자카드 유사도
def makeSet(s) :
    tmp_list = []
    for i in range(len(s) - 1) :
        tmp = s[i:i+2]
        if(tmp.isalpha()) :
            tmp_list.append(tmp)
    return tmp_list

def solution(str1, str2):
    str1_list = makeSet(str1.lower())
    str2_list = makeSet(str2.lower())

    str1_set = set(str1_list)
    str2_set = set(str2_list)
    union = list(str1_set | str2_set)
    inter = list(str1_set & str2_set)

    union_score = 0 # 합집합(max)
    inter_score = 0 # 교집합(min)

    for i in union :
        union_score += max(str1_list.count(i), str2_list.count(i))

    for i in inter :
        inter_score += min(str1_list.count(i), str2_list.count(i))

    if(union_score == 0) :
        return 65536

    similarity = inter_score / union_score
    return int(similarity * 65536)
    
    
