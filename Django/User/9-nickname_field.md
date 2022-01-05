# 닉네임 필드 추가하기

- user 모델의 username 필드
  - 유저 인증, 로그인에 사용되는 필드
  - 새로운 validate를 추가하거나 필드를 커스터마이징하기 어려움 -> 새로운 닉네임 필드가 필요한 이유!

- model에 nickname 필드 추가하기
  - models.py
    ```py
    class User(AbstractUser):
    # 닉네임 필드 정의
    nickname = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.email
    ```
  - 이후 변경사항에 대한 migration 적용 (makemigrations + migrate 진행) -> `makemigrations시 에러 발생`
    ```
    $ python manage.py makemigrations
    You are trying to add a non-nullable field 'nickname' to user without a default; we can't do that (the database needs something to populate existing rows).
    Please select a fix:
    
    // nickname에 넣을 default값을 설정해야 한다는 메시지지만, default값을 정해줘도 nickname이 unique해야 한다는 조건때문에 migration이 실패함!
    ```
    - 두 가지 해결책
      - ① unique=True 삭제 → default 닉네임 설정 → 어드민 페이지에서 닉네임 수정
      - ② null=True 추가 → 어드민 페이지에서 닉네임 수정 ✔
        - 닉네임 값을 회원가입 페이지에서 받으려면 일단 null=True로 설정해주어야 함
        - django allauth는 우선적으로 기본 정보가 입력된 유저를 생성하고, 그 후에 닉네임같은 추가 정보들을 채워넣음(처음부터 닉네임이 채워지지 않음)
        - models.py
          ```py
          class User(AbstractUser):
          # 닉네임 필드 정의
          nickname = models.CharField(max_length=15, unique=True, null=True)
          
          def __str__(self):
              return self.email
          ```
        - makemigrations 진행
          ```
          $ python manage.py makemigrations
          Migrations for 'coplate':
            coplate\migrations\0002_user_nickname.py
              - Add field nickname to user

          // 이때 기존 유저들의 nickname 필드는 null로 채워짐!
          ```
        - migrate 진행
          ```
          $ python manage.py migrate
          Operations to perform:
            Apply all migrations: account, admin, auth, contenttypes, coplate, sessions, sites, socialaccount
          Running migrations:
            Applying coplate.0002_user_nickname... OK

          // migration 적용 완료!
          ```

- admin 파일에서 custom fields라는 섹션 아래에 nickname field 추가하기
  - user모델에 대한 추가 필드는 기본적으로 admin 페이지에 나타나지 않기 때문에 따로 admin 페이지에 추가해주는 코드
  - admin.py
    ```py
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User

    admin.site.register(User, UserAdmin)
    UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)
    ```

> 회원가입 페이지는 서비스에 따라 요구하는 정보가 천차만별이기 때문에 폼을 커스터마이징하는 경우가 많음

- allauth에서 회원가입 form 커스터마이징 하기
  - 추가적인 field에 대한 form을 만들어줘야 함 -> coplate/forms.py 생성
    - coplate/forms.py
      ```py
      from django import forms
      from .models import User

      # ModelForm을 이용해서 SignupForm 생성
      # ModelForm은 사용할 모델만 적어주면 모델의 필드에 따라서 폼을 알아서 만들어줌!(meta클래스에 '모델'과 '추가할 필드' 명시, 기본적인 필드 명시할 필요X)
      class SignupForm(forms.ModelForm):
        class Meta:
          model = User # 사용할 모델 정의
          fields = ["nickname"] # 사용할 필드 정의

        # signup 함수 정의
        def signup(self, request, user):
          # 추가적인 필드에 대한 값 적어줌
          user.nickname = self.cleaned_data['nickname'] # form에 기입된 데이터는 cleaned_data로 가져올 수 있음(django topic 1,2 확인)
          user.save() # 저장
      ```
  - settings.py에 SignupForm 추가 
    - coplate_project/settings.py
      ```py
      # SignupForm 추가
      ACCOUNT_SIGNUP_FORM_CLASS = "coplate.forms.SignupForm"
      ```

- 홈페이지 template에 nickname 추가
  - template/index.html
    ```html
    <h1>홈페이지</h1>
    <!-- 현재 유저의 정보 홈페이지에 추가 -->

    {% if user.is_authenticated %}
      <!-- 유저가 로그인되어있으면-->
      <p>{{user}}님의 닉네임은 {{user.nickname}}입니다. </p>
    {% else %}
      <!-- 유저가 로그아웃 되어있으면-->
      <p>로그아웃된 상태입니다.</p>
    {% endif %}
    ```