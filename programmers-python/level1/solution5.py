# 두 정수 사이의 합
def solution(a, b):
    if(a > b):
        a, b = b, a
    return sum(range(a, b+1))
    #return sum(list(x for x in range(a, b+1))) 굳이 리스트로 만들지 않아도 된다... sum의 range만 잡아준다

# return sum(range(min(a,b),max(a,b)+1)) a와 b둘중 어느것이 큰지 if문을 쓰지 않고 min, max함수로 판단