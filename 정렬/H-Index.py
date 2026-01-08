def solution(citations):
    answer = 0
    temp = []
    for i in range(len(citations)+1):
        num = 0
        for j in citations:
            if j>=i:
                num +=1
        if num >= i:
            temp.append(i)
    temp.sort(reverse = True)
    answer = temp[0]
    return answer
