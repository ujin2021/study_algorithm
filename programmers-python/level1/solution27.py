# level1 체육복

def solution(n, lost, reserve):
    count = 0
    # 자기것을 잃어버렸을 땐 먼저 자기가 여벌의 옷을 가져야 한다
    uni = set(lost) & set(reserve)
    lost = list(set(lost) - uni)
    reserve = list(set(reserve) - uni)
    
    for i in lost :
        if (i-1 in reserve) :
            reserve.remove(i-1)
        elif (i+1 in reserve) :
            reserve.remove(i+1)
        else :
            count += 1
    return n - count

print(solution(5, [1, 2, 3], [2, 3, 4]))
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
