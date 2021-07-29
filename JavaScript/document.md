## Document

### HTML 가져오기(document)

- 브라우저에 이미 존재하는 object
- 우리가 접근할 수 있는 HTML을 가리키는 객체
    - document가 HTML을 JavaScript의 관점(object 형태)으로 보여줌
    - **JavaScript에서 HTML document 객체로부터 title을 가지고 올 수 있음!**
    ```js
    document.title
    >> "Momentum"
    ```

> 브라우저가 HTML 정보가 아주 많이 들어있는 document라는 object를 전달해주는 것!

- JavaScript에서 HTML을 읽어오는 것 뿐만 아니라 HTML을 변경할 수도 있음
    ```js
    document.title = "HI"
    >> "HI"
    ```

- 중요한 것은 이 모든 설정들이 다 준비되어 있다는 것임!
    - HTML과 JavaScript를 연결하기 위해서 아무것도 하지 않아도 됨
    - 브라우저가 사용자에게 많은 유용한 것들이 들어있는 document 객체를 주기 때문

> JavaScript vs HTML : 동시에 적용하면 누가 이길까?

- app.js

```js
document.title = "Hello! From JS!";
```

- index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Hello! From HTML!</title>
</head>
<body>
    <script src="app.js"></script>     
</body>
</html>
```

- 결과
    - JS document win!

### HTML 변경하기1(getElementById)

> document.getElementById()

- Id를 사용하여 JavaScript를 이용해 HTML element에 접근
- element를 찾고나면 그 HTML에서 뭐든지 바꿀 수 있음
     - ex) innerText, className, autofocus ...

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Hello! From HTML!</title>
</head>
<body>
    <h1 id="title">Grab me!</h1>
    <script src="app.js"></script>     
</body>
</html>
```

```js
//console
document.getElementById("title")
>> <h1 id="title">Grab me!</h1>
```
- id="title"을 가진 \<h1>태그 가져옴

```js
//console.dir(title)
const title = document.getElementById("title")

console.dir(title)
```
- **console.dir()** : element의 내부를 보는 메서드 (object로 표시한 element)
    - *object 내부에 있는 일부 property의 값들은 변경할 수 있음!* (불가능한 것도 존재)
- \<h1>title 하나에서 가져올 수 있는 모든 것을 보여줌

```js
const title = document.getElementById("title")

title.innerText = "Got you!";
```

- JavaScript로 \<h1>태그 안의 값을 바꿔줄 수도 있음!

```js
const title = document.getElementById("title")

title.innerText = "Got you!";

console.log(title.id);
console.log(title.className);
```

- class 이름 확인하는 것도 가능!

### HTML 변경하기2(getElementsByClassName)

> document.getElementsByClassName()

- 여러 개의 elements를 한번에 가져와야 하는 경우에 사용

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
    <h1 class="hello">Grab me!</h1>
    <h1 class="hello">Grab me!</h1>
    <h1 class="hello">Grab me!</h1>
    <h1 class="hello">Grab me!</h1>
    <h1 class="hello">Grab me!</h1>
    <script src="app.js"></script>     
</body>
</html>
```
```js
const hellos = document.getElementsByClassName("hello");

console.log(hellos)

//값이 여러 개인 경우 배열에 담아서 리턴
>> HTMLCollection(5) [h1.hello, h1.hello, h1.hello, h1.hello, h1.hello]
```

### Element를 가져오는 가장 멋진 방법

> document.querySelector() : 첫 번째 값 하나만 리턴 (element)
> document.querySelectorAll() : 존재하는 모든 값 리턴 (array)

- element를 CSS 방식으로 검색 가능

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
    <div class="hello">
        <h1>Grab me!</h1>
    </div>
    <script src="app.js"></script>     
</body>
</html>
```

```js
const title = document.querySelector(".hello h1");

console.log(title)

>> <h1>Grab me!</h1>
```
- document.querySelector는 **한 개의 element만 리턴** (첫 번째 값)

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
    <div class="hello">
        <h1>Grab me1!</h1>
    </div>
    <div class="hello">
        <h1>Grab me2!</h1>
    </div>
    <div class="hello">
        <h1>Grab me3!</h1>
    </div>
    <script src="app.js"></script>     
</body>
</html>
```

```js
const title = document.querySelectorAll(".hello h1");

console.log(title)

>> NodeList(3) [h1, h1, h1]
```

- document.querySelectorAll는 **모든 element 리턴** (array로 리턴)

### 정리

- 모든 것들은 document로부터 시작함!
- 즉 document는 website를 의미함
    - ex) document.title , document.body ...