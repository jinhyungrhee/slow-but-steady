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