## JS function 기초

- function은 어떤 코드를 캡슐화해서 그걸 계속 반복해서 사용하도록 하는 것
- Object 안에서 함수를 정의해서 사용할 수 있음!

```js
const player = {
    name : "nico",
    sayHello: function(otherPersonsName) {
        console.log("hello " + otherPersonsName + " nice to meet you!");
    },
};

player.sayHello("lynn");
player.sayHello("dal");
player.sayHello("dean");
```

- calculator 예제

```js
const calculator = {
    plus : function(a, b) {
        console.log(a + b);
    },
    minus : function(a, b) {
        console.log(a - b);
    },
    multiple : function(a, b) {
        console.log(a * b);
    },
    divide : function(a, b) {
        console.log(a / b);
    }
};


calculator.plus(1, 3);
calculator.minus(1, 3);
calculator.multiple(1, 3);
calculator.divide(1, 3);
```

- console.log 대신 return 사용
```js
const calculator = {
    plus : function(a, b) {
        return a + b;
    },
    minus : function(a, b) {
        return a - b;
    },
    multiple : function(a, b) {
        return a * b;
    },
    divide : function(a, b) {
        return a / b;
    },
    power : function(a, b) {
        return a ** b;
    }
};

//상호의존적으로 작용
const plusResult = calculator.plus(2, 3);
const minusResult = calculator.minus(plusResult, 10);
const multipleResult = calculator.multiple(10, minusResult);
const divideResult = calculator.divide(multipleResult, plusResult);
const powerResult = calculator.power(divideResult, minusResult);

console.log(powerResult);
```
=> `return`을 사용하면 상호의존적인 코드를 작성할 수 있음!

- console.log는 단순히 값을 console에 출력하는 것
    - 변수나 메모리에 저장되지 않음
- return은 함수에서 처리된 결과값을 받아서 저장함
    - 변수에 return 값을 저장하면 다른 곳에 이용하거나 상호의존적으로 사용가능

- return을 하면 function은 작동을 멈추고 결과값을 return한 후 종료됨!
    - return 뒤에 코드를 작성하면 해당 코드는 작동하지 않음!