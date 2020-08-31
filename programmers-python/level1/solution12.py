# 모의고사
def solution(answers):
    score = {'0' : 0, '1' : 0, '2' : 0}
    pattern = {'0' : '12345', '1' : '21232425', '2' : '3311224455'}
    for i in range(3) :
        answer = (str(pattern[str(i)]) * len(answers))[0:len(answers)]
        for j in range(len(answer)) :
            if (int(answer[j]) == answers[j]) :
                score[str(i)] = score[str(i)] + 1

    max_score = max(score.values())
    return [int(x)+1 for x in score.keys() if score[x] == max_score]

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))

''' 다른사람 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''