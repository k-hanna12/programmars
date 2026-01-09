## 해시(hash)

1. put()
2. get()
3. getOrDefault() (> java )
  > 해당 key가 없는 상황 고려, 없다면 false 반환 (있다면 헤당 value 반환)
4. set()
## 풀이
1. [완주하지 못한 선수]()
2. [폰켓몬](https://github.com/k-hanna12/programmars/blob/main/%ED%95%B4%EC%8B%9C/%ED%8F%B0%EC%BC%93%EB%AA%AC.py) 
   > set : 중복X, 순서X
   > min : 최소값 반환 
    ```python 
    def solution(ls):
        return min(len(ls)/2, len(set(ls)))
   ```
3. [전화번호 목록](https://github.com/k-hanna12/programmars/blob/main/%ED%95%B4%EC%8B%9C/%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8%EB%AA%A9%EB%A1%9D.py)
   > startswith() 사용으로 접두어 비교 가능
4. [의상](https://github.com/k-hanna12/programmars/blob/main/%ED%95%B4%EC%8B%9C/%EC%9D%98%EC%83%81.py)
