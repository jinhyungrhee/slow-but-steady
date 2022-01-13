# null vs blank

## null

- 데이터베이스와 관련된 옵션
- `null = True`로 설정하면, 필드에 해당하는 데이터베이스 컬럼에 NULL(데이터베이스에서 존재하지 않는 값을 의미)값을 허용하고, 필드에 대한 값이 없으면 데이터베이스에 NULL을 저장함.
- null의 디폴트 값은 false임

## blank

- 폼과 유효성 검사에 관련된 내용
- `blank = True`로 설정하면, 폼(admin 페이지의 폼 포함)에서 필드에 대한 값을 입력해주지 않아도 됨. 즉 optional(= 필수가 아닌) 필드가 됨.

## 문자열 기반 필드

- 문자열 데이터가 저장되는 필드
- 종류
  - `CharField`
  - `EmailField` : 문자열이 이메일 주소인지 확인
  - `URLField` : 문자열이 URL 주소인지 확인
  - `TextField` : 길이 제한이 없는 문자열 필드
  - `ImageField` : 이미지의 URL을 저장하는 필드
- Django에서는 기본적으로 문자열 기반 필드에 대한 값이 없으면 데이터베이스에 빈 문자열("")을 저장함.
  - 데이터베이스에 NULL 대신 빈 문자열("")을 저장하기 때문에 옵셔널 필드로 만들어도 `null=True`가 필요 없음!
    ```py
    # name 필드는 옵셔널 필드(폼에서 작성하지 않아도 됨)
    class Person(models.Model):
      name = models.CharField(max_length=20, blank=True)
    ```
    - 폼에서 name을 입력받지 않으면, 데이터베이스에 빈 문자열("")이 저장됨
    - 만약 옵셔널 필드에 `unique=True`를 사용하려고 하면 문제 발생!
      - 필드 값이 없는 오브젝트가 여러 개 생성될 수 있는데 빈 값을 모두 ""로 저장하면 ""가 중복되어 데이터베이스에서 오류가 발생함
      - 해결 : `null=True`추가 - ""대신 NULL을 사용하면, 어떤 주어진 값으로 생각하지 않기 때문에 중복이 되어도 상관 없음!
      ```py
      # 에러 발생 - 중복 불가 오류(null=False이기 때문!)
      ID      name(blank=True, null=False, unique=True)
      1       "철수"
      2       ""
      3       ""
      4       "영희"

      # 해결(null=True로 변경!)
      ID      name(blank=True, null=True, unique=True)
      1       "철수"
      2       NULL
      3       NULL
      4       "영희"
      ```

## 문자열 기반이 아닌 필드

- 종류
  - `IntegerField` : 정수 저장 필드
  - `DateTimeField` : 날짜와 시간 저장 필드
- 문자열 처럼 빈 값을 대표하는 값(ex-"")이 없기 때문에 데이터베이스에 반드시 NULL로 저장해야 함!
  - 문자열 기반이 아닌 필드를 옵셔널 필드로 만들어주고 싶다면 `blank=True`, `null=True` 둘 다 사용!
  ```py
  # age 필드는 옵셔널 필드(폼에서 작성하지 않아도 됨)
  class Person(models.Model):
    age = models.IntegerField(blank=True, null=True)
  ```


## 정리) 모델 필드의 종류에 따라 null과 blank의 쓰임새가 달라짐!

1. 문자열 기반 필드를 옵셔널 필드로 만들고 싶다면(=필드에 '빈 값'을 허용하고 싶다면) : `blank = True` 사용!
    ```py
    # name 필드는 옵셔널 필드(폼에서 작성하지 않아도 됨)
    class Person(models.Model):
      name = models.CharField(max_length=20, blank=True)
    ```
    - 중복 금지(unique=True)옵션도 같이 사용하고 싶다면 : `unique=True`, `null=True`, `blank=True` 모두 적용!
    ```py
    # name 필드는 옵셔널 필드(폼에서 작성하지 않아도 됨), 하지만 중복 금지!
    class Person(models.Model):
      name = models.CharField(max_length=20, blank=True, null=True, unique=True)
    ```

2. 문자열 기반이 아닌 필드를 옵셔널 필드로 만들고 싶다면 : `null=True`, `blank=True` 사용!
    ```py
    # age 필드는 옵셔널 필드(폼에서 작성하지 않아도 됨)
    class Person(models.Model):
      age = models.IntegerField(blank=True, null=True)
    ```
    - 중복 금지(unique=True)옵션도 같이 사용하고 싶다면 : `unique=True`, `null=True`, `blank=True` 모두 적용!
    ```py
    # age 필드는 옵셔널 필드(폼에서 작성하지 않아도 됨), 하지만 중복 금지!
    class Person(models.Model):
      age = models.IntegerField(blank=True, null=True, unique=True)
    ```
