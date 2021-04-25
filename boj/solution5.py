# 1992 쿼드트리

def quadTree(video, n) :
    result = []
    test = set(sum(video, []))
    if(len(test) == 1) :
        return video[0][0]
    result.append(quadTree([video[x][:n//2] for x in range(0, n // 2)], n // 2))
    result.append(quadTree([video[x][n//2:] for x in range(0, n // 2)], n // 2))
    result.append(quadTree([video[x][:n//2] for x in range(n // 2, n)], n // 2))
    result.append(quadTree([video[x][n//2:] for x in range(n // 2, n)], n // 2))
    return '(' + ''.join(result) + ')'

n = int(input())
video = []
for _ in range(n) :
    video.append(list(tuple(input())))
result = quadTree(video, n)
print(result)