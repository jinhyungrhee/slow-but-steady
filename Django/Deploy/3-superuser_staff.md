# 웹 사이트 관리자 만들기

- superuser
  - admin 페이지에 접속할 수 있고, admin 페이지 내에서도 모든 권한을 갖고 있음

- staff
  - admin 페이지에 접속할 수 있는 유저
  - 모든 superuser는 staff지만, 모든 staff가 superuser는 아님!
 
- admin 페이지
  - admin 페이지에 로그인할 때는 'username'과 'email'을 둘 다 사용할 수 있음
  - admin 페이지에서 일반 유저를 staff로 변경할 수 있음
    - 특정 유저에 대해 '스태프 권한'을 체크 → 이 경우 아무런 권한도 주어지지 않음
    - `사용자 권한:` 선택 필요
      - admin 페이지에서는 모든 모델에 대한 생성/조회/수정/삭제 권한이 따로따로 존재함
      - staff에게 부여하고 싶은 권한을 선택하면 됨
      - ❗주의❗ 이곳에서 staff에게 '유저 수정'권한을 줘버리면, 해당 staff는 자신에게 superuser 권한을 줄 수 있기 때문에 조심해야 함!
      - ⭐중요⭐ 'admin 페이지에서 주어지는 권한'은 '웹 사이트 내에서의 접근 권한'과는 다름!
        - ex) user1이 admin 페이지에서 아무 리뷰나 삭제할 수 있다고 해서, 웹 사이트 내에서 아무 리뷰에 대한 삭제 페이지로 들어갈 수 있는 것은 아님!

- 코드에서 활용
  - User가 Staff인지 확인 : `user.is_staff`
  - User가 Superuser인지 확인 : `user.is_superuser`
    - 이를 통해, 유저가 staff인 경우에만 네비게이션 바에 'admin 페이지 링크'를 만들어 줄 수 있음!

- 필요없는 유저와 리뷰 삭제하기
  - 특정 유저를 삭제하면, 해당 유저가 작성한 리뷰도 모두 삭제됨!
    - Review 모델의 author 필드
      ```py
      author = models.ForeignKey(
        User,
        on_delete = models.CASCADE
      )
      ```
      - `on_delete = models.CASCADE` : 참조하는 object가 삭제되면 현재 object도 삭제
  - admin 페이지에서 리뷰를 모두 삭제해도, 업로드된 사진들은 삭제되지 않음!
    - PythonAnywhere의 File 탭에서 media 폴더 안의 파일들을 모두 삭제해야 함