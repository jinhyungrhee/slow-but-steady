## Input

- 사용자로부터 데이터를 전달 받아 화면에 표시

> html

```html
<body>
    <div id="login-form">
        <input type="text" placeholder="what is your name?"/>
        <button>Log In</button>
    </div>
    <script src="app.js"></script>     
</body>
```
> js에서 `input`과 `button` 가져오기

```js
const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form button");
```

> input에 입력한 값(value) 콘솔 로그에 찍어보기

```js
const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form button");

function handleLoginBtnClick() {
    console.log(loginInput.value);
    console.log("click!!");
}


loginButton.addEventListener("click", handleLoginBtnClick);
```

> username 유효성 검사
```js
function handleLoginBtnClick() {
    const username = loginInput.value;
    if(username === "") {
        alert("Please write your name");
    } else if(username.length > 15) {// 15자 넘으면 경고
        alert("Your name is too long.");
    }
}
```

> username 유효성 검사 - HTML 활용하기

- HTML input 태그 자체적으로 제공하는 기능도 있음
    - `required` : 필수 입력
    - `maxlength` : 최대 글자수

    ```html
    <body>
        <form id="login-form">
            <input
            required
            maxlength="15" 
            type="text"
            placeholder="what is your name?"/>
            <button>Log In</button> <!-- <input type="submit" value="Log In"> -->
        </form>
        <script src="app.js"></script>     
    </body>
    ```

- **HTML로 input의 유효성 검사를 작동시키기 위해서는 form 태그 안에 있어야 함!**

- HTML을 이용한 유효성 검사는 form이 submit되어 웹사이트를 재시작시킴!
    1. input 안에 있는 button을 누르거나 
    2. type이 submit인 input을 클릭하면 작성한 form이 submit됨  

- 이러한 HTML input의 기능을 이용하면 더 이상 click을 신경쓸 필요 없이 **form을 submit하는 것에 관심**을 두게 됨!


> form submit시 새로고침 되는 것 막기

- 새로고침은 form submit의 기본 동작임
- onLoginSubmit 함수가 하나의 argument를 받도록 하고 그것은 JS에게 넘겨주어서 처리함
    - `.preventDefault` 사용 : 어떤 event의 기본 행동(ex새로고침)도 발생하지 못하도록 막음
```js
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");

function onLoginSubmit(event) {
    event.preventDefault();
    console.log(loginInput.value);
}

loginForm.addEventListener("submit", onLoginSubmit);
// function() => 브라우저가 ()를 보는 순간 바로 실행
// function 자체를 인자로 주면 => event가 발생했을 때만 실행(브라우저가 봐도 실행x)
```
- 즉 브라우저가 함수를 호출시켜 줄 뿐만 아니라 event에 관한 정보도 담아주는 것임

> a태그에서 링크로 이동하는 것 막기

```html
<body>
    <form id="login-form">
        <input
        required
        maxlength="15" 
        type="text"
        placeholder="what is your name?"/>
        <button>Log In</button>
    </form>
    <a href="https://nomadcoders.co">Go to courses</a>
    <script src="app.js"></script>     
</body>
```

```js
const link = document.querySelector("a");

function handleLinkClick (event) {
    event.preventDefault();
    console.dir(event);
}

link.addEventListener("click", handleLinkClick);
```

> username 제출하면 form 사리지게 하기

- css를 이용하여 숨김
```css
.hidden {
    display: none;
}
```
```js
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");

function onLoginSubmit(event) {
    event.preventDefault(); // 새로고침(기본동작) 막아줌
    const username = loginInput.value;
    loginForm.classList.add("hidden");
    console.log(username);
}

loginForm.addEventListener("submit", onLoginSubmit);
```

> username 입력하면 form은 사라지고 h1에 이름 추가하기

- innerText와 classList.add/remove 사용

```js
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting"); 

const HIDDEN_CLASSNAME = "hidden"; // 일반적으로 string만 포함된 변수는 대문자로 표기

function onLoginSubmit(event) {
    event.preventDefault(); // 새로고침(기본동작) 막아줌
    loginForm.classList.add(HIDDEN_CLASSNAME);
    const username = loginInput.value;
    //greeting.innerText = "Hello " + username;
    greeting.innerText = `Hello ${username}`; // backtick사용
    greeting.classList.remove(HIDDEN_CLASSNAME);
}

loginForm.addEventListener("submit", onLoginSubmit);
```

- string과 변수를 합치는 방법(변수를 string안에 포함시키는 방법)
    1. "string "('string ') + 변수
    2. \`string ${변수}\` => backtick(`)사용

> username 저장하기 (value 저장하기)

- local storage API 사용
    - 작은 DB같은 API
    - 브라우저에 일단 저장하고 나중에 가져다가 사용하는 것이 가능
- method
    - `setItem()` : local storage에 정보 저장
    - `getItem()` : local storage에 저장된 정보 가져옴
    - `removeItem()` : local storage에 저장된 정보 삭제

> username 저장 여부에 따라 form 표시하기

- local storage가 비어 있으면 form 보여주지만 local storage에 유저정보가 있으면 form을 숨기고 h1을 보여주는 기능 구현
- local storage가 비어 있으면 `.getItem("username")`입력 시 null 리턴 -> if문 사용

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Momentum App</title>
</head>
<body>
    <form id="login-form" class="hidden">
        <input
        required
        maxlength="15" 
        type="text"
        placeholder="what is your name?"/>
        <button>Log In</button>
    </form>
    <h1 id="greeting" class="hidden"></h1>
    <script src="app.js"></script>     
</body>
</html>
```
- form과 h1 모두 처음에는 안 보이도록 .hidden 적용

```js
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting"); 

const HIDDEN_CLASSNAME = "hidden"; // 일반적으로 string만 포함된 변수는 대문자로 표기
const USERNAME_KEY = "username"; // string을 중복해서 사용하는 경우에 대문자 변수로 대체해서 사용(오타 확인 쉬움)

function onLoginSubmit(event) {
    event.preventDefault(); // 새로고침(기본동작) 막아줌
    loginForm.classList.add(HIDDEN_CLASSNAME);
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY, username);
    paintGreetings(username);
}

function paintGreetings(username) {
    greeting.innerText = `Hello ${username}`;
    greeting.classList.remove(HIDDEN_CLASSNAME); // handler 함수와 중복되는 부분이므로 따로 함수를 만들어서 사용
}

const savedUsername = localStorage.getItem(USERNAME_KEY);

if (savedUsername === null) {
    loginForm.classList.remove(HIDDEN_CLASSNAME);
    loginForm.addEventListener("submit", onLoginSubmit);
} else {
    paintGreetings(savedUsername);
}
```
- if문으로 username 저장 여부 확인한 뒤 form을 보여주고 submit event 발생하기를 기다렸다가  event가 발생하면 handler함수로 처리함
- handler함수가 실행되면 username은 local storage에 저장되고 form은 숨겨지며 h1에 텍스트 username이 입력되어 화면에 나타나게 됨 