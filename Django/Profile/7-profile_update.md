# 프로필 수정 페이지 구현하기

- 개요
  - 프로필 설정 페이지와 거의 동일 (디자인만 약간 다름)
  - '프로필 수정' 링크는 '내 프로필' 페이지에 추가함

- 프로필 수정 페이지 URL 작성
  - coplate/urls.py
    ```py
    urlpatterns = [
        # 프로필 수정 페이지
        path(
            "edit-profile/", # url 경로 설정
            views.ProfileUpdateView.as_view(), # 사용할 뷰 설정
            name="profile-update" # # url 이름 설정
        ),
    ]
    ```

- 프로필 수정 뷰 작성
  - coplate/views.py
    ```py
    # 프로필 수정 View - 뷰 로직은 ProfileSetView와 거의 동일
    class ProfileUpdateView(LoginRequiredMixin, UpdateView):
        model = User
        form_class = ProfileForm
        template_name = "coplate/profile_update_form.html"

        def get_object(self, queryset=None):
            return self.request.user

        # 프로필 수정 후에는 그 유저의 프로필 페이지로 이동!
        def get_success_url(self):
            return reverse("profile", kwargs={"user_id": self.request.user.id})
            # url name : "profile"
            # "profile"은 user_id를 필요로 함
            # 'user_id'는 지금 요청한 유저의 id(self.request.user.id)로 넣어줌
    ```

- 프로필 수정 템플릿 작성
  - templates/coplate/profile_update_form.html
    ```html
    <!-- '환영 문구'가 없는 것만 제외하면 profile_set_form 템플릿과 동일! -->
    {% extends "coplate_base/base_with_header.html" %}

    {% load widget_tweaks %}

    {% block title %}프로필 수정 | Coplate{% endblock title %}

    {% block content %}
    <main class="profile-form">
      <form method="post" enctype="multipart/form-data" autocomplete="off">
        {% csrf_token %}
        <div class="profile">
          <div class="profile-pic cp-avatar large" style="background-image: url('{{ user.profile_pic.url }}')"></div>
          <div class="file">
            {{ form.profile_pic }}
          </div>
        </div>
        <div class="nickname">
          {{ form.nickname|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:닉네임" }}
          {% for error in form.nickname.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
        <div class="content">
          {{ form.intro|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:자신을 소개해 주세요!" }}
          {% for error in form.intro.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
        <div class="buttons">
          <!-- 취소 버튼 클릭 시, 다시 프로필 페이지로 이동-->
          <a class="cp-button secondary cancel" href="{% url 'profile' user.id %}">취소</a>
          <button class="cp-button" type="submit">완료</button>
        </div>
      </form>
    </main>
    {% endblock content %}
    ```

- 프로필 템플릿에 '프로필 수정'과 '비밀번호 변경' 링크 생성
  - templates/coplate/profile.html
    ```html
    {% block content %}
    <main class="site-body">
      <div class="profile-header">
        <div class="content max-content-width">
          <div class="cp-avatar large profile-pic" style="background-image: url('{{ profile_user.profile_pic.url }}')"></div>
          <div class="info">
            <h1 class="username"> {{ profile_user.nickname }} </h1>
            <!-- '프로필 수정', '비밀번호 변경' 링크 추가-->
            <a class="edit" href="{% url 'profile-update' %}">
              <img class="cp-icon small" src="{% static 'coplate/icons/ic-pen.svg' %}" alt="Pen Icon">
              프로필 수정
            </a>
            &#183;
            <a class="edit" href="{% url 'account_change_password' %}">
              비밀번호 변경
            </a>
            <!---->
            {% if profile_user.intro %}
            <div>
              <p class="cp-chip intro"> {{ profile_user.intro }} </p>
            </div>
            {% endif %}
          </div>
        </div>
      </div>
    ```

- 비밀번호 변경 후 리디렉트되는 페이지 지정
  - coplate/views.py
    ```py
    # 비밀번호 변경 완료 후 리디렉션 페이지 변경을 위한 뷰 정의
    # 로그인 안 된 유저가 비밀번호 변경 페이지에 접근하지 못하도록 설정 : LoginRequiredMixin
    class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):

        def get_success_url(self):
            # 비밀번호 변경 후 해당 유저의 프로필 페이지로 이동
            return reverse("profile", kwargs={"user": self.request.user.id})
    ```

- 자신의 프로필을 조회할 때만 '프로필 수정', '비밀번호 변경' 링크가 나오도록 설정
  - templates/coplate/profile.html
    ```html
    {% block content %}
    <main class="site-body">
      <div class="profile-header">
        <div class="content max-content-width">
          <div class="cp-avatar large profile-pic" style="background-image: url('{{ profile_user.profile_pic.url }}')"></div>
          <div class="info">
            <h1 class="username"> {{ profile_user.nickname }} </h1>
            <!-- 해당 프로필 페이지가 현재 로그인된 유저의 프로필 페이지일 때만 링크를 보여주도록 설정
            지금 조회하고 있는 유저가 현재 유저인지 확인! -->
            {% if profile_user == user %} 
              <a class="edit" href="{% url 'profile-update' %}">
                <img class="cp-icon small" src="{% static 'coplate/icons/ic-pen.svg' %}" alt="Pen Icon">
                프로필 수정
              </a>
              &#183;
              <a class="edit" href="{% url 'account_change_password' %}">
                비밀번호 변경
              </a>
            {% endif %}
            <!---->
            {% if profile_user.intro %}
            <div>
              <p class="cp-chip intro"> {{ profile_user.intro }} </p>
            </div>
            {% endif %}
          </div>
        </div>
      </div>
    ```