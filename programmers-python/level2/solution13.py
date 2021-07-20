# 프로그래머스 카카오 후보키
from itertools import combinations

def solution(relation):
  l = len(relation) # tuple 수
  sl = len(relation[0]) # attribute 수
  attr = [i for i in range(sl)]
  answer = []

  comb = []
  for i in range(sl) :
    comb += list(combinations(attr, i + 1))
  
  for i in comb : # 조합 
    loop = len(i) # 몇개의 조합인가
    check = []
    for j in range(l) : # 한 column씩
      tmp = [] # 한 colum에서 comb로 뽑은걸 저장
      for k in i : # 조합 요소
        tmp.append(relation[j][k])
      check.append(tuple(tmp))
    if(len(set(check)) == l) :
      answer.append(i)
  
  answer = sorted(answer, key=lambda x : len(x))
  result = answer[:]
  for i in range(len(answer)) :
    for j in range(i + 1, len(answer)) :
      if(set(answer[i]).issubset(set(answer[j]))) :
        if(answer[j] in result) :
          result.remove(answer[j])
  return len(result)

input_list = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(input_list))