# 유저 리뷰 목록 페이지 구현하기

- 유저 리뷰 목록 페이지
  - 유저의 모든 리뷰를 확인할 수 있는 페이지
  - 홈페이지의 리뷰 목록 페이지와 동일하지만 안의 컨텐츠만 달라짐

- URL 패턴 정의
  - coplate/urls.py
    ```py
    urlpatterns = [
        # 유저 리뷰 목록 페이지
        path(
            "users/<int:user_id>/reviews/", # url 설정
            views.UserReviewListView.as_view(), # 사용할 뷰 설정
            name="user-review-list" # 이름 설정
        ),
    ]
    ```

- View 정의
  - coplate/views.py
    ```py
    # 유저 리뷰 목록을 보여주는 View 정의
    class UserReviewListView(ListView):
        model = Review
        template_name = "coplate/user_review_list.html"
        # 뷰에서 템플릿으로 넘어가는 데이터의 이름 지정
        context_object_name = "user_reviews"
        # pagination 적용 (한 페이지에 4개씩)
        paginate_by = 4

        # *리스트뷰는 기본적으로 모델에 해당하는 모든 object를 템플릿으로 전달함*
        # 리스트뷰가 전달하는 object를 바꾸고 싶으면(=특정 유저가 가지고 있는 리뷰만 전달하고 싶으면) get_query_set() 오버라이딩!
        def get_queryset(self):
            # 유저의 id를 url로부터 가져오기
            user_id = self.kwargs.get("user_id")
            # filter 걸어주기
            return Review.objects.filter(author__id=user_id).order_by("-dt_created")
            # 위에서 IndexView를 정렬할 때는 'ordering'속성을 이용했지만, 메서드 안에서는 'ordering'속성이 적용되지 않음! -> 아예 쿼리셋을 정렬해서 사용!
    ```
    - 프로필 페이지의 `ProfileView(DetailView)`와의 차이점
      - `ProfileView(DetailView)`
        - ProfileView는 DetailView이기 때문에, 어떤 유저 instance 하나를 템플릿에 전달해줌
        - 그때 우리는 추가적으로 유저가 작성한 리뷰도 함께 템플릿에 전달해주고 싶었기 때문에, **get_context_data()**를 오버라이딩하여 리뷰들을 가져와서 추가 context로 넣어준 것!
      - `UserReviewListView(ListView)`
        - 말 그대로 Review 모델에 대한 ListView이기 때문에, 기본적으로 Review의 List를 템플릿으로 전달함
          - ProfileView와 달리, Review의 List를 따로 context에 추가해주지 않아도 됨!
        - 추가적으로 **get_queryset()**의 리턴값도 내부적으로 템플릿에 전달됨
          - 이 메서드를 오버라이드하여 특정 유저가 작성한 리뷰들만 리턴해줌!
        - ❗하지만❗ 현재 조회하고 있는 유저가 아직 템플릿으로 전달되고 있지 않음!
          - 지금 조회 중인 유저를 context에 추가하여 전달해야 함 : `get_context_data()` 오버라이딩

- template 파일 정의
  - templates/coplate/user_review_list.html
    ```html
    {% extends "coplate_base/base_with_navbar.html" %}
    {% load static %}
    <!-- 하드코딩 부분 : '현재 조회중인 유저'의 정보 필요! -->
    {% block title %}유저1님의 리뷰 | Coplate{% endblock title %}

    {% block content %}
    <main class="site-body">
      <div class="content-list max-content-width">
        <div class="header">
          <h2>유저1님의 리뷰 (3)</h2>
        </div>

        <!-- 리뷰 목록 부분 -->
        <div class="contents">
          <!-- View에서 설정한 context_object_name : user_reviews -->
          {% for review in user_reviews %}
            <a href="{% url 'review-detail' review.id %}">
              <div class="cp-card content">
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
                      <div class="cp-avatar" style="background-image: url('{{ review.author.profile_pic.url }}')"></div>
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

        <div class="wrap-pagination">    
          <!-- 링크 연결 시 '현재 조회중인 유저'의 정보 필요! -->
          <a class="cp-ic-button circle backbutton" href="#">프로필로 돌아가기</a>
          {% if is_paginated %}
            <ul class="pagination">
              {% if page_obj.has_previous %}
                <li><a href="?page=1">처음</a></li>
                <li><a href="?page={{ page_obj.previous_page_number }}">이전</a></li>
              {% endif %}

              {% for num in page_obj.paginator.page_range %}
                {% if page_obj.number == num %}
                  <li class="current">{{ num }}</li>
                {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
                  <li><a href="?page={{ num }}">{{ num }}</a></li>
                {% endif %}
              {% endfor %}

              {% if page_obj.has_next %}
                <li><a href="?page={{ page_obj.next_page_number }}">다음</a></li>
                <li><a href="?page={{ page_obj.paginator.num_pages }}">마지막</a></li>
              {% endif %}
            </ul>
          {% endif %}
        </div>
      </div>
    </main>
    {% endblock content %}
    ```

