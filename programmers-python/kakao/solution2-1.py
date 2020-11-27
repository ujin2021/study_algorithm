'''
https://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
방금그곡
'''
# c#과 같이 #이 붙은 것들을 소문자로 대체하여 풀어보기 -> 완료
def removeS(s) :
    # print('C#CDC#'.replace('C#', 'c')) 바로 이런식으로 해도 변형됨
    new_s = ''
    for i in range(len(s)-1) :
        if(s[i+1] == '#') :
            new_s += s[i].lower()
        elif(s[i] == '#') :
            continue
        else :
            new_s += s[i]
    if(s[-1] != '#') :
        new_s += s[-1]
    return new_s

def solution(m, musicinfos):
    title = []
    new_m = removeS(m)
    print('new m : ', new_m)
    for i in range(len(musicinfos)) :
        info = musicinfos[i].split(',')
        start = info[0]
        end = info[1]
        lylics = removeS(info[3])
        time = (int(end[0:2]) * 60 + int(end[3:])) - (int(start[0:2]) * 60 + int(start[3:]))
        long_lylics = lylics * (time // len(lylics)) + lylics[:(time % len(lylics))]
        print(f'lylics, time, long_ylics, leng: {lylics}, {time}, {long_lylics}, {len(long_lylics)}')
        if(new_m in long_lylics) :
            title.append([i, time, info[2]])
    if(len(title) == 0) :
        return '(None)'
    elif(len(title) == 1) :
        return title[0][2]
    else :
        title = sorted(title, key = lambda x: x[1], reverse=True)
        max_time = title[0][1]
        i = 0
        for i in range(len(title)) :
            if(title[i][1] == max_time) :
                pass
            else :
                title = title[:i]
                break
        if(len(title) == 1) :
            return title[0][2]
        title = sorted(title, key = lambda x : x[0])
        return title[0][2]

print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))
print(solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))


