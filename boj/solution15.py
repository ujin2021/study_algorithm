# 1283 단축키 지정 [구현]
n = int(input())
key = []
result = []

for _ in range(n) :
    command = input()

    # 단어의 첫글자가 key에 있는지 확인
    words = command.split()
    l = len(words)
    check = False
    for i in range(l) : 
        if(words[i][0].lower() not in key) :
            key.append(words[i][0].lower())
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            result.append(' '.join(words))
            check = True # key 표시 완료
            break
    if(check) : # 단어의 첫글자가 key라면 다음 입력을 받는다
        continue

    # 글자 하나하나씩 확인
    check = False
    l = len(command)
    for i in range(l) :
        if(command[i] == ' ') : # 띄어쓰기는 건너뛴다
            continue
        if(command[i].lower() not in key) :
            key.append(command[i].lower())
            command = command[:i] + '[' + command[i] + ']' + command[i+1:]
            result.append(command)
            check = True 
            break
    if(check) :
        continue

    result.append(command) # 아무것도 key에 해당하지 않을 땐 그냥 append

print('\n'.join(result))