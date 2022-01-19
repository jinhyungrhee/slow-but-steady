# 프로필 정보 추가하기

- Profile
  - 유저를 나타내는 다양한 정보
    - 프로필 사진
    - 간단한 소개 문구
    - 유저 닉네임도 프로필에 속함

## 유저 모델에 프로필 정보 추가하기

- ①필드 추가
  - coplate/models.py
  ```py
  class User(AbstractUser):

      nickname = models.CharField(
          max_length=15, 
          unique=True, 
          null=True, 
          validators=[validate_no_special_characters],
          error_messages={'unique':'이미 사용중인 닉네임입니다.'},
      )

      # 프로필 사진 필드 정의
      # 디폴트 프로필 사진 설정, 모든 프로필 사진은 media/profile_pics 폴더에 저장
      profile_pic = models.ImageField(
          default="default_profile_pic.jpg", upload_to="profile_pics"
      )

      # 소개문구 필드 정의
      intro = models.CharField(max_length=60, blank=True)

      def __str__(self):
          return self.email
  ```
  - 유저가 업로드한 파일(media/profile_pics/)과 구분하기 위하여 디폴트 프로필 사진을 media 폴더(media/)에 위치시킴

- ②모델 수정이 끝났으면 반드시 migration 해주기!!
  ```cmd
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```
  - 이때, 기존 유저들의 프로필사진과 소개문구를 어떻게 할 것인지 묻는 메시지 나타나지 않았음
    - 프로필 사진은 default를 설정해주었고, 소개문구는 빈 값을 허용해주었기 때문!

- ③추가 필드가 admin 페이지에 나타나도록 admin.py 수정
  - 유저 모델의 추가 필드는 기본적으로 admin 페이지에 나타나지 않기 때문!
  - coplate/admin.py
    ```py
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User, Review

    admin.site.register(User, UserAdmin)
    # user모델에 대한 추가 필드는 기본적으로 admin 페이지에 나타나지 않기 때문에 따로 admin 페이지에 추가해주는 코드
    # -> custom fields라는 섹션 아래에 nickname, profile_pic, intro field 추가!
    UserAdmin.fieldsets += (
      ("Custom fields", {"fields": ("nickname", "profile_pic", "intro")}),
    )

    admin.site.register(Review)
    ```

## 템플릿에 프로필 사진 추가하기

- 추가할 코드
  ```html
  <!-- 프로필 사진 추가 -->
  <div class="cp-avatar" style="background-image: url('{{ review.author.profile_pic.url }}')"></div>
  ```
  - 닉네임 앞에 추가
  - `url('{{ review.author.profile_pic.url }}')` : 현재 리뷰(review)의 작성자(author)의 프로필사진(profile_pic)의 url을 가져옴!

- 홈페이지 (templates/coplate/index.html)
  ```html
  ...
  <div class="contents">
    {% for review in reviews %}
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
                <!-- 프로필 사진 추가 -->
                <div class="cp-avatar" style="background-image: url('{{ review.author.profile_pic.url }}')"></div>
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
  ...
  ```

- 리뷰 상세 페이지(templates/coplate/review_detail.html)
  ```html
  ...
  <main class="site-body">
  <article class="review-detail max-content-width">
    <div class="review-info">
      <div class="restaurant-name">
        <span class="cp-chip green">{{ review.restaurant_name }}</span>
      </div>
      <h1 class="title">{{ review.title }}</h1>
      <div class="author">
        <a class="review-author" href="#">
          <!-- 프로필 사진 추가 -->
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
  ...
  ```