# Review 모델

## Review 모델 만들기

- Review 모델 구성
  - 리뷰의 제목(title)
  - 음식점의 이름(restaurant_name)
  - 음식점 장소 카카오 or 네이버 플레이스 링크(restaurant_link)
  - 음식점에 대한 평점 1~5점(rating)
  - 음식 사진 최대 3개(image1, image2, image3)
  - 리뷰 내용(content)
  - 리뷰 생성시간(dt_created)
  - 리뷰 수정시간(dt_updated)

- Review 모델 생성
  - models.py에 Review 클래스 생성
    ```py
    # 리뷰 모델
    class Review(models.Model):
        title = models.CharField(max_length=30)
        restaurant_name = models.CharField(max_length=20)
        restaurant_link = models.URLField(validators=[validate_restaurant_lisk]) # 이 필드에 들어가는 값이 URL인지 자동으로 확인해줌(네이버/카카오 validator 추가 -> validators.py)

        RATING_CHOICES = [
            (1, 1), # 튜플의 첫 번째 값은 실제로 모델 필드에 들어갈 값, 두 번째 값은 display에 사용되는 값
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        ]
        rating = models.IntegerField(choices=RATING_CHOICES) # 필드에 여러 개의 값 중 하나만 들어갈 수 있도록 하려면 'choices' 옵션 사용!

        image1 = models.ImageField()
        image2 = models.ImageField()
        image3 = models.ImageField()
        content = models.TextField() # 길이 제한이 없는 character 필드
        dt_created = models.DateTimeField(auto_now_add=True) # auto_now_add : 모델이 생성되는 시간을 자동으로 필드에 넣어줌
        dt_updated = models.DateTimeField(auto_now=True) # auto_now : 모델이 마지막으로 저장된 시간을 자동으로 필드에 넣어줌

        #리뷰 모델의 string 메서드 정의
        def __str__(self):
            return self.title
    ```

## 정적 파일과 미디어 파일

### 정적 파일

- 웹 어플리케이션에서 바뀌지 않는 파일
- CSS, image, favicon 등은 내용이 바뀌지 않음
- 정적 파일을 사용하려면...
  - 정적 파일이 컴퓨터 안 어디에 있는지 알아야 함
  - 정적 파일의 URL이 무엇인지 알아야 함
- 정적 파일의 URL은 어떻게 정해지는가
  - setting.py
    ```py
    STATIC_URL = '/static/'
    ```
    - 정적 파일의 URL 주소는 `localhost:8000(도메인)/static/my_dir/my_file(폴더 안의 파일 경로)`이 됨
      - 예시 : `localhost:8000/static/coplate/styles/style.css`
- 정적 파일 두 가지 종류
  - 정해져 있는 정적 파일 : `static file`
    - STATIC_URL 사용
    - 파일 위치 : app_name/static/app_name (샌드위치 구조) -> 장고가 직접 찾아갈 수 있음
    - {% static 'path' %} 로 접근 가능
  - 유저가 업로드한 정적 파일 : `media file`
    - MEDIA_URL 사용
    - MEDIA_ROOT 세팅을 통해 위치를 직접 알려줘야 함

### 미디어 파일

- 미디어 파일을 저장할 폴더 생성
  - 프로젝트 루트에 media 폴더 생성하고 그 안에 사진을 저장할 review_pics 폴더 생성
  - coplate_project/media/review_pics

- 장고에게 미디어 파일 위치 알려주기
  - settings.py에 MEDIA_URL 설정(웹에서 접근할 URL)
    ```py
    MEDIA_URL = '/uploads/'
    ```
  - settings.py에 MEDIA_ROOT 설정 (파일이 저장될 위치)
    ```py
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    ```

- 장고한테 media 파일에 대한 요청이 들어오면 media 파일을 돌려주라고 설정하기
  - static 파일을 돌려주는 작업은 장고가 자동으로 해주지만 media 파일은 직접 설정 필요!
  - coplate_project/urls.py
    ```py
    from django.conf import settings
    from django.conf.urls.static import static
    ...
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # 미디어 파일에 대한 요청이 들어오면 미디어 ROOT 안에 있는 미디어 파일을 돌려주라는 의미!
    ```

## ImageField 다루기

- models.ImageField()
  - 미디어 파일의 URL 주소를 저장하고, 이미지 필드에 대한 모델 폼을 만들면 폼에 업로드된 파일을 지정된 미디어 루트(MEDIA_ROOT)안에 넣어줌
  - 미디어 파일을 쉽게 다룰 수 있게 도와줌
  - ImageField를 사용하기 위해서는 pillow 패키지 설치 필요
    ```
    pip install pillow
    ```
  - 사진을 업로드할 때 MIDEA_ROOT 안에 정확히 어느 곳에 업로드할지 지정
    - ImageField()의 upload_to 속성의 값으로 경로 전달
      - models.py
      ```py
      image1 = models.ImageField(upload_to="review_pics") # 필수
      image2 = models.ImageField(upload_to="review_pics", blank=True) # 선택
      image3 = models.ImageField(upload_to="review_pics", blank=True) # 선택
      ```

> Model(models.py)이 변경되었으므로 migration 필요!
> - python manage.py makemigrations
> - python manage.py migrate

## admin 페이지에 Review 모델 등록하기

- admin.py
  ```py
  from .models import User, Review
  ...
  # 리뷰 모델 등록
  admin.site.register(Review)
  ```
- admin 페이지에서 올린 리뷰 사진의 URL 확인
  - django shell 실행 : `python manage.py shell`
    ```
    (InteractiveConsole)
    >>> from coplate.models import Review
    >>> r = Review.objects.all().first()
    >>> r
    <Review: 코스버거에 다녀오다!>
    >>> r.image1
    <ImageFieldFile: review_pics/burger_bhIgJCA.jpg>
    >>> r.image1.url
    '/uploads/review_pics/burger_bhIgJCA.jpg'
    ```