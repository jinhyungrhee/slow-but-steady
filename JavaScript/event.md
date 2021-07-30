## Event

### console.dir() 
    - element의 내부를 보는 메서드 (object로 표시한 element)
    - 그 중 on으로 시작하는 것은 event와 관련된 것임!
    - *object 내부에 있는 일부 property의 값들은 변경할 수 있음!* (불가능한 것도 존재)
    - object로 표현된 'h1'의 내부를 보다보면 'style'이 있고 그 안에 'color' property가 있음!
    - 따라서 h1의 style을 JavaScript에서도 변경할 수 있음!!
    ```js
    const title = document.querySelector(".hello:first-child h1");

    console.dir(title);

    title.style.color = "blue";
    ```

> JavaScript에서 대부분 하는 일은 Event를 listen하는 것!

### event란?
    - 클릭, 마우스 이동, 입력, 접속 해제 등 외부로부터 특정 값이 변경되는 것

- JavaScript에서 EventListener 등록

```js
const title = document.querySelector(".hello:first-child h1");

// 어떤 event를 listen하고 싶은지 명시!
title.addEventListener("click");
// JS는 title을 계속 지켜보다가 누군가 title을 click하는 것을 listen함
```

- EventHandler 함수도 등록

```js
const title = document.querySelector(".hello:first-child h1");

function handleTitleClick() {
    console.log("title was clicked!");
}

// handler함수를 listener의 두번째 인자로 전달
// event가 발생하면 해당 handler함수를 호출
title.addEventListener("click", handleTitleClick); 
```

### 예제 1 : 클릭 시 텍스트 색깔 변경

```js
const title = document.querySelector(".hello:first-child h1");

function handleTitleClick() {
    title.style.color = "blue";
}

title.addEventListener("click", handleTitleClick);
```

> listen하고 싶은 event를 찾는 법!

1. 'h1 html element mdn' 검색
    - HTMLHeadingElement - Web APIs | MDN 
    - (https://developer.mozilla.org/en-US/docs/Web/API/HTMLHeadingElement)

2. console.dir(element);
    - property 이름 앞에 on이 붙으면 그게 바로 event listener임!
        - ex) onmouseenter : 마우스가 해당 element위에 올라갔을 때의 event  
          ex) onmouseleave : 마우스가 해당 element에서 떨어졌을 때의 event

### 예제 2 : 마우스를 갖다 대거나 떼면 Text 변경

```js
const title = document.querySelector(".hello:first-child h1");

function handleTitleClick() {
    title.style.color = "blue";
}

function handleMouseEnter() {
    title.innerText = "Mouse is HERE!";
}

function handleMouseLeave() {
    title.innerText = "Mouse is GONE!";
}

title.addEventListener("click", handleTitleClick);
title.addEventListener("mouseenter", handleMouseEnter);
title.addEventListener("mouseleave", handleMouseLeave);
```

### 예제 3 : window 크기를 변경하면 body 색깔 변경 + 복사하면 "copier!" 경고 + wifi 온라인/오프라인 경고

```js
const h1 = document.querySelector(".hello:first-child h1");

function handleTitleClick() {
    h1.style.color = "blue";
}

function handleMouseEnter() {
    h1.innerText = "Mouse is HERE!";
}

function handleMouseLeave() {
    h1.innerText = "Mouse is GONE!";
}

function handleWindowResize() {
    document.body.style.backgroundColor = "tomato";
}

function handleWindowCopy() {
    alert("Copier!");
}

h1.addEventListener("click", handleTitleClick);
h1.addEventListener("mouseenter", handleMouseEnter);
h1.addEventListener("mouseleave", handleMouseLeave);

window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);
```

- window object도 JavaScript에서 기본적으로 제공함!
- 중요한 element인 body, head, title은 document를 이용하여 불러올 수 있음!
    - ex) document.body / document.head / document.title => O
- 나머지 element들은 querySelector나 getElementById등으로 찾아와야 함!
    - ex) document.div => X (undefined)


### 예제 4 : if-else문을 사용하여 text 색깔 변경

- const, let 사용 주의!
```js
const h1 = document.querySelector(".hello:first-child h1");

function handleTitleClick() {
    const currentColor = h1.style.color; // 비교하는 기존 색상 저장하는 변수
    let newColor; // 변하는 색상 저장하는 변수
    if(currentColor === "blue") {
        newColor = "tomato";
    } else {
        newColor = "blue";
    }
    h1.style.color = newColor; // update
}

h1.addEventListener("click", handleTitleClick);
```



### 정리
> Event를 사용하는 두 가지 방법
1. addEventListener()사용
    `title.addEventListener("click", handleTitleClick);`
2. onEventName사용
    `title.onclick = handleTitleCilck;`

    - addEventListener()가 더 유용
        - removeEventListener()로 event listener 제거할 수 있음!