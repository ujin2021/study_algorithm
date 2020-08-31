# 모의고사 - 실패
def solution(answers):
    score = {'0' : 0, '1' : 0, '2' : 0}
    pattern = {'0' : 12345, '1' : 21232425, '2' : 3311224455}
    for i in range(3) :
        answer = (str(pattern[str(i)]) * len(answers))[:len(answers)]
        for ans in range(len(answer)) :
            if answer[ans] == answers[ans] :
                score[str(i)] = score[str(i)] + 1

    for i in range(3) :
        return sorted(score.keys(), key = lambda x : score[str(i)])

print(solution('12345'))