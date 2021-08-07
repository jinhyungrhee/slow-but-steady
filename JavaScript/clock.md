## interval

- 매번 무슨 일이 일어나게 하고 싶을 때 사용

- `setInterval(function, millisecond)`

## timeout

- 해당 시간이 지난 뒤 단 한 번만 발생

- `setTimeout(function, millisecond)`

## Date object

- `new Date()` : Wed Aug 04 2021 23:52:02 GMT+0900 (한국 표준시)
    - getHours() : 시 
    - getMinutes() : 분
    - getSeconds() : 초 

## 00으로 0 표시하기

- string을 문자 두 개로 채우기
- `padStart(길이, "패딩할 문자")`
    - string에 사용하는 function
    - 시작부분에 padding을 추가하는 것!

- 예시
```
"1".padStart(2,"0");
>> "01"
```
- 만약 이 string의 길이를 2로 만드는데 그 길이가 2가 아니라면 앞에 "0"을 추가함!

```
"hello".padStart(20, "x");
>> "xxxxxxxxxxxxxxxhello"
```
