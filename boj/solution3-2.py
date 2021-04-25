# [재귀] 6603 로또
# itertools.combinations를 사용

import itertools
while(True) :
    input_list = list(map(int, input().split()))
    n = input_list.pop(0)
    if(n == 0) :
        break
    result = list(itertools.combinations(sorted(input_list), 6))
    for i in result :
        i = list(map(str, i))
        print(' '.join(i))
    print()