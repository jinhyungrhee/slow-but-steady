# 테스트 리뷰 추가하기

- media/review_pics 안에 이미지 데이터 추가

- reviews.json을 coplate_project 디렉토리에 추가

- django shell에서 유저들의 id 확인하기
  ```
  >>> from coplate.models import User
  >>> for u in User.objects.all():
  ...     print(u.id)
  ... 
  1
  2
  3
  4
  5
  6
  7
  8
  9
  ```
  - 만약 id값에 1이 존재하지 않으면 fixture(reviews.json)파일의 "author"를 수정해줘야 함!

- fixture 파일(reviews.json) 터미널에서 로드하기
  ```
  $ python manage.py loaddata reviews.json
  Installed 10 object(s) from 1 fixture(s)
  ``` 
  - loaddata 명령어를 사용하여 reviews.json 안에 있는 모든 데이터들을 database에 추가한 것!