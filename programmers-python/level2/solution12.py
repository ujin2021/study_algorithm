# level2 멀쩡한 사각형 - 내풀이
import math
def solution(w,h):
    answer = 0
    if (w == h) : # 정사각형 일 때
        return w * h - w

    if (w > h) :
        w, h = h, w # w 만큼 for문을 도니까 작은수를 w로 넣어주는게 낫다
    g = math.gcd(w, h)
    if(g == 1) :
        s = h / w
        for i in range(1, w) :
            answer += int(s * i) # python에서 double 함수가 누적되면 오차가 발생한다고 한다(테스트6 실패 이유)
        return answer * 2
    else : # 최대공약수가 1보다 크면 최대공약수 만큼 똑같은 패턴이 반복된다
        t = w * h
        tmp = 0
        w, h = w // g, h // g
        s = h / w
        for i in range(1, w) :
            tmp += int(s * i)
        return t - (w * h - tmp * 2) * g

print(solution(3, 5))
print(solution(8, 12))
print(solution(1, 4))