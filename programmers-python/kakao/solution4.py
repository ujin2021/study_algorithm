# 2018 KAKAO BLIND RECRUITMENT 캐시
# hit = 1, miss = 5
# cache size가 0일때 고려
# list에서 값 지울때 인덱스 구해서 하지말고 remove사용하자

def solution(cacheSize, cities):
    time = 0
    cache = []
    if(cacheSize == 0) : # 0일때 생각해주기!!
        return len(cities) * 5
    for i in cities :
        i = i.lower()
        if(i in cache) : # hit
            # print('hit')
            time += 1
            # hit_idx = cache.index(i)
            # cache = cache[:hit_idx] + cache[hit_idx+1:] + [i]
            cache.remove(i) # 그냥 remove를 써주자!
            cache += [i]
        else : # miss
            # print('miss')
            time += 5
            if(len(cache) < cacheSize) :
                cache += [i]
            else :
                cache = cache[1:] + [i]
        print(f'cache : {cache}')
    return time

print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo','Seoul', 'Jeju', 'Pangyo', 'Seoul']))
print(solution(2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(0, ['a', 'a', 'a', 'b']))
