# 모델과 모델 사이의 관계

- User 모델과 Review 모델 사이에는 특정한 관계가 존재함 : "User가 Review를 작성"
  - 이 관계를 모델에 반영해줘야 함!
  - User 모델과 Review 모델의 연결 필요!

- 데이터 모델링(Data Modeling)
  - 주어진 객체(User, Review)들을 가지고 필요한 장고 모델을 설계하는 것
  - 각 모델에 어떤 필드가 들어가는지를 정하는 것도 중요하지만 모델 사이의 관계를 잘 나타내는 것도 매우 중요!
  - 웹 서비스에 필요한 기능을 쉽게 구현하기 위해 반드시 필요

## User와 Review 사이의 관계

- 1대다 관계(one-to-may relationship)
  - User는 여러 개의 Review를 작성할 수 있음
  - 하지만 Review는 작성자가 한 명뿐임

- 장고에서 1대다 관계 모델링하기
  - **ForeignKey** 사용
    - ForeignKey 안에 관계를 맺을 모델을 넣어줌 : `ForeignKey(Model)`
    - ForeignKey는 1대다에서 '다'쪽에 사용 : Review 모델
      - Review 모델에 ForeignKey 필드 추가!
      - ForeignKey 안에 관계를 맺을 User모델을 넣어줌!
      ```py
      class Review(models.Model):
        ...
        # 작성자 필드 추가 - 1대다 관계 : Review모델과 User모델 연결!
        author = models.ForeignKey(User, on_delete=models.CASCADE)
      ```
  - **on_delete** 옵션
    - 참조하는 오브젝트가 삭제되었을 때, 이 오브젝트를 어떻게 할지 결정
      - 예시) user1이 review1, review2, review3을 작성했는데, user1이 데이터베이스에서 삭제될 경우 review들을 어떻게 할지 결정
    - 옵션1 : 유저가 삭제되면, 해당 유저의 리뷰도 모두 삭제
      ```py
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      ```
    - 옵션2 : 유저가 작성한 리뷰가 하나라도 있다면, 해당 유저 삭제 금지
    - 옵션3 : 유저를 삭제한 후, 해당 리뷰의 작성자(author)를 null로 설정

  > 모델 변경 후 migration 잊지 말기!
  >  - You are trying to add a non-nullable field 'author' to review without a default; we can't do that (the database needs something to populate existing rows).
  >  - 기존에 존재하던 리뷰의 'author'필드는 어떻게 할 것인지 물어보는 것
  >  - 1번 선택 : 기존에 있던 리뷰의 'author'를 이번 한 번만 기존 유저의 username으로 설정 ✔ (id=1은 첫 번째로 생성된 유저)
  >  - 2번 선택 : 종료하고 models.py에 default 값 설정하러 가기

  - author가 잘 적용되었는지 django shell로 확인하기
    ```
    (InteractiveConsole)
    >>> from coplate.models import Review, User
    >>> Review.objects.all()
    <QuerySet [<Review: 코스버거에 다녀오다!>]>
    >>> r = Review.objects.all().first()
    >>> r.author
    <User: rheejinhyung@gmail.com>
    >>> r.author.nickname
    'jhlee'
    >>> Review.objects.filter(author__id=1)               // filter 조건 사용
    <QuerySet [<Review: 코스버거에 다녀오다!>]>
    >>> Review.objects.filter(author__nickname='jhlee')   // filter 조건 사용
    <QuerySet [<Review: 코스버거에 다녀오다!>]>
    ```
    - ⭐ForeignKey 필드로 filter를 걸 때는 underscore 두 개(`__`)와 필드 이름 사용⭐