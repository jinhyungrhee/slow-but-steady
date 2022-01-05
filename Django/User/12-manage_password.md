# 비밀번호 관리 기능

- allauth에서는 기본적으로 '비밀번호 찾기/변경/재설정' 기능 제공

- 비밀번호 `재설정`(이메일 인증 통해)
  - 비밀번호 재설정 기간 설정(default : 3일)
    - settings.py
      ```py
      # 비밀번호 재설정 인증 메일 유효기간
      PASSWORD_RESET_TIMEOUT_DAYS = 1
      ```
      - django 3.0 이전 버전에서는 PASSWORD_RESET_TIMEOUT_DAYS (단위: 일)
      - django 3.1 이후 버전에서는 PASSWORD_RESET_TIMOUT (단위: 초)


- 비밀번호 `변경`(프로필 설정 통해)
  - 홈페이지에 추가(index.html)
    ```html
    <p><a href="{% url 'account_change_password' %}"">비밀번호 변경</a></p>
    ```
  - 변경 완료 후 리디렉션 페이지 변경⭐
    - settings.py 설정만으로 해결 불가
    - allauth의 PasswordChangeView를 상속받아서 로직을 수정해야 함
      - coplate/views.py
        ```py
        # 비밀번호 변경 완료 후 리디렉션 페이지 변경을 위한 뷰 정의
        class CustomPasswordChangeView(PasswordChangeView):
            # 어떤 form이 성공적으로 처리되면 어디로 리디렉션할 것인지 정해주는 함수(오버라이딩)
            def get_success_url(self):
                return reverse("index")
        ```
    - PasswordChangeView 대신 CustomPasswordChangeView를 사용하도록 url 패턴 변경
      - coplate_project/urls.py
        ```py
        urlpatterns = [
          path('password/change/',
          CustomPasswordChangeView.as_view(), # 클래스 뷰를 쓸 때는 as_view() 사용
          name="account_password_change"
          ), 
        ]
        ```