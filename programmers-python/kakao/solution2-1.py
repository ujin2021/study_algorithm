'''
https://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
방금그곡
'''
# c#과 같이 #이 붙은 것들을 소문자로 대체하여 풀어보기

def solution(m, musicinfos):
    title = []
    for i in range(len(musicinfos)) :
        info = musicinfos[i].split(',')
        start = info[0]
        end = info[1]
        lylics = info[3]
        time = (int(end[0:2]) * 60 + int(end[3:])) - (int(start[0:2]) * 60 + int(start[3:]))
        nlylics = (lylics * time)[:time+lylics.count('#')]
        # print(f'start, end, lylics, time, leng, nlylics : {start}, {end}, {lylics}, {time}, {len(nlylics)-lylics.count("#")}, {nlylics}')
        if(m in nlylics) :
            idx = nlylics.index(m) + len(m)
            # print('idx : ', nlylics[idx])
            if(nlylics[idx] != '#') :
                title.append([-i, time, info[2]])
    if(len(title) == 0) :
        return None
    elif(len(title) == 1) :
        return(title[0][2])
    else :
        title = sorted(title, key = lambda x: (x[1], x[0]), reverse=True)
        return(title[0][2])

print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))
print(solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))
