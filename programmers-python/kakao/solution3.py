# 2018 KAKAO BLIND RECRUITMENT 파일명 (level2)

def splitFile(file) :
    head = ''
    number = ''
    for i in range(len(file)) :
        if(file[i].isdigit() == False) :
            head += file[i]
            continue
        else :
            file = file[i:]
            break
    for i in range(len(file)) :
        if(file[i].isdigit()) :
            number += file[i]
        else :
            break
    # print('head : ', head, 'numb  : ', number)
    return [head.lower(), int(number)]

def solution(files):
    answer = []
    split_file = []
    for i in range(len(files)) :
        file = splitFile(files[i])
        file.insert(0, i)
        split_file.append(file)
    split_file = sorted(split_file, key = lambda x : (x[1], x[2], x[0]))
    idx = [x[0] for x in split_file]
    for i in idx :
        answer.append(files[i])
    return answer

print(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
print(solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))
