# 로그인된 유저만 리뷰 작성 가능하도록 설정

- django-braces의 LoginRequiredMixin 사용
  - `LoginRequiredMixin` : View에 접근하려면 login을 필요로 하는 mixin
  - 접근을 제어하고 싶은 View에 mixin을 넣어주기
    - coplate/views.py
      ```py
      from braces.views import LoginRequiredMixin
      ...
      # *주의* : AccessMixin은 반드시 제네릭 뷰 '왼쪽'에 써줘야 함 -> 여러 개를 상속받는 경우, 코드가 왼쪽에서 오른쪽 순서로 진행되기 때문!
      class ReviewCreateView(LoginRequiredMixin, CreateView):
        ...
      ```
  - 프로젝트 setting에서 LOGIN_URL 설정
    - coplate_project/settings.py
      ```py
      # 웹 서비스의 로그인에 대한 URL 설정 -> "account_login": allauth가 제공하는 login url
      # (뷰 접근 제어: LoginRequiredMixin은 로그인이 되어있지 않은 상태면 LOGIN_URL에 설정된 로그인 페이지로 안내함)
      LOGIN_URL = "account_login"
      ```
  - 실행
    - 로그인 하지 않고 '리뷰 작성'을 누르면 로그인 페이지로 이동!
      - 이때의 url: `http://127.0.0.1:8000/login/?next=/reviews/new/`
      - 이 상태에서 성공적으로 로그인하면 next paramter의 값(`/reviews/new/`)인 리뷰 작성 url로 리디렉트되는 것!
      - 해당 페이지에서 로그인 성공시 `http://127.0.0.1:8000/reviews/new/`로 이동함!