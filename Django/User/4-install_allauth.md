## django allauth 설치하기

- 공식문서 확인(https://django-allauth.readthedocs.io/en/latest/installation.html)

1. pip install
    - `pip install django-allauth`

2. settings.py에 여러 가지 setting 추가하기
    - AUTHENTICATION_BACKENDS 부분 추가
        - 유저 인증 로직을 담당하는 컴포넌트
        - `'django.contrib.auth.backends.ModelBackend',` 추가
        - `'allauth.account.auth_backends.AuthenticationBackend',` 추가
    - 코드
    ```py
    AUTHENTICATION_BACKENDS = [

        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by e-mail
        'allauth.account.auth_backends.AuthenticationBackend',

    ]
    ```

    - 여러 앱들을 INSTALLED_APPS 목록에 추가해줘야함
        - 필수 항목
            - 'auth'와 'messages'는 이미 존재하는 앱이므로 생략
            ```py
            #'django.contrib.auth',
            #'django.contrib.messages',
            'django.contrib.sites',

            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            ```

        - `'allauth.socialaccount.providers.서비스명`은 소셜로그인과 관련된 것 (원하는 것만 가져다 사용)

        - 코드
        ```py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.sites',
            'coplate',
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
        ]
        ```

    - SITE_ID도 추가
        - `SITE_ID = 1`
            - INSTALLED_APPS 아래에 추가
        - `'django.contrib.sites',`는 어떤 기능을 여러 웹사이트에서 사용할 수 있게 해주는 것
            - 비슷한 콘텐츠나 기능을 가지고 있는 웹사이트가 여러 개 필요할 때는 이것을 사용해서 django 프로젝트 하나로 여러 웹 사이트 운영 가능
            - 그 때 각각의 사이트를 구분하기 위한 ID가 바로 `SITE_ID = 1`임!

    - SOCIALACCOUNT_PROVIDERS 는 소셜로그인과 관련된 부분이므로 일단 생략

    - URL 패턴 추가 (urls.py)
        - url 패턴
            ```py
            urlpatterns = [
                ...
                path('accounts/', include('allauth.urls')),
                ...
            ]
            ```
        - ❗하지만 이대로 추가하면 `'acccount/s' + 'allauth의 url들'` 형태가 됨❗ ➡ *지저분*
            - ex) accounts/login
            - ex) accounts/signup

        - 깔끔하게 login, signup만 url에 나오도록 하기 위해서‼
            - URL은 empty pattern('')에 연결
            - (project 파일) coplate_project/`urls.py`에 'accounts/`없이 추가!
                ```py
                from django.contrib import admin
                from django.urls import path, include

                urlpatterns = [
                    path('admin/', admin.site.urls),
                    path('', include('allauth.urls')),
                ]
                ```

    - 문서에 없는 추가 setting
        - settings.py 맨 아래에 **Email Setting** 추가
            - allauth가 제공하는 이메일 인증이나 비밀번호 찾기 기능을 활용하려면 이메일을 보낼 수 있어야 하는데 이메일을 어떻게 보낼지를 설정하는 setting
            - `"django.core.mail.backends.console.EmailBackend"`는 터미널 콘솔로 이메일을 보내도록 하는 설정
            ```py
            # ..생략..
            # Email settings

            EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"    
            ```
        - 나중에 추가적인 setting 有

- 문서에 따라서 allauth를 설치해주기만 하면 기본적인 auth 관련 페이지들이 자동으로 set-up됨

- ❗변경된 auth를 server에서 확인하기 전에 app을 여러 개 추가했으므로 다시 한 번 `migration` 진행❗
    - `python manage.py migrate`

- Server에서 확인하기
    1. `python manage.py runserver`
    2. 터미널 URL이 아닌 `http://localhost:8000/login/`로 직접 입력해서 들어가기

- 확인 결과
    - 우리가 `Sign In`, `Sign Up`, `Forgot Password?`, `Remember Me`등의 페이지와 기능들을 만들어준 적이 없지만 allauth를 우리 프로젝트에 설치만 해주면 이러한 기능들이 모두 제공됨
    - 우리는 단순히 여기에 몇 가지 세팅을 추가해 User 기능을 우리가 원하는 대로 바꿔주기만 하면 됨! 