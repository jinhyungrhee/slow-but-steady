# 본인의 리뷰만 수정/삭제 가능하게 만들기

- 두 가지 변경
  - 리뷰 상세 페이지의 '삭제', '수정' 버튼이 본인이 작성한 리뷰를 볼 때만 나타나도록 만듦 : `Template 측면`에서의 접근 제한
  - URL을 통해서 '삭제 페이지'와 '수정 페이지'에 들어갈 수 없도록 만듦 : `View 측면`에서의 접근 제한

## Template 측면에서의 접근 제한

- 리뷰의 작성자가 현재 로그인된 유저인 경우에만 삭제/수정 버튼 나타내기
  - template/coplate/review_detail.html
    ```html
    ...
    <div class="footer">
      <a class="back-link" href="{% url 'index' %}">&lt; 목록으로</a>
      <!-- 리뷰의 작성자가 현재 로그인된 유저인 경우에만 버튼 보이기-->
      <!-- 리뷰의 author와 user가 동일한지 체크-->
      <!-- <주의> 템플릿 파일에서는 등호 앞에 반드시 공백을 넣어줘야 함! -->
      {% if review.author == user %}
      <div class="buttons">
        <a class="cp-button warn" href="{% url 'review-delete' review.id %}">삭제</a>
        <a class="cp-button secondary" href="{% url 'review-update' review.id %}">수정</a>
      </div>
      {% endif %}
    </div>
    ```
    - 유저가 로그인되지 않은 상태에서도 버튼은 보이지 않음!

## View 측면에서의 접근 제한

- 리뷰를 수정하려면 로그인이 되어있어야 하고, 수정하려고 하는 리뷰가 본인이 작성한 리뷰여야 함!
  - LoginRequiredMixin 사용
    - 로그인된 상태인지 체크
  - UserPassesTestMixin 사용
    - `test_func()`함수로 리뷰가 본인이 작성한 리뷰인지 체크
  - coplate/views.py
    ```py
    # 제네릭의 UpdateView를 가져와서 ReviewUpdateView 뷰 구현
    class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Review
        form_class = ReviewForm
        template_name = "coplate/review_form.html"
        pk_url_kwarg = "review_id"
        def get_success_url(self):
            return reverse("review-detail", kwargs={"review_id":self.object.id})

        def test_func(self, user):
            # 수정하려는 리뷰의 작성자가 현재 로그인된 유저인지 확인
            review = self.get_object()
            '''
            if review.author == user:
                return True
            else:
                return False
            '''
            # 위 코드를 간소화
            return review.author == user # 조건식이 True면 True가 리턴됨(False면 False 리턴)
    ```

- 웹사이트의 버튼과 링크가 아닌, URL을 통해 이동하는 경우
  - 웹사이트 내에서 가지 말아야 할 곳을 갔다고 생각할 수 있음
  - 클라이언트 쪽에서 부적절한 request를 보내면 서버는 4XX 오류 코드를 리턴함
    - `403 Forbidden response` : 페이지 권한이 없을 때 서버가 돌려주는 오류 코드 ✔
    - 404 Not Found response : 없는 페이지를 요청했을 때 서버가 돌려주는 오류 코드
  - `403 Forbidden response` 리턴하는 방법
    - coplate/views.py
      ```py
      class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        ...
        # 403 forbidden response
        raise_exception = True
        # 로그인이 되어있건 안 되어있건 동일하게 403 에러 리턴
        #redirect_unauthenticated_users = False # (default)
      ```
      - `raise_exception` 옵션에는 여러 종류의 값이 들어갈 수 있음!

> ReviewDeleteView도 동일하게 설정!