# 20436 ZOAC3 [구현]

key_l = {'q' : (0, 0), 'w' : (0, 1), 'e' : (0, 2), 'r' : (0, 3), 't' : (0, 4), 
    'a' : (1, 0), 's' : (1, 1), 'd' : (1, 2), 'f' : (1, 3), 'g' : (1, 4), 
    'z' : (2, 0), 'x' : (2, 1), 'c' : (2, 2), 'v' : (2, 3)}
key_r = {'y' : (0, 5), 'u' : (0, 6), 'i' : (0, 7), 'o' : (0, 8), 'p' : (0, 9), 
    'h' : (1, 5), 'j' : (1, 6), 'k' : (1, 7), 'l' : (1, 8), 
    'b' : (2, 4), 'n' : (2, 5), 'm' : (2, 6)}

def dist(a, b) :
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

sl, sr = input().split()
s = input()

result = 0
left, right = key_l[sl], key_r[sr]
for _ in s :
    if(_ in key_l) :
        result += dist(left, key_l[_])
        left = key_l[_]
    elif(_ in key_r) :
        result += dist(right, key_r[_])
        right = key_r[_]
    result += 1
print(result)