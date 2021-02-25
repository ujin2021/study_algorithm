# 베스트 앨범

def solution(genres, plays):
    answer = []
    play = {}
    genre = {}
    n = len(genres)
    for i in range(n) :
        if genres[i] in play :
            play[genres[i]] += plays[i]
            genre[genres[i]] += [[plays[i], i]]
        else :
            play[genres[i]] = plays[i]
            genre[genres[i]] = [[plays[i], i]]
    order = sorted(play.items(), key = lambda x : x[1], reverse=True)
    for i in order :
        tmp = genre[i[0]]
        tmp = sorted(tmp, key = lambda x : (-x[0], x[1]))[:2]
        # answer.append(tmp[0][1])
        # answer.append(tmp[1][1])
        # 위의 처럼 하면 안되는 이유 : 곡이 항상 2개가아닐 수 있다.
        # 한 장르에 포함되는 곡이 하나일 수 있으므로 len(tmp)동안 돌려야함
        for i in range(len(tmp)): 
            if i == 2: 
                break 
            answer.append(tmp[i][1])
    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500]))