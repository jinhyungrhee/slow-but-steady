# Decorator

- Decorator
  - 함수형 뷰에 사용
  - mixin과 유사하게 '유저가 뷰에 접근할 수 있는지'를 확인하는 로직을 뷰에 추가
  - 접근 관련 decorator는 django.contrib.auth 앱 안에 존재

- `login_required` decorator (= LoginRequiredMixin과 유사)
  - 함수형 뷰에 직접 decorator 붙이기
    - login_required decorator 사용
      ```py
      # views.py
      from django.contrib.auth.decorators import login_required
      
      @login_required
      def my_view(request):
        ...
      ```
  - URL 패턴을 정의할 때 decorator를 적용하기
    - 뷰를 decorator로 감싸줌
      ```py
      # views.py

      # 함수형 뷰
      def my_view(request):
        ...
      # 클래스형  뷰
      class YourView(View):
        ...

      # urls.py
      
      from django.contrib.auth.decorators import login_required
      from .views import my_view, YourView

      urlpatterns = [
        # 함수형 뷰
        path('my/url/', login_required(my_view), name='my_url'),
        # 클래스형 뷰
        path('your/url/', login_required(YourView.as_view()), name='your_url'),
      ]
      ```  
  ➡ 로그인이 안 되어 있는데 my_view(또는 YourView)를 접근하려고 하면, 로그인 페이지(settings 파일의 `LOGIN_URL`에 해당하는 URL)로 리디렉트됨!

- `user_passes_test` decorator (= UserPassesTestMixin과 유사)
  - 뷰에 접근하지 못하는 유저를 처리하는 로직을 커스터마이즈 할 수 없음!
    - 뷰에 접근하지 못하는 유저를 어떤 URL로 리디렉트할 것인지 지정하는 로직밖에 구현할 수 없음
    - 다른 로직이 필요하다면, 로직을 함수형 뷰 안에 직접 넣거나 클래스형 뷰를 사용해야 함
  - 자세한 사용법 : https://docs.djangoproject.com/en/2.2/topics/auth/default/#limiting-access-to-logged-in-users-that-pass-a-test