# Arrow Function

- 함수 표현 방식
  - 함수 선언식(Function Declaration)
    ```js
    function add(a, b) {
      return a + b;
    }
    ```

  - 함수 표현식(Function Expression)
    - 일반적인 함수 표현식
      ```js
      const add = function(a, b) {
        return a + b;
      };
      ```
    - 화살표 함수(Arrow Function)
      ```js
      const add = (a, b) => {
        return a + b;
      };
      ```
      - const add : 함수 이름
      

## Arrow Function

- 다른 함수의 인자로 들어가는 함수를 Arrow Function으로 나타내는 경우가 많음 

- 함수를 직접 선언하여 사용
  ```js
  const arr = [1, 2, 3, 4, 5];

  function getSquare(x) {
    return x * x;
  }

  const newArr = arr.map(getSquare);
  console.log(newArr); // [1, 4, 9, 16, 25]
  ```

- 익명 함수(Anonymous Function) 사용
  ```js
  const arr = [1, 2, 3, 4, 5];

  const newArr = arr.map(function(x) {
    return x * x;
  })

  console.log(newArr);
  ```
  - map함수의 인자로 들어간 함수는 위의 getSquare 함수의 바디에 해당 => 이름 없는 함수
  - 보통 함수에 함수를 인자로 넣을 때 Anonymous Function 사용
  - Anonymous Function을 Arrow Function 형태로 나타낼 수 있음!

- 화살표 함수(Arrow Function) 사용
  ```js
  const arr = [1, 2, 3, 4, 5];

  const newArr = arr.map((x) => {
    return x * x;
  });

  console.log(newArr);
  ```
  - 이처럼 Anonymous Function의 경우, Arrow Function을 쓰는 것을 권장하는 경우가 많음!