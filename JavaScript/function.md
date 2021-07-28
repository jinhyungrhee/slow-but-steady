## JS function 기초 사용예제

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