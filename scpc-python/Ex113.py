'''
포함되는 1의 개수를 Population count, 줄여서 popcount라고 부른다. 
자연수 N이 주어졌을 때, N의 popcount를 구하는 프로그램을 작성하시오. 
예를 들어, 13을 이진수로 나타내면 1101이 되며, 13의 popcount는 3
'''
import sys

inf = sys.stdin 

def popcount(num):
    Answer = 0
    toBin = bin(num)
    for i in range(0, len(toBin)):
        if (toBin[i] == '1'):
            Answer += 1
    return Answer

T = inf.readline() # testcase
for t in range(0, int(T)):
    num = int(inf.readline().strip())
    Answer = popcount(num)
    print('Case #%d' %(int(t)+1))    
    print(Answer)
inf.close()