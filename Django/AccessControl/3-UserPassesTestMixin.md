# 이메일 인증이 완료된 유저만 리뷰 작성 가능하도록 설정

- 흐름
  - Request(`http://127.0.0.1:8000/reviews/new/`)가 들어오고 '로그인된 상태인지' 체크
    - NO : 로그인 페이지로 안내
    - YES : '이메일 인증이 완료되었는지' 체크
      - NO : 이메일 인증 메일 발송 → 이메일 인증 안내
      - YES : 리뷰 작성 페이지로 안내

- django-braces의 UserPassesTestMixin 사용
  - `UserPassesTestMixin`: 이메일 인증 여부를 확인하는 Mixin
    - 'LoginRequiredMixin'과 달리, 유저가 충족해야 하는 조건을 직접 정의 : `test_func()`
  - 접근을 제어하고 싶은 View에 mixin을 넣어주기
    - coplate/views.py
      ```py
      from braces.views import UserPassesTestMixin
      from allauth.account.models import EmailAddress # 이메일 사용
      ...
      # *주의*: AccessMixin은 반드시 제네릭 뷰 '왼쪽'에 써줘야 함 - 여러 개를 상속받는 경우, 코드가 왼쪽에서 오른쪽 순서로 진행되기 때문!
      # *순서*: 유저가 이메일 인증을 완료했는지 확인하기 전에 먼저 로그인이 되어있는지를 확인해야 함!
      class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
        ...
        # UserPassesTestMixin에서 유저가 충족해야 하는 조건 정의
        # self와 user를 parameter로 받고, user가 View에 접근할 수 있는지 없는지를 boolean값으로 리턴
        def test_func(self, user):
            # allauth는 사용자마다 여러 email을 등록하고 관리할 수 있는 기능을 제공->email 주소들은 EmailAddress 모델에 저장됨!
            # 이러한 email주소들 중에 현재 사용자(user=user)에 등록이 되어있고, 인증이 완료된 주소(verified=True)가 하나라도 있는지 확인
            return EmailAddress.objects.filter(user=user, verified=True).exists()
            # 해당 코드 자체가 boolean값을 리턴함
      ```

## 유저가 mixin을 통과하지 못했을 때 흐름을 제어하는 방법

>**사용되는 두 가지 속성**
>  - `redirect_unauthenticated_users` : 뷰 접근이 차단된 유저 중에, '로그인 되어있는 유저'와 '로그인 되어있지 않은 유저'를 다르게 처리할 것인지?
>    - True : '로그인이 안 된 유저'는 로그인 페이지로 리디렉트, '로그인 된 유저'는 `raise_exception`에 따라 처리됨! ✔
>    - False : '로그인이 안 된 유저'와 '로그인 된 유저' 모두 `raise_exception`에 따라 처리됨!
>  - `raise_exception`
>    - 이메일 인증을 안내하는 페이지로 리디렉트하는 함수 작성

- 이메일 인증이 필요하다고 보여주는 페이지 URL 추가
  - coplate_project/urls.py
    ```py
    # 뷰 접근 제어
    urlpatterns = [
        path(
            'email-confirmation-required/',
            TemplateView.as_view(template_name="account/email_confirmation_required.html"),
            name="account_email_confirmation_required",
        ), 
    ]
    ```

- confirmation_required 페이지로 리디렉트하는 함수 작성
  - `raise_exception` 속성의 값으로 넣어줄 함수임
  - coplate/functions.py
    ```py
    from django.shortcuts import redirect # 리디렉트 위해 django redirect 사용
    from allauth.account.utils import send_email_confirmation 

    # self와 request를 parameter로 받는 함수
    def confirmation_required_redirect(self, request):
      # 유저에게 이메일 발송
      send_email_confirmation(request, request.user)
      # urls.py에서 설정한 URL name을 넣어줌!
      return redirect("account_email_confirmation_required")
    ```

- 인증 이메일 오버라이딩 하기
  - 처음 회원가입시 allauth가 자동으로 보내는 인증 이메일
    - `email_confirmation_signup_message.txt`
    - `email_confirmation_signup_subject.txt`
  - 별도로 보내는 인증 이메일
    - `email_confirmation_subject.txt`
    - `email_confirmation_message.txt`
  - 오버라이딩
    - 원래 사용되는 template 파일과 똑같은 이름을 가진 파일을 account/email/ 폴더 안에 넣어주면 됨!

- View의 `raise_exception` 속성에 함수 넣어주기
  - coplate/views.py
    ```py
    # 작성한 함수 가져오기
    from coplate.functions import confirmation_required_redirect

    class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
        model = Review
        form_class = ReviewForm
        template_name = "coplate/review_form.html"

        # 유저가 mixin을 통과하지 못했을 때 흐름 제어
        redirect_unauthenticated_users = True
        raise_exception = confirmation_required_redirect

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

        def get_success_url(self):
            return reverse("review-detail", kwargs={"review_id":self.object.id})

        def test_func(self, user):
            return EmailAddress.objects.filter(user=user, verified=True).exists()
    ```
    - 흐름
      - 유저가 ReviewCreateView에 접근하려고 하면 `LoginRequiredMixin`로직과 `UserPassesTestMixin`로직이 차례대로 실행됨
      - LoginRequiredMixin는 유저가 로그인이 되어있는지 여부를 확인함
      - UserPassesTestMixin는 유저가 이메일 인증이 완료되었는지를 확인함 : `test_func()`
        - 두 가지 로직이 모두 통과되어야지만 CreateView 로직으로 넘어감!
        - 하나라도 통과하지 못했다면 `redirect_unauthenticated_users`와 `raise_exception`속성들의 값에 따라서 다음 시나리오가 결정됨
          - 로그인이 안 되어있는 유저들은 로그인 페이지로 리디렉트됨!
          - 로그인이 되어 있지만 이메일 인증이 안 되어 있는 유저들은 `raise_exception`에 설정된 함수(confirmation_required_redirect)의 로직에 따라 처리됨!
            - `confirmation_required_redirect()`함수는 유저에게 인증 이메일을 보내고, 이메일 인증이 필요하다는 페이지로 리디렉트 해줌