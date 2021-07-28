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
        console.log(a + b)
    },
    minue : function(a, b) {
        console.log(a - b)
    },
    multiple : function(a, b) {
        console.log(a * b)
    },
    divide : function(a, b) {
        console.log(a / b)
    }
};


calculator.plus(1, 3);
calculator.minus(1, 3);
calculator.multiple(1, 3);
calculator.divide(1, 3);
```