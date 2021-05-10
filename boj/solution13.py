# boj 1120 문자열

a, b = input().split()
n_a = len(a)
n_b = len(b)
n = n_b - n_a
result = n_b # 이문제에서 차이의 최대값이 n_b
for i in range(n + 1) :
    tmp = b[i : i + n_a] # b를 a길이만큼 잘라서 비교(어차피 a 앞뒤에는 b와 같은 알파벳을 붙일거기 때문에)
    tmp_result = 0
    for j in range(n_a) :
        if(tmp[j] != a[j]) :
            tmp_result += 1
    result = min(tmp_result, result)

print(result)