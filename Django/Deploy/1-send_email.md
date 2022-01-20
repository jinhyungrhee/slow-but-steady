# 이메일 전송 제대로 하기

## 이메일 전송 원리

- 일반적인 이메일 작성 후 '전송'버튼 클릭
  - 이메일이 도메인의 이메일 서버(gmail.com)로 전송됨
    - 이메일 서버 : 이메일의 송수신을 다루는 서버
    - SMTP(Simple Mail Transfer Protocol) 서버 : 이메일의 전송만을 다루는 이메일 서버
  - 해당 이메일 서버(gmail.com)는 수신 도메인 이메일 서버(naver.com)로 이메일을 전송함
  - 수신자는 수신 도메인 이메일 서버(naver.com)로부터 이메일을 전달받음

- django 어플리케이션 경우에도 이메일 전송 방식은 동일함!
  - GMAIL 클라이언트를 사용할 경우, SMTP서버가 GMAIL SMTP서버로 자동으로 설정됨
  - ⭐django 어플리케이션을 사용할 경우, SMTP 서버를 따로 설정해줘야 함!⭐

## gmail을 SMTP서버로 사용하도록 설정

- django 어플리케이션이 GMAIL 계정을 사용할 수 있도록 설정
  - ①앱 비밀번호 생성
    - 구글 로그인 후 주소창에 `myaccount.google.com` 입력
    - 보안 탭 클릭
    - 2단계 인증 활성화
    - 앱 비밀번호 생성 : django 어플리케이션에서는 '앱 비밀번호'를 사용해서 구글 계정에 로그인할 수 있음!
      - 기타(맞춤 이름) : django-coplate
  - ②프로젝트 settings 파일(coplate_project/settings.py)에서 `Email settings`부분 수정
    - 기존 : console 사용
      ```py
      # Email settings
      EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
      ```
    - **변경 : gmail smtp서버 사용**
      ```py
      # Email settings
      EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend" # 이 설정은 default이므로 지워도 OK
      # gmail smtp서버를 사용하기 위한 세팅
      EMAIL_HOST = "smtp.gmail.com"
      EMAIL_PORT = 587
      EMAIL_USE_TLS = True
      # 인증 정보 추가
      EMAIL_HOST_USER = "XXXXXXXX"
      EMAIL_HOST_PASSWORD = "XXXXXXXX"
      ```
      - 결과 : 해당 계정 이름으로 메일이 전송됨!