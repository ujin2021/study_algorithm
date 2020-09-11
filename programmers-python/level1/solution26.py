# 소수찾기 - 에라토스테네스의 체
def solution(n):
    is_prime = [True] * (n+1) # n도 포함시켜야 하므로

    m = int(n ** 0.5)

    for i in range(2, m + 1) :
        if(is_prime[i]) :
            for j in range(2*i, n + 1, i) :
                is_prime[j] = False
    
    prime = [i for i in range(2, n + 1) if is_prime[i] == True]
    return len(prime)

print(solution(10))
print(solution(5))