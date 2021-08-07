## Background

- 이전까지는 항상 html을 먼저 작성하고 그 다음 JavaScript를 사용해서 작성한 html을 다뤄왔음
    - 한 번도 JavaScript에서 뭔가 생성해서 그걸 html에 추가해 본 적은 없었음!

- 이번 목표는 image를 생성해서 html에 추가해보는 것임
    - html에서는 할 수 없고 이미지를 추가하기 위해서는 JavaScript가 필요함!
    - JavaScript에서 이미지를 만들고 이것을 html에 추가해야 함!
    - `document.createElement()` 사용 : **JavaScript에서 HTML element 생성하는 메서드**
    - `document.body.appendChild()` 사용 : **인자를 해당 element의 자식 태그로 append(맨 뒤에 추가)하는 메서드** (↔prepend는 맨 앞에 추가)


- 코드
```js
const images = [
    "0.jpg",
    "1.jpg",
    "2.jpg",
];

const chosenImage = images[Math.floor(Math.random() * images.length)];

// img태그 생성
const bgImage = document.createElement("img");

// img태그 src속성에 대한 값 설정
bgImage.src = `img/${chosenImage}`;

// JavaScript에서 HTML element 생성(<img src="img/0.jpg">)
// console.log(bgImage);

// body 안에 추가하기
document.body.appendChild(bgImage);
```