# [greedy] 1449 수리공 항승
n, l = map(int, input().split())
holes = sorted(list(map(int, input().split()))) # sorting 해야함!

result = 0
end = 0
for hole in holes :
    if(hole - 0.5 >= end) : # 앞에서 붙인 테이프로 해결 못할 때만
        end = hole - 0.5 + l # 테이프를 붙여준다
        result += 1
print(result)

