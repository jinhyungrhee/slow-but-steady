## User model

- django.contrib.auth는 User model 제공
    - 기본 유저 모델 : `User`
        - 권장 X
        - 유저 모델을 한 번 정의하면 다른 모델로 바꾸기 매우 어려움!
        - 현재 추가 필드가 필요 없다고 하더라도 처음부터 AbstractUser 모델을 사용하고 클래스를 비워놓는 것이 더 바람직 
    - 상속 받아서 쓸 수 있는 유저 모델 : `AbstractUser`
        - 우리가 원하는 필드를 추가해서 사용 가능
        - 기본 필드와 메서드들이 다 정의되어 있음
            - username : 로그인 시 사용되는 login ID
            - password
            - first_name
            - last_name
            - email
            - date_joined
            - last_login
        - '닉네임' 같은 필요한 필드를 그냥 추가적으로 정의해서 사용하면 됨(`nickname = models.CharField(..)`)
    - 상속 받아서 쓸 수 있는 유저 모델 : `AbstractBaseUser`
        - AbstractBaseUser를 상속받아서 커스터마이징
        - User를 만들기 위한 **틀만 제공**하며 User에게 필요한 모든 필드를 직접 정의해줘야 함 (말 그대로 Base임)
        - 기본적으로 제공되는 필드 대신 모두 커스터마이즈하여 필드를 사용하고 싶다면 AbstractBaseUser 사용


## 코드로 확인

- **User 모델 등록**(생성)
    - AbstractUser import
    - coplate/models.py
        ```py
        from django.db import models
        # AbstractUser 사용
        from django.contrib.auth.models import AbstractUser

        # Create your models here.
        # AbstractUser 상속받는 유저 클래스 생성 - 일단 틀만 생성(pass)
        class User(AbstractUser):
            pass
        ```

- User 모델 생성(등록) 후 **AUTH_USER_MODEL 설정**하기 (중요!)
    - coplate app에 있는 User모델을 이번 프로젝트 내에서 user모델로 사용하겠다는 의미
    - 마이그레이션 시 우리의 커스텀 유저 모델을 참조해서 테이블을 만들어주고 allauth가 커스텀 유저모델을 사용함
    - coplate_project/settings.py
        ```py
        # ... 생략
        # 맨 아래에 추가
        AUTH_USER_MODEL = "coplate.User"
        ```

- User모델이 변경되었으므로 **migration** 해줌
    - User모델 생성 후 AUTH_USER_MODEL 설정 후 첫 migration 해주기!
        - 그렇지 않으면 user 테이블에 대한 migration이 서로 꼬여서 고치기 힘든 오류들이 발생
    - `python manage.py makemigrations`
        - 결과
            ```
            Migrations for 'coplate':
            coplate\migrations\0001_initial.py
                - Create model User
            ```
    - `python manage.py migrate`
        - 결과
                ```
                Operations to perform:
                Apply all migrations: admin, auth, contenttypes, coplate, sessions
                Running migrations:
                Applying contenttypes.0001_initial... OK
                Applying contenttypes.0002_remove_content_type_name... OK
                Applying auth.0001_initial... OK
                Applying auth.0002_alter_permission_name_max_length... OK
                Applying auth.0003_alter_user_email_max_length... OK
                Applying auth.0004_alter_user_username_opts... OK
                Applying auth.0005_alter_user_last_login_null... OK
                Applying auth.0006_require_contenttypes_0002... OK
                Applying auth.0007_alter_validators_add_error_messages... OK
                Applying auth.0008_alter_user_username_max_length... OK
                Applying auth.0009_alter_user_last_name_max_length... OK
                Applying auth.0010_alter_group_name_max_length... OK
                Applying auth.0011_update_proxy_permissions... OK
                Applying coplate.0001_initial... OK
                Applying admin.0001_initial... OK
                Applying admin.0002_logentry_remove_auto_add... OK
                Applying admin.0003_logentry_add_action_flag_choices... OK
                Applying sessions.0001_initial... OK
                ```