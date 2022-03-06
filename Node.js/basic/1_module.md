# 모듈이란?

- Node.js의 핵심개념
  - 모듈
  - 비동기 프로그래밍

## 모듈(Module)

- '전체를 이루는 부품 하나하나'를 의미
  - Node.js에서는 'Javascript 파일 하나'가 하나의 모듈
  - 이러한 모듈들이 모여서 하나의 프로그램이 되는 것!
- `모듈의 핵심` : **하나의 모듈에서 다른 모듈의 기능을 가져다 쓰는 법**을 배우는 것
  - 특정 함수를 사용하기 위해 다른 모듈을 가져오기
    - `require()` : 모듈을 load하는 함수. 모듈을 로드해서 객체 1개를 리턴
    - `exports.<함수명>` : '특정 모듈 안에 있는 함수를 모듈 외부에도 <함수명>이라는 이름으로 공개한다'는 의미
  - 코드
    - math-tools.js
      ```js
      function add(a, b) {
        return a + b;
      }

      // 모듈 내부의 것들을 외부로 공개해줘야 다른 모듈에서도 사용가능해짐 : exports.<함수명>
      // '모듈 안에 있는 함수를 모듈 외부에도 <함수명>이라는 이름으로 공개한다'는 의미

      // exports.add = add;
      exports.plus = add; // 함수 이름을 다르게 공개하는 것도 가능!
      ```
    - main.js
      ```js
      // 모듈 load하기 (특정 변수에 객체 저장 필요)
      let m = require('./math-tools.js');

      // 하나의 모듈에서 다른 모듈 함수 사용하기

      //console.log(m.add(1, 2));
      console.log(m.plus(1, 2));
      ```

- 기타
  - ⭐require 함수가 리턴하는 객체는 `상수(constant)`로 대입하는 것을 권장⭐
    - 변수 vs 상수
      - 변수(variable) : 값을 원할 때마다 새롭게 지정 가능
      - 상수(constant) : 값을 한 번 설정한 후에는 다른 값을 설정할 수 없음
      ```js
      let m = require('./math-tools.js'); // 권장X

      const m = require('./math-tools.js'); // 권장O
      ```
    - 이유
      - 모듈이 리턴한 객체를 변수로 받으면, 나중에 본인 또는 다른 개발자가 변수 m에 다른 값을 실수로 다시 지정할 가능성 有
        - 이 경우, 에러가 발생하지 않지만 의도치 않은 오류가 발생할 수 있음! (더 위험)
        - 상수로 리턴 객체를 받으면, 변수 m에 값을 재지정하려고 할 경우 에러를 발생 시킴 => 더 큰 위험을 사전에 방지 
  - 모듈 안의 모든 것을 공개하기 가능
    - 코드
      - math-tools.js
        ```js
        const PI = 3.14;
        let author = 'codeIt teacher';

        function add(a, b) {
          return a + b;
        }

        let test = {
          date: '2020-09-20',
          types: ['safetyTest', 'performanceTest'],
          printTypes() {
            for (const i in this.types) {
              console.log(this.types[i]);
            }
          }
        };

        // 모든 것을 공개
        exports.PI = PI;
        exports.author = author;
        exports.add = add;
        exports.test = test;
        ```
    - main.js
      ```js
      const m = require('./math-tools');

      console.log(m.PI);
      console.log(m.author);
      console.log(m.add(1, 2));
      console.log(m.test.date);
      console.log(m.test.types);
      m.test.printTypes();
      ```
    - 결과
      ```cmd
      PS C:\codeit\nodeStudy> node main
      3.14
      codeIt teacher
      3
      2020-09-20
      [ 'safetyTest', 'performanceTest' ]
      safetyTest
      performanceTest
      ```

## 하나의 객체로 모아서 외부에 공개하기

- ① 하나씩 exports를 붙여서 공개
  - **모듈 안에 있는 것(변수, 함수)들을 하나씩 공개** -> `exports`
  - math-tools.js
    ```js
    exports.PI = 3.14;
    exports.add = function add(a, b) { return a + b; };
    exports.subtract = function subtract(a, b) { return a - b; };
    exports.multiply = function multiply(a, b) { return a * b; };
    exports.divide = function divide(a, b) { return a / b; };
    ```

- ② 공개하려는 것을 모아서 하나의 객체로 만들고 그 객체를 공개
  - **공개하고 싶은 것들을 모은 '객체'를 외부에 공개** -> `module.exports`
  - 외부에 공개하고 싶은 것들이 많은 경우 사용
  - math-tools.js
    ```js
    // 기존의 변수와 함수를 calculator 객체의 속성과 메서드로 설정 
    let calculator = { 
      PI : 3.14,
      add: (a, b) => a + b,
      subtract: (a, b) => a - b,
      multiply: (a, b) => a * b,
      divide: (a, b) => a / b,
    };
    // calculator 객체 자체를 외부에 공개
    module.exports = calculator;
    ```
  - main.js
    ```js
    const m = require('./math-tools'); // calculator 객체를 리턴
    
    console.log(m.PI);
    console.log(m.add(2, 4));
    console.log(m.subtract(2, 4));
    console.log(m.multiply(2, 4));
    console.log(m.divide(2, 4));
    ```