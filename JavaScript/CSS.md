## CSS
- JavaScript안에서 CSS 작업을 하는 것은 바람직하지 않음
- CSS 작업은 CSS 파일 안에서!
```css
/*style.css*/
body {
    background-color: beige;
}

h1 {
    color: blue;
}

.active {
    color: tomato;
}
```
> h1이든, span이든 어떤 element든지 active를 클래스명으로 적용하면 tomato 색깔을 가지게 됨! 

```js
//app.js
const h1 = document.querySelector(".hello:first-child h1");

function handleTitleClick() {
    h1.className = "active"; // 현재 이 코드는 getter이면서 setter임!
}

h1.addEventListener("click", handleTitleClick);
```
> JavaScript가 CSS를 직접 건드리지 않고 html만을 변경함  
> 그러면 HTML을 바라보고 있던 CSS는 변경된 HTML에 새로운 값을 적용하게 됨  
> 이것이 더 바람직한 방법!(더 적은 JS코드, 덜 헷갈림)

### 예제 1 : CSS와 JS를 분리해서 클릭 시 색깔 변경
```css
body {
    background-color: beige;
}

h1 {
    color: blue;
    transition:color .5s ease-in-out /*천천히 바뀜*/
}

.active {
    color: tomato;
}
```

```js
const h1 = document.querySelector(".hello:first-child h1");

function handleTitleClick() {
    const clickedClass = "active"; 
    // "active"라는 raw value를 직접 if문의 비교에 사용하지 않고 변수에 담아서 사용
    if(h1.className === clickedClass) {
        h1.className = "";
    } else {
        h1.className = clickedClass;
    }
}

h1.addEventListener("click", handleTitleClick);
```
> 실수를 방지하기 위해 raw value(string)을 직접 사용하는 대신에 const변수에 담아서 사용  
> raw value의 오타는 JavaScript가 알려주지 못하지만 변수의 오타는 체크해서 알려줌!

### 예제 1 문제점

- 기존에 이미 다른 클래스로 CSS 적용을 받고 있다면 JS로 클래스 변경 시 기존 클래스는 사라져버림

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
        <h1 class="sexy-font">Click me!</h1>
    </div>
    <script src="app.js"></script>     
</body>
</html>
```

```css
body {
    background-color: beige;
}

h1 {
    color: blue;
    transition:color .5s ease-in-out
}

.active {
    color: tomato;
}

.sexy-font {
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
     Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
```

```js
const h1 = document.querySelector(".hello:first-child h1");

function handleTitleClick() {
    const clickedClass = "active";
    if(h1.className === clickedClass) {
        h1.className = "";
    } else {
        h1.className = clickedClass;
    }
}

h1.addEventListener("click", handleTitleClick);
```

- sexy-font라는 클래스를 삭제하지 않고 clickedClass 적용하는 방법?
    - className 대신 **classList** 사용!

### classList

- classList는 말그대로 class들의 목록으로 작업할 수 있도록 함
    - classList.contains(className) : class들의 목록이 해당 클래스를 포함하고 있는지 확인  
    - classList.add(className) : class들의 목록에 해당 클래스를 추가
    - classList.remove(className) : class들의 목록에서 해당 클래스 삭제
    ```js
    const h1 = document.querySelector(".hello:first-child h1");

    function handleTitleClick() {
        const clickedClass = "active";
        if(h1.classList.contains(clickedClass)) {
            h1.classList.remove(clickedClass);
        } else {
            h1.classList.add(clickedClass);
        }
    }

    h1.addEventListener("click", handleTitleClick);
    ```

    - 이 일련의 과정들은 `classList.toggle()`로 대체될 수 있음!
        - toggle은 classList에 인자로 받은 class가 있는지 확인해서 만약 있다면 해당 클래스를 제거하고 없다면 해당 클래스를 추가함
        - 위 과정을 간단히 하나의 함수로 만든 것
    ```js
    const h1 = document.querySelector(".hello:first-child h1");

    function handleTitleClick() {
        h1.classList.toggle("active");
    }

    h1.addEventListener("click", handleTitleClick);
    ```