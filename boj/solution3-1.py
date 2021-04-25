# [재귀] 6603 로또
# 조합 재귀함수 출처 : https://cotak.tistory.com/70

def gen_combinations(arr, n): 
    result = [] 
    if n == 0: 
        return [[]] 
    for i in range(0, len(arr)):
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        gen_result = gen_combinations(rest_arr, n-1)
        for C in gen_result: 
            result.append([elem]+C) 
    return result

while(True) :
    input_nums = list(map(int, input().split()))
    n = input_nums.pop(0)
    if(n == 0) :
        break
    num_list = sorted(input_nums)
    result = gen_combinations(num_list, 6)
    # print(result)
    for i in result :
        i = list(map(str, i))
        print(' '.join(i))
    print()
