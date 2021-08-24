## django.contrib.auth

- 유저 기능을 구현하는데 쓰이는 장고에 포함된 앱
- contrib = contributed(기여하다)
    - 사람들이 빠르고 간편하게 웹 개발을 하도록 이미 완성된 장고 앱
    - 장고 프레임워크에 기여된 앱들
        - django.contrib.admin : 관리자 기능 제공
        - django.contrib.staticfiles : css같은 정적 파일을 다룰 때 사용
    - 장고 프로젝트 생성 시 여러 contrib앱들이 자동으로 생성됨
- auth = authentication(유저인증)
- django 앱 구성
    - models
    - urls
    - views
    - forms 등

- django.contrib.auth도 동일함
    - User model (models)
    - /login/logout (urls) : url 패턴 정의
    - login logic(views, forms) : login logic 처리

- django.contrib.auth 대신 django-allauth 사용!
    - django-allauth : 유저 기능을 위한 패키지
    - 기본적으로 설치되어 있지 않기 때문에 따로 설치해줘야 함

## django-allauth

- 유저기능에 필요한 url, view, form등이 포함되어 있지만 User model은 포함되어 있지 않기 때문에 django.contrib.auth의 User model 사용
- 모델은 django.contrib.auth 사용, 기능은 django-allauth 사용!
- 실제 존재하는 이메일인지 확인하는 이메일 인증 기능 제공
- 소셜 서비스를 이용해서 로그인 하는 소셜 로그인 기능 제공
- 유저 기능이 이미 다 완성되어 있어서 짧은 코드 몇 줄로 우리가 원하는 설정만 해주면 됨(contrib.auth는 필요한 부분 직접 구현해야 함)
