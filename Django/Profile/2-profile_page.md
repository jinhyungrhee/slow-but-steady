# 프로필 페이지 구현하기

- TODO
  - 프로필 페이지 구현
    - 유저의 프로필 정보 뿐만 아니라 유저가 최근에 작성한 리뷰도 함께 보여줌(최대 4개)
  - 리뷰 상세 페이지의 작성자 부분을 작성자의 프로필 페이지로 연결
  - 네비게이션 바에 '내 프로필' 버튼(링크) 생성

- 프로필 페이지 URL 정의
  - coplate/urls.py
    ```py
    urlpatterns = [
        # 프로필 페이지
        path("users/<int:user_id>", views.ProfileView.as_view(), name="profile"),
    ]
    ```
    - url 정의 부분(urls.py)에서 'user_id'라는 이름으로 parameter를 넘겨주도록 지정

- 프로필 뷰 정의
  - coplate/views.py
    ```py
    # 프로필 뷰 정의 - DetailView 사용
    class ProfileView(DetailView):
        model = User
        template_name = "coplate/profile.html"
        pk_url_kwarg = "user_id"
        context_object_name = "profile_user"
        # 결과: user id에 해당하는 유저는 'profile_user'라는 이름으로 템플릿에 전달됨!

        # 유저가 최근에 작성한 리뷰 보여주기 -> 리뷰들을 템플릿으로 전달되는 context에 추가(get_context_data() 오버라이딩)
        def get_context_data(self, **kwargs):
            # 1)기본적으로 전달되는 context 가져오기
            context = super().get_context_data(**kwargs)
            # 2)유저가 작성한 리뷰 가져오기
            user_id = self.kwargs.get("user_id") # 유저id는 url에서 가져옴(url로 전달되는 parameter는 'self.kwargs'로 접근 가능)
            context["user_reviews"] = Review.objects.filter(author__id=user_id).order_by("-dt_created")[:4]
            return context
            # 결과: "user_reviews"라는 이름으로 가장 최근 리뷰 4개가 템플릿에 전달됨!
    ```
    - `pk_url_kwarg = "user_id"` : url 정의 부분(urls.py)에서 'user_id'로 넘겨주었기 때문에, 여기서도 "user_id"로 받아주는 것
    - `context_object_name = "profile_user"`
      - context_object_name을 따로 지정하지 않으면 디폴트 값인 'user'로 사용됨
      - 하지만 'user'는 항상 현재 유저를 참조하는데 사용되기 때문에 충돌 방지를 위해 'profile_user'로 지정함
      - **즉, user_id에 해당하는 유저는 'profile_user'라는 이름으로 템플릿에 전달됨!**
    - ` get_context_data()` 오버라이딩
      - 유저가 최근에 작성한 리뷰 보여주기 위해, 리뷰들을 템플릿으로 전달되는 context에 추가해줘야 함
        - ⭐ **템플릿으로 전달되는 context에 추가 데이터 넣기 위해 get_context_data() 오버라이딩 필요!** ⭐
      - `context = super().get_context_data(**kwargs)` : 기본적으로 전달되는 context를 가져옴. 이때 context는 '딕셔너리' 형태임!
      - `user_id = self.kwargs.get("user_id")` : url로부터 유저 id를 가져옴(⭐**url로 전달되는 parameter는 'self.kwargs'를 통해 접근 가능**⭐)
      - `context["user_reviews"] = Review.objects.filter(author__id=user_id).order_by("-dt_created")[:4]`
        - filter(author__id=user_id) : 현재 유저 id와 작성자 id가 같은 리뷰들만 필터링함
        - order_by("-dt_created") : -'를 붙여서 생성일 기준 내림차순(=최신순)으로 정렬
        - [:4] : 앞에서부터 4개의 항목만 가져옴
        - 결과 : **"user_reviews"라는 이름으로 가장 최근 리뷰 4개가 템플릿에 전달됨!**

