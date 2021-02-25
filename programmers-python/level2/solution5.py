# 전화번호 목록
# 내 풀이
def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort() # 길이가 짧은게 뒤에있을 수도 있으니 sort를 해주어야 한다.
    for i in range(n - 1) :
        a = phone_book[i]
        for j in range(i + 1, n) :
            b = phone_book[j]
            if (a in b and len(a) <= len(b)) :
                if (a == b[:len(a)]) :
                    return False
    return answer

# hash를 이용한 풀이
def solution_using_hash(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    print('hash_map : ', hash_map)
    for phone_number in phone_book: # phone_book의 number하나하나를 temp에 붙여가면서
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number: # hashmap에 있지만 phone_number과 다르면 접두사라는 뜻
                return False
    return answer

print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))
print()
print(solution_using_hash(['119', '97674223', '1195524421']))
print(solution_using_hash(['123','456','789']))
print(solution_using_hash(['12','123','1235','567','88']))