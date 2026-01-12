#정렬기반 풀이 / 문자열 정렬하여 이웃한 문자(=접두어 유사가능성 존재)만 확인
def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        b = phone_book[i+1][:len(a)]
        if (b == a): 
            return False
    return True
  
#해시기반 풀이 /앞에서부터 쪼개서 해당 문자가 hash 안에 있는지 확인
def solution(phone_book):

    phone_hash = set(phone_book)    #시간복잡도 고려하기 위해

    for i in phone_book:
        temp = ""
        for j in i[:-1]:
            temp += j
            if temp in phone_hash:
                return False
    return True
