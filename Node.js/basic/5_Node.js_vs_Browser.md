# Node.js와 브라우저의 차이

- 제공하는 API가 다름
  - API(Application Programming Interface)
    - 어떤 플랫폼이나 실행환경 등에서 제공하는 인터페이스
    - 특정 환경에서 자유롭게 가져다 쓸 수 있는 함수나 객체 등
  - Node.js에서 제공하는 API
    - 컴퓨터 제어 API
  - 브라우저에서 제공하는 API
    - UI 관련 API
    - window, document 객체

- Node.js는 PC용 프로그램을 제작할 때 사용됨
  - Electron 프레임워크를 사용하면 Node.js 위에서 돌아가는 PC용 프로그램 제작 가능
    - ex) visual studio code

- Javascript를 실행하는 엔진이 다름
  - Node.js가 사용하는 엔진
    - V8
  - 브라우저가 사용하는 엔진(종류에 따라 다름)
    - Chrome Browser : V8
    - Firefox : SpiderMonkey
    - Microsoft Edge : V8, Chakra

## Node.js 개발 팁

- 특정 부라우저가 Javascript의 표준 문법 중에서 어디까지를 지원하는지 확인하는 것 중요!
- 각 브라우저별 Javascript 표준 구현 현황 (https://kangax.github.io/compat-table/es6/)
  - IE = Internet Explorer
  - FF = FireFox
  - CH = chrome
