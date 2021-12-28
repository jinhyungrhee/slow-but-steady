# 현재 로그인된 유저 접근하기

- 현재 유저 정보와 로그아웃/로그인 링크 추가하기

- 현재 유저(웹사이트를 이용중인 유저) 접근하기
  - View : `request.user`
  - Template : `{{user}}`

- View에서 확인하기
  - views.py에서는 `reqeust.user`로 접근!
    ```py
    def index(request):
      print(request.user) # username 필드가 출력
      print(request.user.email) # user의 email 필드 출력
      print(request.user.is_authenticated) # login 여부 출력
      return render(request, "coplate/index.html")
    ```
  - print(reqeust.user)의 결과로 user model의 username 필드가 출력됨!
    - user model의 str메서드는 username을 리턴함
    - login이 되어있지 않으면 username 대신 AnonymousUser를 출력함
  - `request.user`를 이용하면 현재 user에 대한 모든 필드에 접근 가능!
    - `print(request.user.email)`
  - 현재 로그인되어 있는지 여부를 확인하기 위해 `is_authenticated` 속성 사용
    - `print(request.user.is_authenticated)`

- Template에서 확인하기
  - template에서는 `{{user}}`로 접근!
  - allauth의 urls.py 참고하여 작성(https://github.com/pennersr/django-allauth/blob/master/allauth/account/urls.py)
  - template/index.html
    ```html
    <navbar>
      {% if user.is_authenticated %}
        <!-- 유저가 로그인되어있으면 로그아웃 링크 보여줌-->
        <a href="{% url 'account_logout'%}">로그아웃</a>
      {% else %}
        <!-- 유저가 로그아웃 되어있으면 로그인 링크와 회원가입 링크 보여줌-->
        <a href="{% url 'account_login'%}">로그인</a>
        <a href="{% url 'account_signup'%}">회원가입</a>
      {% endif %}
    </navbar>

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
  - '로그아웃'시 페이지 이동 없이 바로 로그아웃하기
    - coplate_project/settings.py에 `ACCOUNT_LOGOUT_ON_GET = True` 추가
