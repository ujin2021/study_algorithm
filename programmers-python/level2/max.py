# #  가장 큰 수 - 참고함

# def solution(numbers):
#     answer = ''
#     for i in range(len(numbers)) :
#         numbers[i] = str(numbers[i])
    
#     numbers = sorted(numbers, key = lambda x : x[0], reverse=True)
#     same = []
#     same_num = numbers[i][0]
#     i = 0
#     for i in range(len(numbers) - 1) :
#         if(same_num != numbers[i+1][0]) :
#             if(len(same) > 0) :
#                 same = sorted(same, key = lambda x : int(x)%10, reverse=True)
#                 answer += ''.join(same)
#                 same = []
#             else :
#                 answer += numbers[i]
#                 if(i == len(numbers) - 2) :
#                     answer += numbers[i+1]
#             same_num = numbers[i+1][0]
#         else :
#             if(len(same) == 0) :
#                 same += [numbers[i], numbers[i+1]]
#             else :
#                 same += [numbers[i+1]]
#                 if(i == len(numbers) - 2) :
#                     same = sorted(same, key = lambda x : int(x)%10, reverse=True)
#                     answer += ''.join(same)
#     if(int(answer) == 0) :
#         return '0'               
#     return answer
# print(solution([6, 10, 2]))
# print(solution([6, 10, 2]) == '6210')
# print(solution([3, 30, 34, 5, 9]))
# print(solution([3, 30, 34, 5, 9]) == '9534330')
# print(solution([3, 30, 34, 5, 56, 9]))
# print(solution([3, 30, 34, 5, 56, 9]) == '956534330')

def solution(numbers) :
    numbers = list(map(str, numbers)) # number의 int들을 str으로 변환
    numbers.sort(key = lambda x:x*4, reverse=True) # 세자리로 맞춰주기위한(number의 숫자들은 1000이하)
    return ''.join(numbers)

print(solution([6, 10, 2]) == '6210')
print(solution([3, 30, 34, 5, 9]))
print(solution([3, 30, 34, 5, 9]) == '9534330') # lambda x:x 하면 3 < 30이므로 330이아닌 30이 나온다
print(solution([3, 30, 34, 5, 56, 9]))
print(solution([3, 30, 34, 5, 56, 9]) == '956534330')

# int 형에서의 크기비교와 str에서의 크기비교가 다름
# str에서는 10 < 9, 99 > 9 (사전식으로)