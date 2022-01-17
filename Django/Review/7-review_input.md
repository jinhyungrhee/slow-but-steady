# 리뷰 작성 페이지 구현하기

- 리뷰 작성 페이지 URL 설정
  - coplate/urls.py
    ```py
    urlpatterns = [
        # 리뷰 작성 페이지
        path(
            "reviews/new/",
            views.ReviewCreateView.as_view(),
            name="review-create"
        ),
    ]
    ```
    - coplate/views.py에 `ReviewCreateView` 구현 필요!

- 리뷰 작성 시 사용될 ReviewFom 생성
  - coplate/forms.py
    ```py
    # *** 리뷰 작성에 사용될 ReviewForm 생성 *** 
    # Modelform 사용 -> 모델에 있는 필드를 따라서 Form을 자동으로 만들어줌!
    # Modelform 사용 방법 : Meta 클래스 안에 사용할 모델과 모델의 필드를 정의하면 됨!
    class ReviewForm(forms.ModelForm):
      class Meta:
        model = Review # 사용할 모델
        fields = [ # 사용할 필드
          "title",
          "restaurant_name",
          "restaurant_link",
          "rating",
          "image1",
          "image2",
          "image3",
          "content",
          # dt_created, dt_updated, author 필드는 사용자로부터 입력받지 않고 자동으로 생성되거나 연결됨
        ]
    ```

- `ReviewCreateView` 뷰 작성
  - coplate/views.py
    ```py
    # 제네릭 뷰에서 CreateView 가져오기
    from django.views.generic import CreateView
    # 생성한 ReviewFrom 가져오기
    from coplate.forms import ReviewForm 

    # 제네릭의 CreateView 가져와서 ReviewCreateView 작성!
    # 폼을 전달할 때 default로 'form'이라는 이름으로 django form에 템플릿을 전달함!
    class ReviewCreateView(CreateView):
        # 리뷰 작성 form 필요 -> forms.py에 ReviewForm 생성!
        model = Review
        form_class = ReviewForm
        template_name = "coplate/review_form.html"
    ```

