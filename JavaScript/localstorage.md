## Local Storage

- local storage에는 단순한 형태의 string으로만 저장이 가능함
    - 예) array를 만들어 저장을 해도 실제 array가 아닌 string으로 변경해 저장해야 함
    - **JSON.stringify()** 사용
    ```js
    const todos = ["a", "b", "c"];

    localStorage.setItem("todos", JSON.stringify(todos));
    ```

- 이를 저장된 상태 그대로 그냥 불러오면 단순 string 형태로 리턴됨

```js
localStorage.getItem("todos");
>> "[\"a\",\"b\",\"c\"]"
```

- 단순 string 형태가 아닌 실제 array 형태로 리턴하고 싶다면 **JSON.parse()** 사용

```js
JSON.parse(localStorage.getItem("todos"))
>> (3) ["a", "b", "c"]
```

- **forEach()** : array에 있는 각각의 item에 대해서 function 실행 가능 
- submit eventListener가 event(argument)를 기본적으로 제공해주는 것처럼 JS는 지금 처리되고 있는 **item** 또한 기본적으로 제공해줌!

```js
function sayHello(item) {
    console.log("this is the turn of", item);
}

const savedTodos = localStorage.getItem(TODOS_KEY);

if (savedTodos !== null) {
    const parsedTodos = JSON.parse(savedTodos);
    parsedTodos.forEach(sayHello);
}
```

- 이를 더 간단하게 표현하는 방법 : **arrow function(=>)**

    - function 정의할 필요X
    - 함수 이름 명시할 필요X
```js
const savedTodos = localStorage.getItem(TODOS_KEY);

if (savedTodos !== null) {
    const parsedTodos = JSON.parse(savedTodos);
    parsedTodos.forEach((item) => console.log("this is the turn of", item));
}
```

- 문제1 : 새로고침하고 다시 값을 추가할 시 기존 local storage 내용이 사라지고 새로 입력받은 값만 다시 저장됨
    - 이미 존재하는 값들 복원해서 다시 저장해주는 과정 필요

```js
// const 대신 let으로 array가 초기화되는 것 방지
let todos = [];

// 중략

const savedTodos = localStorage.getItem(TODOS_KEY);

if (savedTodos !== null) {
    const parsedTodos = JSON.parse(savedTodos);
    // local storage에 이미 todos가 있으면 todos에 parsedTodos를 넣어서 전에 있던 todos를 "복원"시킴
    todos = parsedTodos;
    parsedTodos.forEach(paintTodo);
}
```

- 문제2 : x표시를 눌러서 삭제하면 화면 상에서만 사라지고 local storage에는 데이터가 남아있음 
    - 주의 : `todos` array가 실질적인 **database**이고 `local storage`는 이 todos array를 **복사해두는 곳**임
    - object로 만들어서 text와 함께 id값을 할당해야 함(각각의 text를 고유하게 식별하기 위해)
    - array에서 특정 값 삭제하기 === 지우고 싶은 item을 빼고 새로운 array를 만드는 것
        - **filter()** 사용
        - filter()는 기존 array의 item을 지우는 것이 아니라 **item을 제외시켜 새로운 array를 만듦**!
```js
// ...
// newTodo는 Object임
function paintTodo(newTodo) {
    
    const li = document.createElement("li");
    // li에 object의 id값 추가
    li.id = newTodo.id;
    const span = document.createElement("span");
    // spand에는 object의 text값 저장
    span.innerText = newTodo.text;
    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", deleteTodo);
    li.appendChild(span);
    li.appendChild(button);
    todoList.appendChild(li);
}
function handleTodoSubmit(event) {
    event.preventDefault();
    const newTodo = todoInput.value;
    todoInput.value = "";
    // todos array(DB)에 text대신 object만들어서 push!
    // 삭제 시 id로 각각의 값 식별 필요!
    const newTodoObject = {
        text:newTodo,
        id : Date.now(),
    }
    todos.push(newTodoObject);
    paintTodo(newTodoObject);
    saveTodos();
}
// delete 기능 구현
function deleteTodo(event) {
    // path에서 클릭 target이 무엇인지 확인 가능! => target은 "클릭된 HTML element(=button)임!"
    // event는 property를 가지는데 어떤 button이 클릭되었는지 알려주지만 이것은 충분하지 않음 
    // parent를 알아야 함 : parentNode / parentElement = "li"
    // parent를 알면 어떤 li를 삭제해야 하는지 알 수 있음!
    // console.dir(event.target.parentElement.innerText); 
    // console.log(event.target.parentElement);
    const li = event.target.parentElement;
    // 이렇게 하면 화면에서 li를 삭제하기 전에 li를 얻을 수 있음!
    console.log(li.id);
    li.remove();
}
```

- filter() 예시
    - array의 item을 유지하고 싶으면 true를 리턴해야 함!
```js
function sexyFilter() {return true}
>> undefined
[1, 2, 3, 4, 5].filter(sexyFilter)
>> (5)[1, 2, 3, 4, 5]

function notSexyFilter() {return false}
>> undefined
[1, 2, 3, 4, 5].filter(notSexyFilter)
>> []

function myFilter(item) {return item !== 3}
>> undefined
[1, 2, 3, 4, t].filter(myfilter)
>> (4)[1, 2, 4, 5]

const arr = ["pizza", "banana", "tomato"]
>> undefined
function sexyFilter(food) {return food !== "banana"}
>> undefined
arr.filter(sexyFilter)
>> (2)["pizza", "potato"]

const arr = [1234, 5454, 223, 122, 45, 6775, 334]
>> undefined
function sexyFilter(num) {return num <= 1000}
>> undefined
arr.filter(sexyFilter)
>> (4)[223, 122, 45, 334]

const toDos = [{text: "a", id: 1628401817786}, {text: "a", id: 1628401818123}, {text: "a", id: 1628401818486}]
>> undefined
function sexyFilter(todo) {return todo.id !== 1628401817786 }
>> undefined
todos.filter(sexyFilter)
>> (2) [{…}, {…}]
    0: {text: "a", id: 1628401818123}
    1: {text: "a", id: 1628401818486}
    length: 2
    [[Prototype]]: Array(0)]

// filter는 새로운 array를 생성시킴
const arr = [1, 2, 3, 4]
>> undefined
arr.filter(item => item > 2)
>> (2) [3, 4]
const newArr = arr.filter(item => item > 2)
>> undefined
arr
>> (4) [1, 2, 3, 4] // 기존 arr은 바뀌지 않음
newArr
>> (2) [3, 4] // newArr은 arr.filter()가 전달해 준 값임
```
