# 영어끝말잇기

def solution(n, words):
  done = [words[0][0]]
  r = 0 # round
  while True:
    r += 1
    if(len(done) - 1 == len(words)) :
      break
    for j in range(n) :
      word = words[(r - 1) * n + j]
      if(word in done or done[-1][-1] != word[0]) : # 이미 했던 단어일 때
        return [j + 1,r]
      done.append(word)   
  return [0,0]

print(solution(3, 	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))