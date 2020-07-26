'''
구독자 수가 10만명 이상이 되면 실버 버튼을, 100만명 이상이 되면 골드 버튼을, 1,000만명 이상이 되면 다이아몬드 버튼을 선물로 준다. 
어떤 와이튜버의 구독자 수가 주어졌을 때, 마지막으로 받은 플레이버튼의 색을 구하는 프로그램을 작성하시오.

입력 파일에는 여러 테스트 케이스가 포함될 수 있다.
파일의 첫째 줄에 테스트 케이스의 개수를 나타내는 자연수 T 가 주어지고,
이후 차례로  T 개의 테스트 케이스가 주어진다. (1 ≤ T ≤ 50)
각 테스트 케이스의 입력은 다음과 같은 형식이다.
첫 번째 줄에 와이튜버의 구독자 수를 나타내는 자연수가 주어진다. 주어지는 구독자 수는 1억명을 넘지 않는다.

입력
4
1432
192314
3635904
10000009
출력
Case #1
NONE
Case #2
SILVER
Case #3
GOLD
Case #4
DIAMOND
'''
import sys

inf = sys.stdin 
T = inf.readline()

def button(sub):
    top = sub // 100000
    if(top < 1):
        Answer = 'NONE'
    elif(top >= 1 and top < 10):
        Answer = 'SILVER'
    elif(top >= 10 and top < 100):
        Answer = 'GOLD'
    else:
        Answer = 'DIAMOND'
    return Answer

for t in range(0, int(T)):
    sub = int(inf.readline())
    Answer = button(sub)
    print('Case #%d' %(int(t)+1))    
    print(Answer)
inf.close()