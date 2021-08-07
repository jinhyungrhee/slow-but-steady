## 무작위성

### random number 생성하기

- 0과 어떤 수 사이의 어떤 랜덤한 수를 가져오고 싶을 땐 그냥 그 수를 곱하면 됨!
    - ex) 0 ~ 10사이의 숫자 : `Math.random() * 10(원하는 숫자)`
    - ex) 0 ~ 5 사이의 숫자 : `Math.random() * 5(원하는 숫자)`
        - Math.random() 의 결과가 0에서 1사이이므로 절대 곱한 숫자 이상의 것을 주지 못함, 그것이 최고치 숫자임!

- `Math`모듈 `random()`함수 사용
```js
Math.random()
>> 0.549812449065409

Math.random()
>> 0.5396680537370375

// 10을 곱하면 0에서 10사이의 숫자(float) 얻을 수 있음

Math.random() * 10
>> 0.5396680537370375

Math.random() * 10
>>9.791830591972971
```

- float를 integer로 바꾸는 세 가지 방법

1. round() : 반올림
```js
Math.round(1.3)
>> 1

Math.round(1.5)
>> 2
```

2. ceil() : 올림
```js
Math.ceil(1.1)
>> 2

Math.round(1.01)
>> 2

Math.round(1.0)
>> 1
```

3. floor() : 내림
```js
Math.ceil(1.9)
>> 1

Math.round(1.9999999999)
>> 1
```

- 0에서 10 사이의 정수를 얻기 위해서는 위의 세 가지 방법 중 하나 선택

```js
Math.floor(Math.random() * 10)
>> 3

Math.floor(Math.random() * 10)
>> 5

```