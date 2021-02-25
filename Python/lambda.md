# 한 줄 함수 lambda

- lambda는 lambda arguments: statement 로 정의된다.

- 예시
```py
add = lambda a, b : a+b # 한 줄로 작성
# a, b -> 매개변수, a+B -> 명령문장, add -> 람다 함수이름
print(add(2,3)) # 람다 함수 add를 일반 함수처럼 호출!
```

- lambda와 연관된 세가지 함수 (map, filter, reduce)
    1.  map과 함께 사용
        - ```map(function, sequence)```형식으로 sequence의 각 원소에 function을 적용. 그 결과를 sequence 형식으로 반환!
        ```py
        >>> b = list(map(lambda x: x*x, [3, 6, 4]))
        >>> print(b)
        [9, 36, 16]
        ```

    2. filter과 함께 사용
        - ```filter(func, sequence)```형식으로 func함수는 True/False를 리턴하고, sequence에 있는 원소 중 func의 값이 True인 원소만 모아 sequence로 만들어 리턴!
        ```py
        >>> a = [1, 3, 5, 6, 7, 10]
        >>> b = list(filter(lambda x: x%2 == 0, a)) 
        >>> b
        [6, 10]
        ``` 

    3. reduce와 함께 사용
        - ```reduce(function, iterable, initializer=None)```형식
        - reduce함수는 여러 개의 데이터를 대상으로 누적 집계를 내기 위해 사용!
        - 기본적으로 초기값을 기준으로 데이터를 루푸 돌면서 집계 함수를 계속해서 적용하며 데이터를 누적하는 방식
        ```py
        >>> from functools import reduce 
        >>> print(reduce(lambda x, y: x+y, [1, 4, 2]))
        7
        >>> print(reduce(lambda x, y: x if x > y else y, [1, 4, 2]))
        ```