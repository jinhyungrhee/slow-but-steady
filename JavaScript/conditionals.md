## 조건문

- prompt()
    - 사용자에게 창을 띄울 수 있게 해줌
        - argument1 : message(string)
        - argument2 : default(string)
    - 아주 오래된 방법이라 잘 사용하지 않음
    - css 적용 안 됨
    ```js
    const age = prompt("How old are you?"); // 입력 값이 들어올 때까지 잠시 멈춤(pause)

    console.log(age);
    ```

> type 확인하는 방법

- `typeof` 키워드 사용
    - typeof 변수명

    ```js
    const age = prompt("How old are you?");

    console.log(typeof age); 
    ```

> type을 변경하는 방법

- parseInt()
    - string을 number로 변환하는 함수
    - 입력받은 숫자를 비교할 때 사용

    ```js
    parseInt("15"); // 정수 15로 변환
    ```

    - 입력 값이 숫자가 아닌 경우에 판별 가능
        - 일반적인 문자열을 parseInt()할 경우 `NaN`(Not a Number)리턴
        - parseInt()는 "123"같은 string만 처리가능, "lalala"와 같은 string은 처리 불가(=> `NaN`)
    ```js
    const age = parseInt(prompt("How old are you?"));

    console.log(age);
    ```  
    

> 무언가가 NaN인지 판별하는 방법
- isNaN()
    - true/false 리턴
        - NaN이면, 즉 숫자가 아니면 true리턴
        - NaN이 아니면, 즉 숫자면 false리턴
    ```js
    const age = parseInt(prompt("How old are you?"));

    console.log(isNaN(age));
    ```

> 조건문

- condition은 boolean이어야 함

```js
if(condition) {
    // condition === true
} else {
    // conditino === false
}

// 또는 (동일)

if(condition) {
    // condition === true
} 

```

- 예제
```js
const age = parseInt(prompt("How old are you?"));

if(isNaN(age)){
    console.log("Please write a number");
} else {
    console.log("Thank you for writing your age.");
}

```

- 다중조건
```js
const age = parseInt(prompt("How old are you?"));

if(isNaN(age)){
    console.log("Please write a number.");
} else if(age < 18) {
    console.log("You are too young.");
} else {
    console.log("You can dring.");
}
```

- and 연산자(&&)
    - true && true => true
    - true && false => false
    - false && true => false
    - false && false => false

- or 연산자(||)
    - true || true => true
    - true || false => true
    - false || true => true
    - false || false => false

```js
const age = parseInt(prompt("How old are you?"));

if(isNaN(age) || age < 0){
    console.log("Please write a real positive number.");
} else if(age < 18) {
    console.log("You are too young.");
} else if(age >= 18 && age <= 50) {
    console.log(" You can drink.")
} else if(age > 50 && age <= 80) {
    console.log("You should exercise.");
} else if(age > 80) {
    console.log("You can do whatever you want.");
}
```

- equal 연산자(===)
    - '같다' 의미
    - `=`는 대입 연산자
    - not equal 연산자는 `!==` : '다르다' 의미

    ```js
    const age = parseInt(prompt("How old are you?"));
    // 실행 순서 고려하는 것 중요!
    if(isNaN(age) || age < 0){
        console.log("Please write a real positive number.");
    } else if(age < 18) {
        console.log("You are too young.");
    } else if(age >= 18 && age <= 50) {
        console.log(" You can drink.")
    } else if(age > 50 && age <= 80) {
        console.log("You should exercise.");
    }else if(age === 100) {
        console.log("Wow you are wise");
    }else if(age > 80) {
        console.log("You can do whatever you want.");
    } 
    ```

> 복잡한 조건문

```js
if((a && b) || (c && d) || (x || y)) {

}
```

- 실행 순서 : 뒤에서 부터 true/false return
    1. (x || y) => true/false
    2. (c && d) => true/false
    3. (a && b) => true/false