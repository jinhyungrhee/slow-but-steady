# 회원가입 정보 유효성 검사

- 많은 유효성 검사를 django.contrib.auth와 allauth가 기본적으로 수행

- 장고 언어 세팅(기본 언어 변경)
  - coplate_project/settings.py
    ```py
    LANGUAGE_CODE = 'ko'
    ```

- nickname 필드 unique 오류 메시지 변경 : `error_messages 속성` 적용
  - coplate/models.py
    ```py
    class User(AbstractUser):
    # 닉네임 필드 정의
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True, 
        error_messages={'unique':'이미 사용중인 닉네임입니다.'},
    )
    ```

- nickname 필드 유효성 검사 추가 : validators.py import 필요
  - coplate/models.py
    ```py
    class User(AbstractUser):
    # 닉네임 필드 정의
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True, 
        validators=[validate_no_special_characters], # 닉네임에 대한 validator 추가
        error_messages={'unique':'이미 사용중인 닉네임입니다.'},
    )
    ```
  - settings.py 안의 AUTH_PASSWORD_VALIDATORS에 작성한 validator 추가
    ```py
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'coplate.validators.CustomPasswordValidator',
        },
    ]
    ```

- 폼에 대한 오류가 나도 입력했던 비밀번호 그대로 유지
  - settings.py
    ```py
    ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True
    ```