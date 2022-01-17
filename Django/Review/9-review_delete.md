# 리뷰 삭제 페이지 구현하기

- 리뷰 삭제 페이지의 URL 추가
  - coplate/urls.py
    ```py
    urlpatterns = [
        # 리뷰 삭제 페이지
        path(
            # 삭제도 어떤 리뷰를 삭제해야 할지 알아야 하므로 review_id를 넘겨줘야 함
            "reviews/<int:review_id>/delete/",
            views.ReviewDeleteView.as_view(),
            name="review-delete", # 이름 설정
        ),
    ]
    ```

- 리뷰 삭제 로직을 처리하는 뷰(ReviewDeleteView) 구현
  - coplate/views.py
    ```py
    from django.views.generic import (
        ListView,
        DetailView, 
        CreateView, 
        UpdateView,
        DeleteView, # DeleteView 가져오기
    )
    ...
    # 제네릭의 DeleteView를 가져와서 ReviewDeleteView 뷰 구현
    class ReviewDeleteView(DeleteView):
        model = Review
        template_name = "coplate/review_confirm_delete.html"
        # url에 전달되는 review id의 이름 설정
        pk_url_kwarg = "review_id"
        # 리뷰 삭제 후 홈페이지로 리디렉션
        def get_success_url(self):
            return reverse("index")
    ```

- 리뷰 삭제 template 연결 & 완성
  - coplate/review_detail.html
    ```html
    ...
      <div class="footer">
        <a class="back-link" href="{% url 'index' %}">&lt; 목록으로</a>
        <div class="buttons">
          <!-- 삭제 버튼 클릭시 해당 url로 이동하면서 review.id를 parameter로 넘겨줌! -->
          <a class="cp-button warn" href="{% url 'review-delete' review.id %}">삭제</a>
          <a class="cp-button secondary" href="{% url 'review-update' review.id %}">수정</a>
        </div>
      </div>
    </article>
    ```
  - coplate/review_confirm_delete.html
    ```html
    {% extends "coplate_base/base_with_navbar.html" %}

    {% block title %}{{ review.title }} | Coplate{% endblock title %}

    {% block content %}
    <main class="site-body">
      <!-- 삭제는 서버의 데이터를 바꾸는 것이기 때문에 'post'방식의 request를 보내야 함 -->
      <form class="cp-dialog review-confirm-delete" method="post">
        {% csrf_token %}
        <span class="content">정말 리뷰를 삭제하시겠습니까?</span>
        <button class="cp-button warn" type="submit">삭제</button>
        <!-- 삭제 취소 버튼 클릭시 다시 해당 리뷰의 상세 페이지로 이동(review.id parameter 통해)-->
        <a class="cp-button secondary" href="{% url 'review-detail' review.id %}">취소</a>
      </form>
    </main>
    {% endblock content %}
    ```

- 정리
  - 리뷰 상세 페이지에서 '삭제'버튼을 클릭하여 리뷰 삭제 페이지(reveiw-confirm-delete 템플릿)를 가져오는 것은 `GET 방식`
  - 리뷰 삭제 페이지에서 '삭제'버튼을 클릭하여 리뷰를 삭제하는 것은 `POST 방식`
