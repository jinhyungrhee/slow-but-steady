# 홈페이지 구현하기

- 페이지 만들 때 일반적인 순서
  - URL → View → Template

## 홈페이지에 대한 URL

- coplate/urls.py
  ```py
  urlpatterns = [
      # 제네릭 뷰 사용
      path("", views.IndexView.as_view(), name="index"),
  ]
  ```

## 홈페이지에 대한 View
- 어떤 Model에 대한 CRUD 기능 구현 시 django의 `제네릭 뷰` 사용
- `제네릭 뷰` : 웹 개발에서 가장 흔히 쓰이는 View 로직 몇 가지를 미리 구현해서 View 형태로 만들어 놓은 것
- 종류
  - Create : `CreateView`
  - Read : `DetailView`, `ListView`
  - Update : `UpdateView`
  - Delete : `DeleteView`
- ListView 사용 (coplate/views.py)
    ```py
    # Review 모델 가져오기
    from coplate.models import Review
    # 리스트뷰 가져오기
    from django.views.generic import ListView

    # 제네릭뷰(ListView) 사용
    class IndexView(ListView):
        model = Review
        template_name = "coplate/index.html"
        context_object_name = "reviews"
        # 모든 Review를 가져와서 템플릿에 넘길 때, context의 이름은 'reviews'임
        paginate_by = 4
        # 한 페이지에 4개씩 보여줌
        ordering = ["-dt_created"]
        # 보여주는 순서는 최신순으로 보여줌(생성일을 기준으로 내림차순(-)으로 정렬) **
    ```

## 홈페이지에 대한 Template

- 모든 웹 페이지는 coplate_base 템플릿 중 하나를 상속받음
  - `base.html` : 아무것도 없는 템플릿
  - `base_with_header.html` : 로고가 포함된 헤더가 있는 헤더 템플릿
  - `base_with_navbar.html` : navbar와 footer가 포함된 템플릿
- 네비게이션 바 연결
  - coplate_base/base_with_navbar.html
    ```html
    {% block header %}
    <header class="site-header navbar">
      <div class="content max-width">
        <a href="{% url 'index' %}"> <!-- 연결 -->
          <img class="logo" src="{% static 'coplate/assets/coplate-logo.svg' %}" alt="Coplate Logo">
        </a>
        <nav>
          <ul class="navbar">
            {% if user.is_authenticated %}
              <li><a href="{% url 'account_logout' %}">로그아웃</a></li> <!-- 연결 -->
            {% else %}
              <li><a href="{% url 'account_login' %}">로그인</a></li> <!-- 연결 -->
              <li><a href="{% url 'account_signup' %}">회원가입</a></li> <!-- 연결 -->
            {% endif %}
          </ul>
        </nav>
      </div>
    </header>
    {% endblock header %}
    ```

- for문을 사용하여 리뷰 반복 출력(ListView)
  - 장고 템플릿에서 파이썬의 `for i in range():`를 사용하는 방법! : `ljust필터` 사용!
    - `ljust필터` : 앞에 오는 문자열 뒤에 공백을 추가해서 항상 명시된 숫자만큼의 길이가 되도록 만들어줌
      ```html
      {% for i in ""|ljust:review.rating %}★{% endfor %}
      ```

  - empty 예외 처리 : `for-empty문` 사용!
    ```html
    {% for review in reviews %}
      ...
    {% empty %} <!--reviews가 존재하지 않거나 비어있다면 이 부분이 display됨! -->
        <p class="empty">아직 리뷰가 없어요 :(</p>
    {% endfor %}
    ```

  - 전체 코드
    ```html
    <div class="contents">
    {% for review in reviews %} <!-- View에서 넘겨준 reviews에서 하나씩 가져옴-->
      <a href="#">
        <section class="cp-card content">
          <div class="thumb" style="background-image: url('{{ review.image1.url }}');"></div> <!--image1 필드 연결-->
          <div class="body">
            <span class="cp-chip green">{{ reveiw.restaurant_name }}</span>
            <h2 class="title">{{ review.title }}</h2>
            <date class="date">{{ reveiw.dt_created|date:"Y년 n월 j일" }}</date> <!--날짜 formatting 필요-->
            <div class="metadata">
              <div class="review-rating">
                <span class="cp-stars">
                  {% for i in ""|ljust:review.rating %}★{% endfor %}
                </span>
                <!-- 장고 템플릿 문법에는 range()가 없음 -->
                <!-- 길이가 rating 길이인 문자열을 만들고 그것을 반복문에 사용 : ljust필터 사용 -->
              </div>
              <div class="review-author">
                <span> {{ review.author.nickname }} </span> <!--닉네임 가져오기-->
              </div>
            </div>
          </div>
        </section>
      </a>
    {% empty %}
      <p class="empty">아직 리뷰가 없어요 :(</p>
    {% endfor %}
    </div>
    ```
    - 날짜 formatting 참고 : https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#date