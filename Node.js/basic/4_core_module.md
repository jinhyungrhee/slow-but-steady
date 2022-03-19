# Node.js에서의 모듈

- 내가 직접 만든 모듈
- 이미 만들어져 있는 모듈
  - 코어 모듈
    - Node라는 실행프로그램 안에 이미 포함되어 있는 모듈
    - Node만 설치하고 나면 바로 사용 가능
  - 서드파티 모듈
    - 여러 개발자나 회사들이 만들어서 인터넷의 공개 저장소에서 제공하는 모듈
    - 제 3자가 제작한 모듈

## Core 모듈

- 종류
  - fs(file system) 모듈 : 파일이나 디렉토리에 관한 작업을 할 때 필요한 코어 모듈
    ```js
    // main.js
    const fs = require('fs');

    // readdirSync() : 특정 디렉토리 안에 있는 파일 목록들을 배열 형식으로 리턴하는 함수
    let fileList = fs.readdirSync('.');
    console.log(fileList);

    // 파일에 내용을 작성하는 함수(또는 파일을 새로 생성하는 함수)
    fs.writeFileSync('new', 'Hello Node.js!');
    ```
    - Node 프로그램 안에 내장되어 있기 때문에 require 함수 안에 경로를 표시해줄 필요 없음!

  - os(operating system) 모듈 : 컴퓨터에 설치된 운영체제와 관련된 정보를 가져오기 가능
    ```js
    // main.js
    const os = require('os');

    // 현재 컴퓨터의 CPU 정보를 출력하는 함수
    console.log(os.cpus());
    ```

  - 더 많은 코어 모듈은 Node.js 공식 문서 확인 (https://nodejs.org/dist/latest-v12.x/docs/api/)

- 정리
  - 위와 같은 작업들은 일반(browser에서의) Javascript가 절대 할 수 없는 작업들임
  - 하지만 서버용 프로그램을 만들기 위해서는 이러한 기능들이 꼭 필요하기 때문에 Node.js에서 관련 함수들을 제공함
  - 즉, Node.js를 활용하면 컴퓨터의 더 깊은 부분까지 Javascript로 제어할 수 있게 됨!