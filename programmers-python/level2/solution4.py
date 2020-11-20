# 주식가격 - 참고함

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)) :
        for j in range(i+1, len(prices)) : 
            answer[i] += 1
            if(prices[i] > prices[j]) :
                break
        
    return answer
# 6번줄 : i == len(prices) - 1일 때 j i+1(==len(prices)) 이므로 for문이 돌지않음
print(solution([1, 2, 3, 2, 3]))
print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])