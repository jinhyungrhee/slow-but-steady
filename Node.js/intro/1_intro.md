# Node.js 시작하기

## Node.js란?

- 자바스크립트는 원래 브라우저 안에서만 실행할 수 있는 코드
- 하지만 Node.js가 등장하면서 브라우저가 아닌 터미널에서도 실행 가능해짐!
- Node.js는 자바스크립트 실행환경이며, 엄밀히 따지면 프레임워크가 아님
  - Django 프레임워크는 프로그램의 구조가 미리 고정되어 있어서 MVT 패턴 내에서 개발을 해야 하지만, Node.js는 프로그램 내부의 전체 구조를 개발자 본인이 직접 설계해야 함 

## REPL 모드

- Read, Eval, Print, Loop의 약자
  - 사용자가 입력한 내용을 읽고 그 결과값을 구하여 값을 출력하고 이 과정을 계속 반복하는 모드
- 짧은 코드를 간단하게 테스트하고 싶을 때 사용
- 실행: 터미널에서 `node` 명령어만 입력
- 종료: `.exit`
- 코드
  ```cmd
  PS C:\codeit\nodeStudy> node
  Welcome to Node.js v16.14.0.
  Type ".help" for more information.
  > console.log('Hello codeit')
  Hello codeit
  undefined
  > for(let i = 0; i < 5; i++){
  ... console.log(i);
  ... }
  0
  1
  2
  3
  4
  undefined
  ```
  - javascript에서는 어떤 코드가 결과값을 별도로 리턴하지 않으면 undefined를 리턴한 것으로 간주함!
  ```cmd
  > function add(a, b) {
  ... return a + b;
  ... }
  undefined
  > add(3, 4)
  7
  ```

