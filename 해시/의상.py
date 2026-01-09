def solution(clothes):
    answer = 1
    kind = {}
    for cloth in clothes:
        kind[cloth[1]] = kind.get(cloth[1],0)+1
        
    for i in kind:
        answer *= (kind[i]+1)
        
    answer -=1
    return answer
