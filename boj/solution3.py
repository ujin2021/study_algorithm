# [재귀] 6603 로또
# 조합(nC6을 재귀함수로 구현) 출처 : https://deftkang.tistory.com/179

def solution(n, arr): 
    picked = [] 
    start = 0 
    def recur(start, n): 
        if len(picked) == 6: 
            for i in picked :
                print(arr[i], end = ' ')
            print()
            # print(' '.join(picked))
            return 
        for i in range(start, n): 
            picked.append(i) # 재귀하면서 나머지 원소 선택 
            start = picked[-1] + 1 
            recur(start, n) 
            picked.pop() 
    recur(start, n)
    print()

while(True) :
    input_list = list(map(int, input().split()))
    n = input_list.pop(0)
    if(n == 0) :
        break
    num_list = sorted(input_list)
    solution(n, num_list)