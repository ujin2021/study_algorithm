# 2019 카카오 개발자 겨울 인턴십 - 튜플

def solution(s):
  answer = []
  ss = sorted(s[2:-2].split("},{"), key = lambda x : len(x))
  for i in range(len(ss)) :
    ss[i] = set(ss[i].split(","))
    if(len(ss[i]) == 1) :
      answer.append(list(ss[i])[0])
      continue
    answer.append(list(ss[i] - ss[i - 1])[0])

  return list(map(int, answer))