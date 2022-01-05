# 자주 사용되는 allauth URL

|URL 경로|URL 네임|설명|
|--|--|--|
|'signup/'|'account_signup'|회원가입 페이지|
|'login/'|'account_login'|로그인 페이지|
|'logout/'|'account_logout'|로그아웃 페이지(settings.py에서 ACCOUNT_LOGOUT_ON_GET=True 적용시 바로 로그아웃됨)|
|'confirm-email/'|'account_confirm_email'|이메일 인증페이지(settings.py에서 ACCOUNT_CONFIRM_EMAIL_ON_GET=True 적용시 바로 인증 완료됨)|
|'password/change/'|'account_change_password'|비밀번호 변경 페이지|
|'password/reset/'|'account_reset_password'|비밀번호 찾기 페이지(비밀번호 재설정 링크를 받을 이메일을 입력하는 페이지)|
|'password/reset/done/'|'account_reset_password_done'|비밀번호 재설정 이메일 전송 완료 페이지|
|'password/reset/key/'|'account_reset_password_from_key'|비밀번호 재설정 페이지(새 비밀번호를 설정한느 페이지)|