# 프로필 설정 페이지 구현하기

- 개요
  - 유저가 프로필을 설정하고 수정하는 기능 구현
  - 1)프로필 설정 페이지
    - 회원가입 후 프로필을 설정할 수 있는 '프로필 설정 페이지' 구현
    - 프로필 사진, 닉네임, 소개문구를 설정하는 페이지
      - 닉네임도 프로필 정보기 때문에 아예 '프로필 설정 페이지'로 옮김!
    - 사용자가 회원가입을 하면, 홈페이지 대신 '프로필 설정 페이지'로 안내(=리디렉트)를 해서 프로필을 설정할 수 있도록 프로세스 설계
  - 2)프로필 수정 페이지
    - 원할 때는 언제든 프로필을 수정할 수 있도록 '프로필 수정 페이지' 구현

## 프로필 설정 기능 구현

- 프로필 설정 페이지 URL 작성
  - coplate/urls.py
    ```py
    urlpatterns = [
        # 프로필 설정 페이지
        path(
            "set-profile/", # url 경로 설정(자신(현재 로그인된 유저)의 프로필을 수정하는 것이므로 user_id 필요 없음)
            views.ProfileSetView.as_view(), # 뷰 설정
            name="profile-set" # url name 설정
        ),
    ]
    ```

- Form 작성
  - coplate/forms.py
    ```py
    # 프로필 설정 시 사용되는 Form
    class ProfileForm(forms.ModelForm):
      class Meta:
        # 모델과 사용할 필드 지정
        model = User
        fields = [
          "nickname",
          "profile_pic",
          "intro",
        ]
        # 'intro'필드는 CharField이기 때문에 기본적으로 한줄짜리 text Input이 사용됨
        # text Input 보다 더 큰 TextArea 사용 -> widgets으로 설정
        widgets = {
          "intro" : forms.Textarea, 
        }
    ```

- ProfileSetView 뷰 작성
  - coplate/views.py
    ```py
    from coplate.forms import ProfileForm
    ...
    # 프로필 설정 View - '수정'제네릭뷰인 UpdateView 사용
    class ProfileSetView(UpdateView):
        model = User
        form_class = ProfileForm
        template_name = "coplate/profile_set_form.html"
        # UpdateView는 어떤 object를 update할 것인지 알아야 함
        # 일반적인 경우: update할 object_id가 url로 전달되면, 그것을 pk_url_kwargs를 사용해서 설정함
        # 하지만 이 경우에는 update할 object_id가 url로 전달되지 않음! -> 단순히 update할 유저는 현재 들어와 있는 유저임!
        # get_object() 오버라이딩 : update할 object를 UpdateView에 알려주는 메서드
        # get_object() 메서드는 ListView의 get_queryset() 메서드와 유사함
        # - ListView는 여러 object를 다루기 때문에 get_queryset() 메서드를 오버라이드함
        # - UpdateView는 하나의 object를 다루기 때문에 get_object() 메서드를 오버라이드함
        #   - 하나의 object를 다루는 DetailView, CreateView, DeleteView도 get_object() 메서드를 오버라이드함
        def get_object(self, queryset=None):
            # 여기에서 현재 유저를 리턴함(<클래스형 뷰>에서는 현재 유저를 'self.request.user'로 접근)
            return self.request.user
        # *UpdateView는 항상 update 후에 리디렉트할 url을 적어줘야 함*
        def get_success_url(self):
            return reverse("index")
    ```


## 회원가입 페이지에서 닉네임 필드 제거

- cf) allauth에서 제공하는 signup 페이지에 어떠한 필드(=닉네임 필드) 추가하는 방법
  - forms.py 안의 SignupForm 클래스에 추가 필드에 대한 폼을 생성
    ```py
    # coplate/forms.py
    
    class SignupForm(forms.ModelForm):
      class Meta:
        model = User # 사용할 모델 정의
        fields = ["nickname"] # 사용할 필드 정의
      # signup 함수 정의
      def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()
    ```
  - 프로젝트 파일의 settings.py에서 'ACCOUNT_SIGNUP_FORM_CLASS'에 우리가 만든 폼 클래스를 지정 
    ```py
    # coplate_project/settings.py

    # SignupForm 추가
    ACCOUNT_SIGNUP_FORM_CLASS = "coplate.forms.SignupForm"
    ```

- 더 이상 닉네임 필드가 필요 없으므로 SignupForm 클래스와 settings.py의 해당 세팅을 코멘트 처리
  
  - coplate/forms.py
    ```py
    #class SignupForm(forms.ModelForm):
    #  class Meta:
    #    model = User # 사용할 모델 정의
    #    fields = ["nickname"] # 사용할 필드 정의
    #  # signup 함수 정의
    #  def signup(self, request, user):
    #    user.nickname = self.cleaned_data['nickname']
    #    user.save()
    ```

  - coplate_project/settings.py
    ```py
    #ACCOUNT_SIGNUP_FORM_CLASS = "coplate.forms.SignupForm"
    ```

