'''
배드민턴은 21점을 얻으면 승리한다. 
득점한 순서가 주어졌을 때, 게임이 진행중인지, 혹은 게임이 끝나서 Alice혹은 Bob가 승리하였는지 출력하는 프로그램을 작성하시오.

입력
3
ABAAABBAAA
ABBAAAAAAAABAAAAAAAABAABAA
BBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAB
출력
Case #1
Playing
Case #2
Alice
Case #3
Bob
'''
import sys
inf = sys.stdin 

def win(score):
    if(len(score) < 21):
        return 'Playing'
    a, b = 0, 0
    for i in range(0, len(score)):
        if(score[i] == 'A'):
            a += 1
            if(a == 21):
                return "Alice"
        else:
            b += 1
            if(b == 21):
                return "Bob"
    return 'Playing'

T = inf.readline()
for t in range(0, int(T)):
    print('Case #%d' %(int(t)+1))
    score = input()
    Answer = win(score)
    print(Answer)
inf.close()