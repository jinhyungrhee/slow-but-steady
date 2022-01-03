# 로그인은 얼마나 오랫동안 유지될까?

- 세션과 쿠키
  - ① 유저가 로그인 창에서 로그인 정보를 입력하고 로그인 버튼을 누름
  - ② 로그인 정보가 서버로 전달되고 서버는 로그인 아이디와 비밀번호가 일치하는지 확인
  - ③ 일치하면 서버에 유저에 대한 `세션(session)`이 생성됨
    - 세션은 유저의 웹 사이트 방문에 대한 기록임
      ```json
      '12345': { // Session ID는 랜덤하게 생성되는 값임
                  user_id : 1,
                  user_email: 'abcde@gmail.com`,
                }
      '23456': { // Session ID는 랜덤하게 생성되는 값임
                  user_id: 2,
                  user_email: 'anon@gmail.com',
                }
      ```
  - ④ 세션이 생성되면 user의 login request에 대하여 server가 login response를 보냄
    - 이때 Session ID를 포함해서 response를 보냄!
  - ⑤ Browser는 Session ID를 받아서 `쿠키(Cookie)`라는 곳에 저장함
    - 쿠키는 웹 사이트에 대한 정보를 저장하는 곳임
  - ⑥ Brower가 웹 사이트에 다른 request를 보낼 때 해당 웹 사이트에 대한 쿠키도 같이 전송됨
    - 즉 Session ID가 전송되는 것
  - ⑦ server는 Session ID를 확인하고 매칭되는 세션을 찾아서, 세션에 있는 유저를 현재 유저(=로그인된 유저)로 설정해줌
    - 즉 Session ID를 주고받음으로써 로그인이 유지가 되는 것!

- Chrome에서 세션ID 확인하기
  - 개발자도구/Application/Storage/Cookies
  - login시 SessionID가 생성되어 있음
  - logout시 SessionID가 삭제됨
    - 이때 browser가 server에 request를 보내면 더 이상 SessionID가 전송되지 않기 때문에 웹 서버는 현재 상태를 logout된 상태로 인식하게 됨!
      - **이 경우(직접 logout) web server 상의 세션 데이터는 삭제됨!**
    - 직접 logout하지 않아도 쿠키가 만료되어서 삭제될 수도 있음
      - **이 경우(세션쿠키 만료) web server 상의 세션 데이터는 삭제되지 않음!**
        - web server 상의 세션이 아주 많이 쌓이게 되면 많은 메모리를 차지하고 성능에 영향을 줄 수 있음
        - 실제 웹 사이트 운영 시, 만료된 세션 데이터를 지워주는 작업 필요
          ```py
          #django command
          python manage.py clearsessions
          ```
  - Remember Me
    - browser를 닫았을 때 세션쿠키를 유지할 것인지 삭제할 것인지 정하는 것

- Browser를 닫아도 항상 user를 기억하도록 설정
  - coplate_project/settings.py
    ```py
    # 항상 user session 기억하기
    ACCOUNT_SESSION_REMEMBER = True
    ```
    - Remember Me 체크박스 사라짐

- Cookie 유효시간 지정
  - default는 2주
  - coplate_project/settings.py
    ```py
    # 쿠키 유효시간 지정
    SESSION_COOKIE_AGE = 3600 # 1시간(=3600초)으로 변경
    ```
    - 한 시간 후 쿠키가 만료되면 다시 로그인 필요!