# boj 1316 그룹 단어 체크

import sys
n = int(input())
words = [sys.stdin.readline().strip() for _ in range(n)]
result = 0
for i in words :
    n = len(i)
    tmp = ' ' # 현재 그룹을 이루는 단어 저장
    check = [] # group을 이룬 단어 저장
    isGroup = True # 이 단어는 그룹단어이다
    for j in range(n) :
        if(tmp[-1] != i[j]) : # 이전 단어와 다르면
            if(i[j] in check) : # 이미 그룹에 속해있는 알파벳이라면
                isGroup = False # 그룹단어가 아니다
                break
            check.append(i[j]) # 그룹을 이루는 알파벳 추가
            tmp = i[j] # 현재 그룹을 이루는 알파벳 저장
    if(isGroup) : # 그룹단어 일 때만
        result += 1
print(result)