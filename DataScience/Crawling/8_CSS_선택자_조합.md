# CSS 선택자 조합

## OR 연산

- OR 연산 : `쉼표(,)`
- 쉼표(,)로 연결된 선택자 중 하나라도 해당되면 선택함

```html
<p class="one">paragraph1</p>
<p class="two">paragraph2</p>
<p class="three">paragraph3</p>
<p class="four">paragraph4</p>
<p class="five">paragraph5</p>
```
```css
.two, .four {
  color: red;
}
```
- class 이름이 `"two"`이거나 `"four"`인 태그 선택하여 빨간색으로 지정

|CSS선택자|의미|
|--|--|
|#login, .left|아이디가 `login`이거나 클래스가 `left`인 태그|
|p, i|모든 `p`태그와 모든 `i`태그|

## AND 연산

- AND 연산 : `붙여쓰기`
- CSS 선택자를 붙여쓰면, 조건들에 모두 해당되는 요소만 선택함

```html
<p class="favorite">paragraph1</p>
<p class="favorite">paragraph2</p>
<p class="favorite private">paragraph3</p>
<p class="private">paragraph4</p>
<p class="private">paragraph5</p>
```
```css
.favorite.private {
  color: red;
}
```
- `"favorite"`클래스와 `"private"`클래스를 모두 가진 태그의 색상을 빨간색으로 지정

|CSS 선택자|의미|
|--|--|
|.favorite.private|`favorite`클래스와 `private`클래스를 모두 가진 태그|
|p.favorite|`favorite`클래스를 가진 `p`태그|

## 중첩된 요소

- HTML 태그 안에 또 다른 HTML 태그가 있는 경우
- 중첩된 요소만 가져오기 : `띄어쓰기`
```html
<i>디저트</i>
<p>
  <i>다쿠아즈</i>
  <i>마카롱</i>
  <i>케이크</i>
</p>
```
```css
p i {
  color: red;
}
```
- 모든 \<i>태그가 아닌 `<p>태그 안에 중첩된 <i>태그`만 빨간색으로 지정

|CSS선택자|의미|
|--|--|
|.favorite .private|`favorite`클래스를 가진 태그에 중첩된, `private`클래스를 가진 태그|
|p .favorite|`p`태그 아래 중첩된, `favorite`클래스를 가진 태그|

- 주의) `.class1 .class2`와 `.class1 > .class2` 차이
  - `.class1 .class2` : `class1`클래스를 가진 태그의 **자손** 중에 `class2`클래스를 가진 **모든** 태그
  - `.class1 > .class2` : `class1`클래스를 가진 태그의 **자식** 중에 `class2`클래스를 가진 태그