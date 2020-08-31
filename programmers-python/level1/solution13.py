# 완주 못한 사람
def solution(participant, completion):
    if (set(participant) == set(completion)) :
        for i in completion : 
            if(participant.count(i) != completion.count(i)):
                return i
    else : 
        return list(set(participant) - set(completion))[0]

print(solution(['leo', 'kiki', 'eden', 'leo'], ['eden', 'kiki', 'leo']))