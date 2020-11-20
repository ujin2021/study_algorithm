# 2020 KAKAO BLIND RECRUITMENT 
# 가사검색
# 정확성은 모두통과, 효율성을 통과하려면 이중for문 x , Trie 구조 사용할 것(접두사, 접미사 두개가 포인트!)

def solution(words, queries):
    answer = []
    for query in queries :
        match = 0
        start = True
        leng = len(query)
        if(query[-1] == '?') :
            idx = query.index('?')
            query = query[:idx]
        else :
            query = query[::-1] # str reverse
            idx = query.index('?') * -1
            query = query[::-1]
            query = query[idx:]
            start = False

        for word in words :
            if(len(word) == leng) :
                if(start and query == word[:idx] or (start == False and query == word[idx:])) :
                    match += 1

        answer.append(match)

    return answer
    
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
