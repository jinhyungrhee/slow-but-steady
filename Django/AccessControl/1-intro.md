# 뷰 접근 제어하기 : Decorator와 Mixin

- 웹사이트 제어
  - 로그인을 해야 리뷰 작성 가능!
  - 내가 작성한 리뷰만 수정/삭제 가능!  
  ➡ 유저가 **특정 웹 페이지**로 들어가는 것을 제한

- 예시
  - User01이 User02가 작성한 Review03에 `localhost:8000/reviews/3/delete/`로 접근했을 경우
    - 접근 오류 발생
    - 또는 특정 페이지로 리디렉트

- 뷰 접근 제어
  - 유저가 어떤 웹 페이지에 대해서 request를 보내면, 해당 request를 처리해주는곳이 `View`임!
  - 그러므로 View에 대한 접근을 제어해줘야 함
  - 방식 : `decorator` 또는 `mixin` 사용
    - 기존의 코드에 추가 기능을 더해주는 역할
    - `decorator` : 함수형 뷰에 사용됨
    - `mixin` : 클래스형 뷰에 사용됨

- Request 처리 과정(**mixin 사용**)
  - 어떤 URL에 대해서 request가 들어오면, 장고는 해당 URL을 보고 request를 올바른 View로 보내줌 : `URL Dispatcher`
  - View는 정해진 로직을 통해서 request를 처리하고 response를 돌려줌
  - 이때 `mixin`은 View 앞에 위치하여, request가 View에 도착하기 전에 mixin의 로직을 먼저 거치도록 함!
    - mixin 부분에 "해당 View에 접근하려면 유저는 로그인이 되어있어야 한다" 같은 로직을 넣어줄 수 있음
      - 만약 로그인이 되어있으면, request를 그대로 View에 전달해줌
      - 만약 로그인이 되어있지 않으면, (View를 거치는 대신) 로그인 페이지로 리디렉트하는 redirect response를 돌려주거나 View에 접근할 권한이 없다는 forbidden response를 돌려주면 됨
  
- 접근 제어 관련 mixin을 제공하는 패키지 (여러가지 존재)
  - `django.contrib.auth`
    - 장고 프레임워크에 포함되어 있으나, 마음대로 커스터마이징해서 원하는 로직을 구현하기 어려움
  - `django-braces` ✔
    - 접근 제어와 관련된 여러 가지 mixin(=`Access Mixin`)들을 제공

- django-braces 설치
  ```cmd
  $ pip install django-braces
  ```