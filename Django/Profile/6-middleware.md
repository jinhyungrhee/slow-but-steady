# Middleware 활용하기

## Middleware

- Request와 Response 사이클을 제어하는 역할
- 뷰 하나에만 적용되는 Mixin과 달리, Middleware는 **뷰 컴포는트 전체에 적용**됨
- 모든 Request는 URL Dispatcher에 도착하기 전에 항상 Middleware를 먼저 통과함
- Middleware에는 다양한 로직을 넣을 수 있음
  - ① Mixin처럼 Request를 다음 컴포넌트(= 뷰)로 전달
  - ② Request를 다음 컴포넌트로 전달하지 않고 바로 Response를 돌려줌
  - ③ Request를 그대로 전달하지 않고 프로세싱한 뒤 다음 컴포넌트로 전달 (`Request 프로세싱`)
    - Request에 추가 정보를 더하거나, Request 정보를 수정할 수 있음!
  - ④ 뷰에서 리턴되는 Response도 프로세싱 가능 (`Response 프로세싱`)
    - Response에 추가 정보를 더하거나, Response 정보를 수정할 수 있음!

- django는 기본적으로 여러 가지 middleware를 사용함
  - coplate_project/settings.py
    ```py
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        # AuthenticationMiddleware가 모든 request에 user속성(=현재 유저 정보) 추가해줌
        # 결과 : View에서 현재 유저를 'request.user'로 접근 가능!
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ```
    - 이처럼 전체적인 request에 대한 로직은 middleware에서 구현
    - `request` : 상위 미들웨어부터 하위 미들웨어로 통과
    - `response` : 하위 미들웨어부터 상위 미들웨어로 통과

- django middleware 공식 문서
  - https://docs.djangoproject.com/en/2.2/topics/http/middleware/
  - 함수형 미들웨어와 클래스형 미들웨어 존재
  - 클래스형 미들웨어 틀
    ```py
    class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    ```

## 유저가 프로필을 설정하지 않고 다른 페이지로 이동하는 것 방지

- 아직 프로필 설정을 하지 않은 경우, 항상 프로필 설정 페이지로 리디렉트하는 방법
  - url과 상관없이 리디렉트를 하고 싶기 때문에 Middleware 사용
  - 조건 : `로그인 돼있음` + `프로필 작성하지 않음` + `프로필 설정 페이지가 아닌 다른 페이지로 request를 보냄` → **프로필 설정 페이지로 리디렉트**

- 앱 디렉토리 안에 middleware 파일 생성 (= middleware 정의)
  - coplate/middleware.py
    ```py
    from django.urls import reverse
    from django.shortcuts import redirect

    class ProfileSetupMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        # request를 프로세싱해주는 부분
        def __call__(self, request):
            # 프로필 설정 페이지로 가게 되는 조건 설정
            if (
              request.user.is_authenticated and # 유저가 로그인 되어있는지 확인
              not request.user.nickname and  # 유저의 닉네임이 None이 아닌지(= 프로필 설정을 했는지) 확인
              request.path_info != reverse("profile-set") # 유저가 프로필 설정 페이지가 아닌 다른 페이지로 request보냈는지 확인
              # request url 경로는 'path_info'를 통해 확인 가능
            ):
              # 위 조건을 모두 충족하면, 프로필 페이지로 리디렉트!
              return redirect("profile-set")

            # 위 조건들이 해당하지 않으면 request가 평소처럼 처리됨!
            response = self.get_response(request)

            return response
    ```

- 작성한 Middleware를 settings파일에 추가
  - coplate_project/settings.py
    ```py
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        # AuthenticationMiddleware : ProfileSetupMiddleware 앞에 위치!
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # 작성한 Middleware 추가!
        # ProfileSetupMiddleware : AuthenticationMiddleware 뒤에 위치!
        'coplate.middleware.ProfileSetupMiddleware',
    ]
    ```
    - ❗주의❗ 우리가 작성한 미들웨어(ProfileSetupMiddleware)는 반드시 AuthenticationMiddleware 다음에 나와야 함
      - ProfileSetupMiddleware 코드 안에서 `request.user`를 사용하는데, 이는 AuthenticationMiddleware를 거쳐야지만 설정되기 때문!