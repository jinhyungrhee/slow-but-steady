# allauth 유용한 세팅들

- allauth 전용 세팅은 모두 ACCOUNT로 시작함
  - 그 외는 모두 일반 django 세팅
- 모든 세팅은 프로젝트 파일 내의 settings.py에 추가하면 됨!

|세팅|값|디폴트 값|설명|
|--|--|--|--|
|ACCOUNT_AUTHENTICATION_METHOD|"username", "email", "username_email"|"username"|로그인 방법 설정 : 유저네임 사용("username"), 이메일 사용("email"), 둘다 사용 가능("username_email")|
|ACCOUNT_CONFIRM_EMAIL_ON_GET|True, False|False|이메일 인증 링크를 클릭하면 바로 인증됨(True), 이메일 인증 링크를 클릭하면 인증 confirmation 페이지로 이동(False)|
|ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL|URL(URL 경로, URL 네임 모두 가능)|LOGIN_URL (아래 참고)|로그인이 안된 상태로 인증을 완료했을 때 리디렉트되는 URL|
|ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL|URL (URL 경로, URL 네임 모두 가능)|LOGIN_REDICRECT_URL (아래 참고)|로그인이 된 상태로 인증을 완료했을 때 리디렉트되는 URL|
|ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS|이메일 인증 링크 만료 기간 (단위: 일)|3|이메일 인증 링크 만료 기간|
|ACCOUNT_EMAIL_REQUIRED|True, False|False|회원가입 시 이메일을 꼭 입력해야 하는지 결정 : 이메일을 반드시 입력(True), 이메일을 선택적으로 입력(False)|
|ACCOUNT_EMAIL_VERIFICATION|"mandatory", "optional", "none"|"optional"|이메일 인증 필요 여부 설정 : 회원가입 시 인증 메일 발송 & 인증 완료 후 로그인 가능(mandatory), 회원가입 시 이메일 인증 발송 & 인증 필수X(optional), 회원가입 시 인증 메일 발송X(none)|
|ACCOUNT_LOGIN_ATTEMPTS_LIMIT|최대 로그인 실패 횟수|5|최대 로그인 실패 횟수|
|ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT|로그인이 잠기는 기간 (단위: 초)|300|로그인 시도가 ACCOUNT_LOGIN_ATTEMPTS_LIMIT을 초과하면 설정하는 시간만큼 로그인이 잠김|
|ACCOUNT_LOGOUT_ON_GET|True, False|False|로그아웃 링크를 클릭하면 바로 로그아웃(True), 로그아웃 링크를 클릭하면 로그아웃 confirmation 페이지로 이동(False)|
|ACCOUNT_LOGOUT_REDIRECT_URL|URL (URL 경로, URL 네임 모두 가능)|"/"|로그아웃 시 리디렉트되는 URL|
|ACCOUNT_PASSWORD_INPUT_RENDER_VALUE|True, False|False|폼 유효성 검사를 실패한 경우, 입력했던 비밀번호가 채워진 상태로 폼이 돌아오는지 설정|
|ACCOUNT_SESSION_REMEMBER|None, True, False|None|브라우저를 닫으면 유저를 로그아웃 시킬지 결정 : 유저가 체크박스를 통해 선택(None), 브라우저를 닫아도 로그인 유지(True), 브라우저를 닫으면 로그아웃(False)|
|ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE|True, False|False|회원가입 시 이메일을 두 번 입력해야 하는지를 설정|
|ACCOUNT_SIGNUP_FORM_CLASS|폼 클래스 (e.g. 'myapp.forms.SignupForm')|None|회원가입 페이지에서 추가 정보를 받아야 할 때, 사용할 폼 클래스를 지정|
|ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE|True, False|False|회원가입 시 비밀번호를 두 번 입력해야 하는지를 설정|
|ACCOUNT_SIGNUP_REDIRECT_URL|URL (URL 경로, URL 네임 모두 가능)|LOGIN_REDIRECT_URL (아래 참고)|회원가입 성공 시 리디렉트되는 URL|
|ACCOUNT_USERNAME_REQUIRED|True, False|True|회원가입 시 유저네임을 입력해야 하는지 결정 : 유저네임 입력O(True), 유저네임 입력X(False)|
|LOGIN_REDIRECT_URL|URL (URL 경로, URL 네임 모두 가능)|'/accounts/profile/'|성공적인 로그인 시 리디렉트되는 URL|
|LOGIN_URL|URL (URL 경로, URL 네임 모두 가능)|'/accounts/login/'|웹사이트의 로그인 URL(뷰 접근 제어:Decorator, Mixin 강의 참고)|
|PASSWORD_RESET_TIMEOUT|비밀번호 재설정 링크 만료 기간 (단위: 초)|259200 (3일)|비밀번호 재설정 링크 만료 기간 (Django 3.1 이후 버전)|
|PASSWORD_RESET_TIMEOUT_DAYS|비밀번호 재설정 링크 만료 기간 (단위: 일)|3|비밀번호 재설정 링크 만료 기간 (Django 3.0 이전 버전)|
|SESSION_COOKIE_AGE|세션 쿠키 만료 기간 (단위: 초)|1209600 (2주)|세션 쿠키 만료 기간 (로그인을 얼마나 오랫동안 유지할 것인지 결정)|

- 기타 세팅들
  - https://django-allauth.readthedocs.io/en/latest/configuration.html