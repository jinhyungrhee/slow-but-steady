# 리뷰 상세(조회) 페이지 구현하기

- 리뷰 상세 페이지 URL 설정
  - coplate/urls.py
    ```py
    urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        # 상세 리뷰 페이지
        path(
            "reveiws/<int:review_id>/",       # 리뷰 id에 해당하는 리뷰를 보여주는 경로
            views.ReviewDetailView.as_view(), # ReveiwDetailView 사용
            name="review-detail",             # 이름 지정
        ),
    ]
    ```
    - coplate/views.py에 `ReviewDetailView` 구현 필요!

- `ReviewDetailView` 뷰 구현
  - coplate/views.py
    ```py
      # 제네릭으로부터 DetailView 가져옴
      from django.views.generic import DetailView

      # 제네릭의 DetailView 가져와서 ReviewDetailView 작성!
      class ReviewDetailView(DetailView):
          model = Review
          template_name = "coplate/review_detail.html"
          # 리뷰id로 사용되는 이름을 DetailView에 알려줌('pk_url_kwarg' 사용!)
          pk_url_kwarg = "review_id"
          # object를 하나만 다루는 view에서는 'context_object_name'의 default값이 모델의 이름(=Review)이 됨! -> 작성 필요X
      ```
  
- 홈페이지에서 리뷰 상세 페이지로 가는 링크 채우기
  - templates/coplate/index.html
    ```html
    <div class="content-list max-content-width">
    <div class="header">
      <h2>리뷰 목록</h2>
      <a class="cp-ic-button circle newreview" href="#">리뷰 작성</a>
    </div>

      <div class="contents">
      {% for review in reviews %}
         <!-- url에 parameter가 들어가는 경우, 'urlname'을 먼저쓰고 그 뒤에 parameter(=review.id)를 하나씩 나열에주면 됨! -->
        <a href="{% url 'review-detail' review.id %}">
          <section class="cp-card content">
            <div class="thumb" style="background-image: url('{{ review.image1.url }}');"></div> 
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
                  <span> {{ review.author.nickname }} </span>
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

- 리뷰 상세 페이지 작성
  - 위치 : templates/coplate/review_detail.html
    ```html
    {% extends "coplate_base/base_with_navbar.html" %}

    {% load static %}

    {% block title %}{{ review.title }} | Coplate{% endblock title %}

    {% block content %}
    <main class="site-body">
      <article class="review-detail max-content-width">
        <div class="review-info">
          <div class="restaurant-name">
            <span class="cp-chip green">{{ review.restaurant_name }}</span>
          </div>
          <h1 class="title">{{ review.title }}</h1>
          <div class="author">
            <a class="review-author" href="#">
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

        <div class="content">
          <!-- 사진 넣기 : image1 필수, image2,3은 선택 -->
          <img class="thumb" src="{{ review.image1.url }}">
          <!-- image2,3은 있을 때만 보여주기 : if문 사용! -->
          {% if review.image2 %} 
            <img class="thumb" src="{{ review.image2.url }}">
          {% endif %}
          {% if review.image3 %}
            <img class="thumb" src="{{ review.image3.url }}">
          {% endif %}
          <p class="content">{{ review.content|linebreaksbr }}</p> <!-- 리뷰 내용|linebreaksbr 필터 : 본문의 줄바꿈을 <br>태그로 바꿔줌!-->
          <a class="location" target="_blank" href="{{ review.restaurant_link }}"> <!-- 위치에는 식당의 link를 넣어줌 -->
            <img class="cp-icon" src="{% static 'coplate/icons/ic-pin.svg' %}" alt="Pin Icon">
            <span>위치보기</span>
          </a>
        </div>

        <div class="footer">
          <a class="back-link" href="{% url 'index' %}">&lt; 목록으로</a> <!-- 홈페이지 url을 넣어줌 -->
          <div class="buttons">
            <a class="cp-button warn" href="#">삭제</a>
            <a class="cp-button secondary" href="#">수정</a>
          </div>
        </div>
      </article>
    </main>
    {% endblock content %}
    ```
  - ❗`linebreaksbr` 필터 : 본문의 줄바꿈을 \<br>태그로 바꿔주는 필터❗
