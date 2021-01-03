# 2019 KAKAO BLIND RECRUITMENT
# 오픈채팅방

def solution(record):
    uid_nickname = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    answer = []
    result = []
    for i in record :
        split_i = i.split(' ')
        first = split_i[0]
        uid = split_i[1]
        if(first == 'Leave') :
            answer += (uid, first)
        else :
            nickname = split_i[2]
            uid_nickname[uid] = nickname
            if(first == 'Enter') :
                answer += (uid, first)
    i = 0
    while(i < len(answer)) :
        uid = answer[i]
        first = answer[i + 1]
        tmp = uid_nickname[uid] + uid_nickname[first]
        result.append(tmp)
        i += 2
    return result
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