- 회원가입 템플릿에서 닉네임 필드 코멘트 처리
  - templates/account/signup.html
    ```html
    ...
    {% comment %}
      <div>
        <!-- 필드에 오류가 있을 때 에러 클래스 추가 : add_error_class:"error" -->
        {{ form.nickname|add_class:"cp-input"|attr:"placeholder:닉네임 (Coplate에서 사용되는 이름입니다)"|add_error_class:"error"}}
        <!-- 여러 에러 처리 : form.필드.errors 항목에서 하나씩 가져와서 보여줌 -->
        {% for error in form.nickname.errors %}
        <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
    {% endcomment %}
    ...
    ```

## 회원가입 페이지에서 '회원가입' 버튼을 클릭하면 '프로필 설정 페이지'로 이동하도록 설정

- coplate_project/settings.py
  ```py
  # 회원가입 완료 후 리디렉션 될 url
  ACCOUNT_SIGNUP_REDIRECT_URL = "profile-set"
  ```

## 프로필 설정 페이지 템플릿 설정

- 프로필 설정 페이지 Template
  - templates/coplate/profile_set_form.html
    ```html
    {% extends "coplate_base/base.html" %}

    {% load static %}
    {% load widget_tweaks %}

    {% block title %}환영합니다! | Coplate{% endblock title %}

    {% block content %}
    <div class="account-background">
      <main class="profile-form">
        <!-- coplate 로고와 환영 문구 -->
        <div class="logo">
          <img class="logo" src="{% static 'coplate/assets/coplate-logo.svg' %}" alt="Coplate Logo">
        </div>
        <p class="welcome-message">
          환영합니다! <strong>프로필</strong>을 작성해주세요
        </p>
        <!-- 파일 업로드가 있는 폼 태그 -->
        <form method="post" enctype="multipart/form-data" autocomplete="off">
          {% csrf_token %}
          <!-- 프로필 사진 필드 -->
          <div class="profile">
            <!-- 유저의 현재 프로필 사진을 넣어줌 -> 유저가 생성되면 기본 이미지 파일이 생성됨 -->
            <!-- 주의: 모델 유효성 검사에 의해 포맷 오류가 발생하면, 파일은 다시 한 번 업로드 해줘야 함! -->
            <div class="profile-pic cp-avatar large" style="background-image: url('{{ user.profile_pic.url }}')"></div>
            <div class="file">
              {{ form.profile_pic }}
            </div>
          </div>
          <!-- 닉네임 필드 -> 이전에 사용했던 닉네임 필드에 대한 유효성 검사도 그대로 적용됨 -->
          <!-- 유효성 검사는 Model의 nickname 필드에 추가해주었고, 지금 Model Form을 사용하고 있기 때문!-->
          <div class="nickname">
            {{ form.nickname|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:닉네임" }}
            {% for error in form.nickname.errors %}
              <div class="error-message">{{ error }}</div>
            {% endfor %}
          </div>
          <!-- 소개문구 필드 -->
          <div class="content">
            {{ form.intro|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:자신을 소개해 주세요!" }}
            {% for error in form.intro.errors %}
              <div class="error-message">{{ error }}</div>
            {% endfor %}
          </div>
          <div class="buttons">
            <button class="cp-button" type="submit">완료</button>
          </div>
        </form>
      </main>
    </div>
    {% endblock content %}
  
    ```

## 문제1) 로그인하지 않은 유저가 프로필 설정 url로 접근하지 못하도록 제어하기

- 로그인되지 않은 유저가 url을 통해 프로필 설정 페이지에 접근할 경우, django는 에러 메시지 창을 리턴함
  - 접근
    ```
    http://127.0.0.1:8000/set-profile/
    ````
  - 결과
    ```
    AttributeError at /set-profile/ 
    'AnonymousUser' object has no attribute '_meta'.
    ...
    ```

- 해결방법) 프로필 설정 뷰에 접근하는 것 제어하기 : `Mixin 사용`
  - coplate/views.py
    ```py
    # 뷰 접근 제어 : Mixin 사용
    class ProfileSetView(LoginRequiredMixin, UpdateView):
        model = User
        form_class = ProfileForm
        template_name = "coplate/profile_set_form.html"
        
        def get_object(self, queryset=None):
            return self.request.user

        def get_success_url(self):
            return reverse("index")
    ```
  - 결과
    - 로그인하지 않은 상태에서 `http://127.0.0.1:8000/set-profile/`로 접근 시, 로그인 페이지로 리디렉트 됨
      - 결과 url : `http://127.0.0.1:8000/login/?next=/set-profile/`

## 문제2) 유저가 프로필을 설정하지 않고 다른 페이지로 이동하는 것 방지

- 유저가 '회원가입 페이지'에서 '프로필 설정 페이지'로 이동한 뒤, 프로필 설정을 완료하지 않고 url을 이용해 '홈페이지'로 이동하지 못하도록 제한
  - 이 경우 프로필 페이지에 닉네임이 None으로 나타남

- 해결방법
  - ① 회원가입 시 default로 닉네임을 정해주는 방법
  - ② 아직 프로필 설정을 하지 않은 경우, 항상 프로필 설정 페이지로 리디렉트하는 방법 ✔
    - Middleware 활용!