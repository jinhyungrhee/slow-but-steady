# 템플릿 오버라이딩

- allauth 템플릿 오버라이딩
  - templates/account 만들고 그 안에 우리가 만든 템플릿 파일을 넣어주기
    - 이때 템플릿 파일 이름은 allauth가 제공하는 템플릿 파일 이름과 동일해야 함!
    - allauth 회원가입 템플릿명 : `signup.html`
  - settings.py의 INSTALLED_APPS 확인
    - coplate(앱 명)가 allauth보다 반드시 위에 위치해야 함!
    - 맨 위부터 탐색하면서 allauth에 있는 signup.html이 아닌 coplate에 있는 signup.html을 가져오기 때문  
    ```py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'coplate', # 오버라이딩하려면 allauth보다 위에 있어야 함!
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
    ]
    ```
  - 이렇게 하면 디자인만 적용되고, 실제 장고 로직과는 연결되어 있지 않은 상태임 -> **템플릿(signup.html) 수정 필요!**
    - django template language 사용하여 수정 
    - form 변수(템플릿 변수)를 사용하여 form과 view를 연결
      - django form 렌더하는 방법
        - ① 한꺼번에 렌더하기
          ```html
          {{form.as_p}}
          ```
        - ② 따로따로 렌더하기 ✔
          ```html
          {{form.field1}}
          {{form.field2}}
          {{form.field3}}
          <!-- form field의 이름을 알아야 함! -->
          ```
          ```html
          이메일        →  {{form.email}} 
          닉네임        →  {{form.nickname}}
          비밀번호      →  {{form.password1}}
          비밀번호 확인  →  {{form.password2}}
          <!--이들은 실제 input 태그로 랜더링됨!-->
          ```
          - ⭐템플릿 변수를 통해서 속성을 추가하거나 변경하는 방법⭐
            - `django-widget-tweaks` 패키지 사용
  - 장고 폼에 속성 더하기
    - `django-widget-tweaks` 패키지 사용
      - form 위젯(= input 태그)을 수정하기 위해 만들어진 패키지
      - pip 설치
        ```
        pip intstall django-widget-tweaks
        ```
      - settings.py의 INSTALLED_APPS에 추가
        ```py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.sites',
            'coplate',
            'widget_tweaks',
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
        ]
        ```
      - ⭐템플릿에 적용⭐
        - widget-tweaks 로드
          ```html
          {% load widget_tweaks %}
          ```
        - widget-tweaks가 제공하는 템플릿 필터를 사용해서 원하는 속성에다가 클래스 추가
          ```html
          {{ form.email|attr:"class:cp-input"|attr:"placeholder:이메일"}}
          ```
          - attr 필터 뒤에 속성 이름을 적고 속성 값을 써주면 됨
          - attr 필터는 태그에 해당 속성이 이미 있으면 새로운 값으로 바꿔주고, 속성이 없으면 추가해줌
          - 클래스 적용은 빈번하게 사용되므로 별도의 직관적인 문법 존재
            ```html
            {{ form.email|add_class:"cp-input"|attr:"placeholder:이메일"}}
            ```
        - ⭐필드 별로 에러 처리 해주기⭐
          - 각각의 에러는 `form.필드명.errors`에서 접근 가능
          ```html
          <!-- 필드에 오류가 있을 때 에러 클래스 추가 : add_error_class:"error" -->
          {{ form.nickname|add_class:"cp-input"|attr:"placeholder:닉네임 (Coplate에서 사용되는 이름입니다)"|add_error_class:"error"}}
          <!-- 여러가지 에러 처리 : form.필드.errors 항목에서 하나씩 가져와서 보여줌 -->
          {% for error in form.nickname.errors %}
          <div class="error-message">{{ error }}</div>
          {% endfor %}
          ```
        - **non-field error**
          - 이메일과 비밀번호의 조합이 틀렸을 경우 발생하는 에러
          - 특정 필드에 속한 에러가 아닌 폼 전체에 대한 오류
          - 폼 전체에 대한 오류 접근 방법 : `non-field error`
            ```html
            <!-- non-field error -->
            {% for error in form.non_field_errors %}
              <div class="form-error error-message">{{ error }}</div> <!-- 에러 메시지 -->
            {%% endfor %}
            ```
  - 메시지 오버라이딩
    - 장고 allauth의 기본 에러 메시지를 템플릿에 포함하지 않았기 때문에 겉으로는 보이지 않지만, 내부적으로 메시지가 계속 쌓이는 문제 발생
      - login과 logout을 반복한 뒤 admin 페이지에 들어가보면 쌓였던 메시지가 한꺼번에 등장함
      - 이렇게 메시지들이 내부적으로 계속해서 쌓이는 것
    - 장고 allauth의 기본 메시지를 사용하지 않도록 `비활성화` 필요!
      - allauth의 메시지 템플릿들을 **빈 템플릿으로 오버라이딩**하면 됨
        - templates/account/messages 추가 
        - messages 안에 있는 메시지들(빈 템플릿들)이 사용됨!
  - 이메일 오버라이딩
    - allauth가 발송하는 인증 이메일 내용 변경
    - 메시지 오버라이딩과 유사하게 allauth 이메일 템플릿을 오버라이딩 해주면 됨
      - templates/account/email 추가
        - email_confirmation_signup_message.txt : 회원가입시 발송되는 이메일 내용
        - email_confirmation_signup_subject.txt : 회원가입시 발송되는 이메일 제목
        - password_reset_key_message.txt : 비밀번호 재설정시 발송되는 이메일 내용
        - password_reset_key_subject.txt : 비밀번호 재설정시 발송되는 이메일 제목
        - django template language(`{{user}}`등)는 html 뿐만 아니라 모든 text기반 포맷에 사용할 수 있음!
    - settings.py에 설정 추가
      - 이메일 오버라이딩을 해도 allauth가 보내는 이메일 제목 앞에는 항상 웹사이트 도메인이 붙게됨
      - 따라서 그것을 제거하는 세팅임
      ```py
      # account email의 제목 앞에 붙는 문자열을 빈 문자열로 만듦
      ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
      ```