- 리뷰 작성 페이지 생성(=input 태그들을 django form 필드로 변경)
  - templates/coplate/review_form.html
    ```html
    {% extends "coplate_base/base_with_navbar.html" %}

    {% load widget_tweaks %}

    {% block title %}새 포스트 작성 | Coplate{% endblock title %}

    {% block content %}
    <main class="site-body">
      <form class="review-form max-content-width" method="post" autocomplete="off" enctype="multipart/form-data">
        {% csrf_token %}
        <div class="title">
          <!--<input type="text" name="title" maxlength="30" placeholder="제목" class="cp-input" required id="id_title"> -->
          {{ form.title|add_class:"cp-input"|attr:"placeholder:제목" }}
          <!-- 오류클래스 메시지 추가 -->
          {% for error in form.title.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
        <div class="restaurant-name">
          <!--<input type="text" name="restaurant_name" maxlength="20" placeholder="음식점 이름" class="cp-input" required id="id_restaurant_name"> -->
          {{ form.restaurant_name|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:음식점 이름" }}
          <!-- 오류클래스 메시지 추가 -->
          {% for error in form.restaurant_name.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
        <div class="restaurant-link">
          <!--<input type="url" name="restaurant_link" maxlength="200" placeholder="네이버 또는 카카오 플레이스 주소" class="cp-input" required id="id_restaurant_link">-->
          {{ form.restaurant_link|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:네이버 또는 카카오 플레이스 주소" }}
          <!-- 오류클래스 메시지 추가 -->
          {% for error in form.restaurant_link.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
        <div class="rating">
          <div class="cp-stars">
            <!--<label for="id_rating_0"><input type="radio" name="rating" value="1" id="id_rating_0" required>★</label>
            <label for="id_rating_1"><input type="radio" name="rating" value="2" id="id_rating_1" required>★★</label>
            <label for="id_rating_2"><input type="radio" name="rating" value="3" id="id_rating_2" required>★★★</label>
            <label for="id_rating_3"><input type="radio" name="rating" value="4" id="id_rating_3" required>★★★★</label>
            <label for="id_rating_4"><input type="radio" name="rating" value="5" id="id_rating_4" required>★★★★★</label>-->
            <!-- 각각의 radio button을 하나씩 렌더링 -->
            {% for radio in form.rating %}
              {{ radio }}
            {% endfor %}
          </div>
          <!-- rating에 대한 오류클래스 메시지 추가 -->
          {% for error in form.rating.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
        <div class="content">
          <!--<textarea name="review" cols="40" rows="10" placeholder="리뷰를 작성해 주세요." class="cp-input" id="id_review"></textarea>-->
          {{ form.content|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:리뷰를 작성해 주세요." }}
          <!-- 오류클래스 메시지 추가 -->
          {% for error in form.title.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
        <div class="file">
          <div class="file-content">
            <div>
              <!--<input type="file" name="image1" accept="image/*" id="id_image1">-->
              {{ form.image1 }}
              <!-- 에러 처리 -->
              {% for error in form.image1.errors %}
                <div class="error-message">{{ error }}</div>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="file">
          <div class="file-content">
            <div>
              <!--<input type="file" name="image2" accept="image/*" id="id_image2">-->
              {{ form.image2 }}
              <!-- 에러 처리 -->
              {% for error in form.image2.errors %}
                <div class="error-message">{{ error }}</div>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="file">
          <div class="file-content">
            <div>
              <!--<input type="file" name="image3" accept="image/*" id="id_image3">-->
              {{ form.image3 }}
              <!-- 에러 처리 -->
              {% for error in form.image3.errors %}
                <div class="error-message">{{ error }}</div>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="buttons">
          <a class="cp-button secondary cancel" href="{% url 'index' %}">취소</a> <!-- 홈페이지로 이동 -->
          <button class="cp-button submit" type="submit">완료</button>
        </div>
      </form>
    </main>
    {% endblock content %}
    ```
    - \<form>태그의 `autocomplete` 속성 : 폼을 작성할 때 과거 사용자가 입력했던 값을 제한하는 기능
    - 별점 기능 수정
      - ①Review 모델의 rating 필드
        - models.py
          ```py
          # 리뷰 모델
          class Review(models.Model):
              title = models.CharField(max_length=30)
              restaurant_name = models.CharField(max_length=20)
              restaurant_link = models.URLField(validators=[validate_restaurant_lisk]) # 이 필드에 들어가는 값이 URL인지 자동으로 확인해줌(네이버/카카오 validator 추가 -> validators.py)

              RATING_CHOICES = [
                  (1, "★"), # 튜플의 첫 번째 값은 실제로 모델 필드에 들어갈 값, 두 번째 값은 display에 사용되는 값
                  (2, "★★"),
                  (3, "★★★"),
                  (4, "★★★★"),
                  (5, "★★★★★"),
              ]
              rating = models.IntegerField(choices=RATING_CHOICES, default=None) # 필드에 여러 개의 값 중 하나만 들어갈 수 있도록 하려면 'choices' 옵션 사용!
              # choices 옵션을 사용하면, django는 default로 'select box'를 위젯으로 사용함 -> 'radio button'으로 변경하려면 forms.py에서 수정!(Meta클래스 안에 위젯 정의)
              # '=============' 없애기 -> default 옵션을 None으로 설정! 
          ```
      - ②ReviewForm에서의 위젯 설정
        - forms.py
          ```py
          class ReviewForm(forms.ModelForm):
            class Meta:
              model = Review # 사용할 모델
              fields = [ # 사용할 필드
                "title",
                "restaurant_name",
                "restaurant_link",
                "rating",
                "image1",
                "image2",
                "image3",
                "content",
                # dt_created, dt_updated, author 필드는 사용자로부터 입력받지 않고 자동으로 생성되거나 연결됨
              ]
              widgets = {
                # rating 필드는 choice들이 radio button으로 렌더되도록 설정!
                "rating" : forms.RadioSelect,
              }
          ```
    - \<form>에서 파일 업로드 할 경우 주의 : `enctype="multipart/form-data"`옵션 추가 필요!
      - `enctype` : form 데이터를 어떻게 인코딩할지 정하는 속성

- 리뷰 작성자를 현재 로그인된 유저로 설정하기
  - `ReviewCreateView`에 **form_valid 메서드** 오버라이딩
    - `form_valid()` : 입력받은 데이터가 유효할 때, 데이터로 채워진 모델 object를 만들고 object를 저장하는 역할 수행! 여기에 `author 데이터`를 추가하여, author 데이터도 리뷰 모델에 같이 저장되도록 함!
    - coplate/views.py
      ```py
      class ReviewCreateView(CreateView):
          model = Review
          form_class = ReviewForm
          template_name = "coplate/review_form.html"
          # 리뷰 작성자를 현재 유저로 설정 - **form_valid()메서드 오버라이딩**
          def form_valid(self, form):
              # 현재 form의 인스턴스에 author라는 필드 정의하고 현재 유저정보(request.user) 입력함
              # 함수형 view에서는 request가 view parameter로 전달되지만, 클래스형 view에서는 request를 self.request로 접근해야 함!!
              form.instance.author = self.request.user
              # 이러한 form 데이터로 모델 object를 만들고 object를 저장하는 로직을 수행 -> form_valid() 호출
              # super()는 ReviewCreateView의 상위 클래스인 CreateView 클래스를 의미함!
              return super().form_valid(form)
              # 정리: form의 인스턴스에 author를 추가하고, 그 form을 CreateView의 form_valid() 메서드에 넣어줬기 때문에 author도 리뷰 object에 함께 저장되는 것!

          # 새로 리뷰가 생성되면 리디렉트될 URL 지정 - **get_success_url()메서드**
          def get_success_url(self):
              # 새로 생성된 리뷰의 상세 페이지로 리디렉트
              # 리뷰 상세 페이지(review-detail)는 id가 parameter로 들어감 -> CreateView에서 새로 생성된 object는 'self.object'로 접근 가능
              return reverse("review-detail", kwargs={"review_id":self.object.id})
      ```
      - 접근 제어(로그인 상태에서만 리뷰 작성) 기능은 아직 구현 X