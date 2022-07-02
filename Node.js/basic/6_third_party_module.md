# 써드파티(3rd party) 모듈

- 다른 개발자나 회사들이 만들어서 인터넷상의 공개 저장소에서 제공하는 모듈

## 써드파티 모듈 사용해보기

- npm(node package manager) 사용하여 cowsay 모듈 다운 받음
  ```cmd
  npm install cowsay
  ```

- 설치가 완료되면 'node_modules' 디렉토리와 'package-lock.json', 'package.json' 파일이 생성됨

- main.js에서 cowsay 모듈의 say() 함수 사용
  ```js
  // 서드파티 모듈도 경로 표시 없이 이름만으로 require 사용
  const cowsay = require('cowsay');

  console.log(cowsay.say({
    text : "I love javascript",
  }));
  ```

- 결과
  ```cmd
  PS C:\codeit\nodeStudy> node main.js
  ___________________
  < I love javascript >
  -------------------
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\
                  ||----w |
  ```

## 써드파티 모듈 설치 후 생겨난 것들

1. package-lock.json

- dependencies : 현재 작업 디렉토리 안에 설치된 서드파티 모듈에 관한 정보가 기록되어 있음 (-> 프로젝트가 의존하고 있는 써드파티 모듈들)
- requires : 해당 모듈(써드파티 모듈)이 의존하는 다른 써드파티 모듈들의 이름이 적혀 있음.
- `다단계 의존 관계`
  - 예시) cowsay -> string-width -> strip-ansi -> ansi-regex 모듈
  - cowsay requeires 안에 ansi-regex 모듈은 없지만, cowsay는 ansi-regex 모듈을 **간접적으로 의존**하고 있음!
  - 이러한 관계를 **다단계 의존 관계**라고 함!

2. node_modules 디렉토리

- 써드파티 모듈들이 실제로 설치되는 공간
- 해당 공간에서 써드파티 모듈들은 하나의 `디렉토리`로 존재함
- 즉, **모듈은 하나의 파일일 수도 있고, 하나의 디렉토리일 수도 있음!**