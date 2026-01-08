## 정렬(sort)

1. sort
2. sort(reverse=True/False)
3. sorted >새 리스트 생성
4. sort(key)
    1. key = a[i]
    2. key=lambda x: x[1]
    3. key=lambda x: (-x[1], x[0])

## 풀이
1. [K번째 수](https://github.com/k-hanna12/programmars/blob/main/%EC%A0%95%EB%A0%AC/K%EB%B2%88%EC%A7%B8%20%EC%88%98.py) :star:
2. [가장 큰수](https://github.com/k-hanna12/programmars/blob/main/%EC%A0%95%EB%A0%AC/%EA%B0%80%EC%9E%A5%20%ED%81%B0%20%EC%88%98.py) :star::star::star:
   > 문자열로 변형한 A,B를 A+B와 B+A로 비교하기 위해 lambda x:x*3 수행 ex) 343434 323232 333 444 >>(문자열 비교시) 444 > 343434 > 333 > 323232  결과)434332
3. [H-index](https://github.com/k-hanna12/programmars/blob/main/%EC%A0%95%EB%A0%AC/H-Index.py):star::star::star::star:
   > 이 코드에서 벽을 느껴요.
   ```python 
    def solution(citations):
        citations = sorted(citations)
        l = len(citations)
        for i in range(l):
            if citations[i] >= l-i:
                return l-i
        return 0
   ```