- 프로필 템플릿에서 링크 연결하기
  - templates/coplate/profile.html
    ```html
    ...
    <div class="content-list max-content-width">
      <div class="header">
        <h2>{{ profile_user.nickname }}님의 최신 리뷰</h2>
        <!-- 유저 리뷰 목록 페이지 연결 (parameter 필요) -->
        <a class="cp-ic-button after circle morereview" href="{% url 'user-review-list' profile_user.id %}">
          리뷰 전체보기
        </a>
      </div>
    ...
    ```

## 템플릿의 '하드코딩 부분' & '프로필로 돌아가기' 버튼 수정하기

- ❗이 부분을 수정하기 위해선 뷰에서 `get_context_data()` 메서드를 오버라이딩하여 '현재 조회하고 있는 유저'가 템플릿으로 전달되도록 해야 함❗

- UserReviewListView 뷰 수정
  - coplate/views.py
    ```py
    from django.shortcuts import render, get_object_or_404
    ...

    class UserReviewListView(ListView):
        model = Review
        template_name = "coplate/user_review_list.html"
        context_object_name = "user_reviews"
        paginate_by = 4

        def get_queryset(self):
            user_id = self.kwargs.get("user_id")
            return Review.objects.filter(author__id=user_id).order_by("-dt_created")

        # 지금 조회 중인 유저를 context에 추가하여 템플릿으로 전달하기
        def get_context_data(self, **kwargs):
            # 1)기존의 context 가져오기
            context = super().get_context_data(**kwargs)
            # 2)유저 가져와서 context에 유저 추가
            # get_object_or_404 함수가 조회한 값(=유저)을 context에 'profile_user' 키로 저장(=등록)
            context["profile_user"] = get_object_or_404(User, id=self.kwargs.get("user_id"))

            return context
    ```
    - `get_object_or_404`
      - 찾는 유저가 없으면 404오류를 발생시키는 함수
      - object를 찾을 모델('User')과 찾을 때의 조건('id=self.kwargs.get("user_id")')을 parameter로 받음
    - get_context_data() 메서드를 오버라이딩했으므로 템플릿에서는 'profile_user'를 활용하면 됨!

- template 파일 수정
  - templates/coplate/user_review_list.html
    ```html
    ...
    <!-- 하드코딩 부분 수정 -->
    {% block title %}{{ profile_user.nickname }}님의 리뷰 | Coplate{% endblock title %}

    {% block content %}
    <main class="site-body">
      <div class="content-list max-content-width">
        <div class="header">
          <!-- 유저가 작성한 리뷰의 총 개수 -->
          <!-- 쿼리셋 전체의 object 개수가 알고 싶은 경우 : {{ paginator.count }} 사용 -->
          <h2>{{ profile_user.nickname }}님의 리뷰 ({{ paginator.count }})</h2>
        </div>

    ...

    <!-- '프로필로 돌아가기'버튼 링크 연결 시에도 '현재 조회중인 유저'의 정보 필요함! -->
    <div class="wrap-pagination">    
      <a class="cp-ic-button circle backbutton" href="{% url 'profile' profile_user.id  %}">프로필로 돌아가기</a>
      {% if is_paginated %}
        <ul class="pagination">
          {% if page_obj.has_previous %}
            <li><a href="?page=1">처음</a></li>
            <li><a href="?page={{ page_obj.previous_page_number }}">이전</a></li>
          {% endif %}
    ...
    ```

## '리뷰 전체보기' 버튼이 작성한 리뷰가 있는 경우에만 보이기

- 프로필 template 파일 수정
  - templates/coplate/profile.html
    ```html
    ...
    <div class="content-list max-content-width">
    <div class="header">
      <h2>{{ profile_user.nickname }}님의 최신 리뷰</h2>
      <!-- if문 사용하여 리뷰가 있을 경우에만 해당 버튼 보여주기-->
      {% if user_reviews %} 
        <a class="cp-ic-button after circle morereview" href="{% url 'user-review-list' profile_user.id %}">
          리뷰 전체보기
        </a>
      {% endif %}
    </div>
    ...
    ```