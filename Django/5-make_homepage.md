# 홈페이지 만들기

## allauth - 회원가입 인증 메일 관련

- 일단 아무것도 만들지 않은 상태에서 Signup 페이지에서 회원가입을 진행하면 `Page not found(404)`에러 발생
    - default 리다이렉션 주소 : `http://localhost:8000/accounts/profile/`
    - 회원가입이 완료되면 accounts/profile/로 리다이렉트 되도록 설정되어있지만 해당 페이지는 우리가 아직 만들지도 않았고 allauth에서 기본적으로 제공하는 페이지도 아님!
    - **이는 단순히 리다이렉션 문제이고 그와 별개로 회원가입은 성공적으로 진행됨**
        - 리다이렉션 주소를 홈으로 바꿔주는 것 필요 
    - 위 과정을 거쳤을 때 콘솔에 출력되는 메시지
        ```shell
        Subject: [example.com] Please Confirm Your E-mail Address
        From: webmaster@localhost
        To: user1@gmail.com
        Date: Sat, 28 Aug 2021 02:56:25 -0000
        Message-ID: <163011938554.27300.12783835022454201651@DESKTOP-5ONIL2T>

        Hello from example.com!

        To confirm this is correct, go to http://localhost:8000/confirm-email/MQ:1mJoW9:okaPIhtSIPHimYqZU92rZ6kWxv8/     

        Thank you for using example.com!
        example.com
        ```
            ➡ 회원가입을 했기 때문에 이메일 인증을 해달라고 메일이 전송된 것
            ➡ 이러한 이메일 인증 기능도 setting을 통해서 바꿔줄 수 있음

        
## 홈페이지 URL 만들기

1. coplate_project/urls.py에 empty url패턴을 coplate앱의 url로 연결시킴
    ```py
    urlpatterns = [
        path('admin/', admin.site.urls),
        # empty url패턴을 coplate앱의 url로 연결
        path('', include('coplate.urls')),
        path('', include('allauth.urls')),
    ]
    ```
    - django가 url 매칭을 할 때는 성공적인 매칭이 될 때까지 **가장 위에 있는 패턴부터** 하나씩 확인해 나감
        - 예를들어) 127.0.0.1:8000/example/path라는 URL이 나왔을 때  
            ➡ `path('admin/', admin.site.urls)`: URL의 앞부분(example)이 'admin'과 매칭되지 않으므로 다음줄로 넘어가서 확인  
            ➡ `path('', include('coplate.urls'))`: 다음줄은 empty string이므로 우선 이 부분과 매칭되어 coplate의 url로 넘어감(coplate의 url에 'example/path'와 같은 url이 있으면 매칭이 되고, 없어서 매칭이 되지 않으면 다시 다음 줄로 넘어감)  
            ➡ `path('', include('allauth.urls'))` : allauth 내부 URL에서도 이것(example/path)과 같은 패턴이 있는지 찾아봄(있으면 매칭이 되어 로직을 담당하는 View로 넘어가고, 없으면 더 이상 검색할 urlpattern이 없기 때문에 페이지가 없다는 에러를 발생시킴)

2. coplate/urls.py 생성
    - 새로 생성한 coplate 앱에는 urls.py가 없으므로 생성
    - view를 import
    - empty pattern을 index view에 연결, url name을 'index'로 설정
        ```py
        from django.urls import path
        # view 가져오기
        from . import views

        urlpatterns = [
            # empty pattern을 index view에 연결, url name을 'index'로 설정
            path("", views.index, name="index"),
        ]
        ```

3. coplate/views.py 작성
    - index라는 template을 render해주는 간단한 view
        ```py
        from django.shortcuts import render

        # Create your views here.
        # index라는 template을 render해주는 간단한 view
        def index(request):
            return render(request, "complate/index.html")
        ```

4. index.html 생성
    - complate 앱 안에 templates 디렉토리 생성
    - templates 디렉토리 안에 complate 디렉토리 생성
    - complate/templates/complate 안에 index.html 생성
        ```html
        <h1>홈페이지<h1>
        ```

5. allauth의 default 동작 바꿔주기 (로그인/회원가입 시 홈페이지로 리다이렉션)
    - 여러 가지 예시
        - 리다이렉션 url 변경 가능
        - username 대신 email 사용하여 로그인하도록 변경 가능
        - 로그인 실패 제한 횟수 변경 가능
        - allauth configuration 관련 docs 확인
            - https://django-allauth.readthedocs.io/en/latest/configuration.html
    - 프로젝트 파일 `settings.py`에 allauth 관련 코드를 추가해주면 됨
        - url name("index")을 사용하여 간단하게 변경 가능!
        ```py
        ACCOUNT_SIGNUP_REDIRECT_URL = "index"
        LOGIN_REDIRECT_URL = "index"
        ```
    - ❗주의❗
        - allauth는 회원가입을 하면 자동으로 login된 상태 유지(default)
        