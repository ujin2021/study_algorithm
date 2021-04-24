# [재귀] 11729 하노이의 탑 이동순서
print_msg = '{} {}'
def hanoi(n, start, via, end) :
    if(n == 1) :
        print(f'{start} {end}')
    else :
        hanoi(n - 1, start, end, via)
        print(f'{start} {end}')
        hanoi(n - 1, via, start, end)

n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 2, 3)