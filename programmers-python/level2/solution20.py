# 2021 KAKAO BLIND RECRUITMENT - 순위 검색
# 정확도 100, 효율성 0
def solution(info, query):
    answer = []
    db = {'cpp' : set(), 'java' : set(), 'python' : set(), 'backend' : set(), 'frontend' : set(), 'junior' : set(), 'senior' : set(), 'chicken' : set(), 'pizza' : set()}
    score = dict()
    inter = set()
    for i in range(len(info)) :
        inter.add(i)
        tmp = info[i].split()
        score[i] = int(tmp[-1])
        tmp = tmp[:-1]
        for k in tmp :
            db[k].add(i)

    for i in range(len(query)) :
        tmp = query[i].split()
        score_limit = int(tmp[-1])
        tmp = tmp[:-1]
        inter_set = inter.copy()
        count = 0
        for k in tmp :
            if(k == '-' or k == 'and') :
                continue
            inter_set = db[k].intersection(inter_set)
            if(len(inter_set) == 0) :
                break
        
        for i in list(inter_set) :
            if(score[i] >= score_limit) :
                count += 1

        answer.append(count)
    return answer

    

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query) == [1,1,1,1,2,4])

# cpp, java, python (0, 1, 2)
# backend, frontend (0, 1)
# junior, senior (0, 1)
# chicken, pizza (0, 1)

# info : 개발언어 직군 경력 소울푸드 점수