- 프로필 템플릿 정의
  - templates/coplate/profile.html
    ```html
    {% extends "coplate_base/base_with_navbar.html" %} 

    {% load static %} 

    {% block title %}{{ profile_user.nickname }} | Coplate{% endblock title %} 

    {% block content %}

    <main class="site-body">
      <div class="profile-header">
        <div class="content max-content-width">
          <!-- 'profile_user'로 view에서 template으로 전달됨 -->
          <div class="cp-avatar large profile-pic" style="background-image: url('{{ profile_user.profile_pic.url }}')"></div>
          <div class="info">
            <h1 class="username"> {{ profile_user.nickname }} </h1>
            <!-- 소개문구가 있는 경우에만 보이도록 if문 추가 -->
            {% if profile_user.intro %}
            <div>
              <p class="cp-chip intro"> {{ profile_user.intro }} </p>
            </div>
            {% endif %}
          </div>
        </div>
      </div>

      <div class="content-list max-content-width">
        <div class="header">
          <h2>{{ profile_user.nickname }}님의 최신 리뷰</h2>
          <a class="cp-ic-button after circle morereview" href="#">
            리뷰 전체보기
          </a>
        </div>

        <div class="contents">
          <!-- view에서 리뷰들을 'user_reviews' 이름으로 context안에 담아서 전달 -->
          {% for review in user_reviews %}
          <a href="{% url 'review-detail' review.id %}">
            <div class="cp-card content">
              <div
                class="thumb"
                style="background-image: url('{{ review.image1.url }}');"
              ></div>
              <div class="body">
                <span class="cp-chip green">{{ review.restaurant_name }}</span>
                <h2 class="title">{{ review.title }}</h2>
                <date class="date">{{ review.dt_created|date:"Y년 n월 j일" }}</date>
                <div class="metadata">
                  <div class="review-rating">
                    <span class="cp-stars">
                      {% for i in ""|ljust:review.rating %}★{% endfor %}
                    </span>
                  </div>
                  <div class="review-author">
                    <div
                      class="cp-avatar"
                      style="background-image: url('{{ review.author.profile_pic.url }}')"
                    ></div>
                    <span>{{ review.author.nickname }}</span>
                  </div>
                </div>
              </div>
            </div>
          </a>
          {% empty %}
          <p class="empty">아직 리뷰가 없어요 :(</p>
          {% endfor %}
        </div>
      </div>
    </main>
    {% endblock content %}
    ```

- 리뷰 상세 페이지의 닉네임과 프로필 페이지 연결
  - templates/coplate/review_detail.html
    ```html
    {% block content %}
    <main class="site-body">
      <article class="review-detail max-content-width">
        <div class="review-info">
          <div class="restaurant-name">
            <span class="cp-chip green">{{ review.restaurant_name }}</span>
          </div>
          <h1 class="title">{{ review.title }}</h1>
          <div class="author">
            <!-- 프로필 페이지 url 연결 - 어떤 유저의 프로필인지 알아야 하므로 parameter(=review.author.id) 추가 -->
            <a class="review-author" href="{% url 'profile' review.author.id %}">
              <div class="cp-avatar" style="background-image: url('{{ review.author.profile_pic.url }}')"></div>
              <span> {{ review.author.nickname }} </span>
            </a>
          </div>
          <date class="date">{{ review.dt_created|date:"Y년 n월 j일" }}</date>
          <div class="review-rating">
            <span class="cp-stars">
              {% for i in ""|ljust:review.rating %}
                ★
              {% endfor %}
            </span>
          </div>
        </div>
    ```

- '내 프로필' 버튼을 네비게이션 바에 추가
  - 유저가 로그인 되어 있을때만 보여주도록 설정
  - templates/coplate_base/base_with_navbar.html
    ```html
    {% block header %}
    <header class="site-header navbar">
      <div class="content max-width">
        <a href="{% url 'index' %}">
          <img class="logo" src="{% static 'coplate/assets/coplate-logo.svg' %}" alt="Coplate Logo">
        </a>
        <nav>
          <ul class="navbar">
            {% if user.is_authenticated %}
              <!-- 로그인 되어 있을 때 -->
              <!-- 프로필 페이지는 유저id가 파라미터로 필요함 -->
              <li><a href="{% url 'profile' user.id %}">내 프로필</a></li>
              <li><a href="{% url 'account_logout' %}">로그아웃</a></li>
            {% else %}
              <!-- 로그인 되어 있지 않을 때 -->
              <li><a href="{% url 'account_login' %}">로그인</a></li>
              <li><a href="{% url 'account_signup' %}">회원가입</a></li>
            {% endif %}
          </ul>
        </nav>
      </div>
    </header>
    {% endblock header %}
    ```