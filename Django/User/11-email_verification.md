# 이메일 인증 기능

- 가입한 이메일이 본인이 실제 사용하는 이메일인지 확인하는 절차

- ACCOUNT_EMAIL_VERIFICATION 세팅 적용
  - 3개의 값 적용 가능
    - mandatory : 이메일 인증을 완료할 때까지 로그인 할 수 없음
    - optional : 회원가입 시 인증 요청 메일이 발송되지만 이메일 인증을 하지 않아도 로그인은 할 수 있음 (default, 없으면 해당 값 적용!)
    - none : 인증 요청 메일이 발송되지 않고, 이메일 인증이 필요 없음
  - 회원가입 후 터미널 확인
    ```
    From: webmaster@localhost
    To: user3@codeit.com
    Date: Tue, 04 Jan 2022 01:22:36 -0000
    Message-ID: <164125935685.33344.8694728347429785503@DESKTOP-5ONIL2T>

    Hello from example.com!

    You're receiving this e-mail because user user3 has given your e-mail address to register an account on example.com.

    To confirm this is correct, go to http://127.0.0.1:8000/confirm-email/Ng:1n4YX6:uQcYqwfFNL1pRf9K29W9g7g5MOE/

    Thank you for using example.com!
    example.com
    ```

- 인증 메일 메시지 바꿔주기(?)
  - settings.py
    ```py
    ACCOUNT_CONFIRM_EMAIL_ON_GET = True
    ```

- '인증 완료 페이지'로 리디렉션
  - coplate_project/urls.py
    - '인증 완료 페이지'는 allauth와 연관된 페이지기 때문에 프로젝트 url 파일에 패턴을 만들어줌!
    - 장고에서 단순 템플릿을 랜더링할 때 제네릭뷰(템플릿뷰) 사용! -> 따로 뷰를 정의하지 않고도 사용할 수 있음!
    ```py
    urlpatterns = [
      path('email-confirmation-done/',
      TemplateView.as_view(template_name="coplate/email_confirmation_done.html"),
      name="account_email_confirmation_done"), # 장고에서 단순 템플릿을 랜더링할 때 제네릭뷰(템플릿뷰) 사용! (뷰 자리에 템플릿 뷰 사용)
    ]
    ```
    - view에 따로 설정하지 않고 urls.py에서 바로 template view 적기 가능
  - 템플릿 생성
    - template/coplate/email_confirmation_done.html
      ```html
      이메일 인증이 완료되었습니다.
      <!-- 유저가 로그인된 상태면 -->
      {% if user.is_authenticated %}
        <!-- 홈 링크 (url name 사용)-->
        <a herf="{% url 'index' %}">홈으로 이동</a>
      <!-- 유저가 로그아웃 상태면 -->  
      {% else %}
        <!-- 로그인 페이지 링크 (url name 사용)-->
        <a herf="{% url 'account_login' %}">로그인 하기</a>
      {% endif %}
      ```
  - 인증 완료 페이지로 리디렉션 세팅
    - coplate_project/settins.py
      ```py
      # 인증 완료 페이지로 리디렉션
      ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "account_email_confirmation_done"
      ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_confirmation_done" 
      ```