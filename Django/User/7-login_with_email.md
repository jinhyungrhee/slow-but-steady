# 이메일로 로그인하기

- 이메일로 로그인하고 회원가입하도록 allauth setting 변경
  - default는 username임
  - coplate_project/settings.py
    ```py
    # 이메일로 로그인하고 회원가입
    ACCOUNT_AUTHENTICATION_METHOD = "email"
    # 이메일과 username 둘다 허용
    #ACCOUNT_AUTHENTICATION_METHOD = "username_email"
    ```
- 회원가입 시 이메일 입력 필수로 변경하고 username 필드는 삭제
  - coplate_project/settings.py
    ```py
    # 회원가입 시 이메일 입력 필수로 변경
    ACCOUNT_EMAIL_REQUIRED = True
    # username 필드는 나타나지 않도록 함
    ACCOUNT_USERNAME_REQUIRED = False
    ```

- user model str메서드 변경
  - username 대신 email이 출력되도록 함
  - coplate/models.py
    ```py
    from django.db import models
    # AbstractUser 사용
    from django.contrib.auth.models import AbstractUser

    # Create your models here.
    # AbstractUser 상속받는 유저 클래스 생성 - 일단 틀만 생성(pass)
    class User(AbstractUser):
        # str 메서드 오버라이딩(username 대신 email 출력)
        def __str__(self):
            return self.email
    ```
  - 이때 template의 {{user}}은 그대로 사용함!
    ```html
    <h1>홈페이지</h1>
    <!-- 현재 유저의 정보 홈페이지에 추가 -->

    {% if user.is_authenticated %}
      <!-- 유저가 로그인되어있으면-->
      <p>안녕하세요, {{user}}님! </p>
    {% else %}
      <!-- 유저가 로그아웃 되어있으면-->
      <p>로그아웃된 상태입니다.</p>
    {% endif %}
    ```