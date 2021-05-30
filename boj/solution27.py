# 11051 이항 계수 2

n, k = map(int, input().split())
def fact(n, k) :
    result = [1, 1, 1] # n, k, n - k
    fact_result = 1
    for i in range(1, n + 1) :
        fact_result *= i
        if(i == n) :
            result[0] = fact_result
        if(i == k) :
            result[1] = fact_result
        if(i == n - k) :
            result[2] = fact_result
    return result
result = fact(n, k)
print(result[0] // (result[1] * result[2]) % 10007)