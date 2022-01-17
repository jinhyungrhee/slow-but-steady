# 리뷰 수정 페이지 구현하기

- 리뷰 수정 페이지
  - 리뷰 작성 페이지와 기능은 다르지만 리뷰 form을 사용하기 때문에 리뷰 작성 페이지와 똑같이 생김
  - 즉, URL과 로직을 처리하는 뷰는 다르지만 동일한 form 클래스와 template 파일을 사용함!

- 리뷰 수정 페이지의 URL 설정
  - coplate/urls.py
    ```py
    urlpatterns = [
        # 리뷰 수정 페이지
        path(
            # '수정'도 기존 리뷰 하나에 대한 액션이므로 review_id가 들어간 URL이 필요함!
            "reviews/<int:review_id>/edit/",
            views.ReviewUpdateView.as_view(),
            name="review-update", # 이름 설정
        ),
    ]
    ```

- 리뷰 수정 로직을 처리하는 뷰(ReviewUpdateView) 구현
  - coplate/views.py
    ```py
    from django.views.generic import (
      ListView,
      DetailView, 
      CreateView, 
      UpdateView # UpdateView도 가져오기
    )

    # 제네릭의 UpdateView를 가져와서 ReviewUpdateView 뷰 구현
    class ReviewUpdateView(UpdateView):
        model = Review
        form_class = ReviewForm
        template_name = "coplate/review_form.html"
        # url에서 수정할 리뷰의 id를 가져와야 함 -> 'pk_url_kwarg' 사용!
        pk_url_kwarg = "review_id" # review_id로 넘겨줌
        # 수정된 리뷰의 detail 페이지로 리디렉션
        def get_success_url(self):
            # 'self.object' -> 이 제네릭 뷰가 다루고 있는 object를 의미함!
            return reverse("review-detail", kwargs={"review_id":self.object.id})
        # UpdateView는 작성자를 건드릴 필요가 없기 때문에 form_valid()메서드 필요X
    ```

- 리뷰 상세 페이지에서 '수정'버튼 연결
  - templates/coplate/review_detail.html
    ```html
    ...
        <div class="footer">
          <a class="back-link" href="{% url 'index' %}">&lt; 목록으로</a>
          <div class="buttons">
            <a class="cp-button warn" href="#">삭제</a>
            <!-- parameter로 review.id를 넣어줌! -->
            <a class="cp-button secondary" href="{% url 'review-update' review.id %}">수정</a> 
          </div>
        </div>
      </article>
    </main>
    ```

- 페이지 상단 title이 '리뷰 제목'으로 나타나도록 변경
  - template에서 리뷰를 생성하는 것인지, 수정하는 것인지 판단해야 함!
    - **template에 리뷰 object가 전달되었는지 여부를 확인하면 됨**
      - 생성 : 리뷰 object가 template에 전달되지 않음 (url에 review_id 포함X)
      - 수정 : 리뷰 object가 template에 전달됨 (url에 review_id 포함O)
    - templates/coplate/review_form.html
      ```html
      <!-- 리뷰 object가 전달이 되면, 해당 리뷰의 제목을 title로 설정 -->
      <!-- 리뷰 object가 전달되지 않으면, '새 포스트 작성'을 title로 설정 -->
      <!-- title 뒤에는 항상 'Coplate'가 붙도록 설정 -->
      {% block title %}
        {% if review %} 
          {{ review.title }}
        {% else %} 
          새 포스트 작성
        {% endif %} | Coplate 
      {% endblock title %}
      ```

- 리뷰 수정 페이지에서 '취소'버튼 클릭시 홈페이지가 아닌 리뷰 상세 페이지로 돌아가도록 설정
  - templates/coplate/review_form.html
    ```html
    <div class="buttons">
      <!-- '리뷰 생성' : 홈페이지로 이동 | '리뷰 수정' : 리뷰 상세 페이지로 이동 -->
      <!-- href 안에서 if문 사용! -->
      <a 
        class="cp-button secondary cancel" 
        href="{% if review %}{% url 'review-detail' review.id %}{% else %}{% url 'index' %}{% endif %}"
        >
          취소
        </a>
      <button class="cp-button submit" type="submit">완료</button>
    </div>
    ```

- 리뷰 수정시 업로드된 사진의 thumbnail 보여주기
  - templates/coplate/review_form.html
    ```html
    <div class="file">
      <div class="file-content">
        <!-- 업로드된 image1의 thumbnail 보여주기 -->
        {% if review.image1 %} 
          <img src="{{ review.image1.url }}">
        {% endif %}
        <div>
          {{ form.image1 }}
          {% for error in form.image1.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
      </div>
    </div>
    <div class="file">
      <div class="file-content">
        <!-- 업로드된 image2의 thumbnail 보여주기 -->
        {% if review.image2 %} 
          <img src="{{ review.image2.url }}">
        {% endif %}
        <div>
          {{ form.image2 }}
          {% for error in form.image2.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
      </div>
    </div>
    <div class="file">
      <div class="file-content">
        <!-- 업로드된 image3의 thumbnail 보여주기 -->
        {% if review.image3 %} 
          <img src="{{ review.image3.url }}">
        {% endif %}
        <div>
          {{ form.image3 }}
          {% for error in form.image3.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
      </div>
    </div>
    ```

- 접근 제어(로그인된 유저가 본인 작성 글에 대해서만 수정 가능)에 대한 기능 구현X