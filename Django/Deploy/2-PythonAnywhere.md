# PythonAnywhere 사용하기

- 배포
  - 서비스를 많은 사용자가 이용할 수 있도록 서버에 배포(deploy)하기

- 프로덕션(Production)
  - 웹 어플리케이션이 배포된 후 실제로 운영되고 있는 상태
  - 프로덕션에 사용되는 환경을 '프로덕션 환경'이라고 함

## 코드를 PythonAnywhere에 올리기

1. coplate_project 폴더 압축 (**주의 : 프로젝트 폴더가 아닌 상위의 전체 폴더임!**)
2. PythonAnywhere 홈페이지 오른쪽 상단 Files 클릭
3. `Upload a file` 클릭하여 압축한 프로젝트 폴더 업로드
4. `Open Bash console here` 클릭하여 콘솔 창을 열고 `$ unzip coplate_project.zip`을 입력하여 압축해제
5. 프로젝트 세팅을 '프로덕션'에 맞게 바꿔줌
    - PythonAnywhere의 Directories에서 coplate_project/coplate_project/settings.py를 열어줌
      ```py
      ...
      # DEBUG를 False로 설정
      DEBUG = False

      # 사용할 pythonanywhere 도메인 추가
      ALLOWED_HOSTS = ['.pythonanywhere.com']
      ...
      ```
      - 'Save' 눌러서 저장!
6. '프로덕션'에 사용될 가상환경 생성(동일한 콘솔 계속 사용하여 작업 : Consoles - Your consoles)
    - ① 'django_coplate_env' 가상환경 생성
      ```cmd
      $ virtualenv --python=python3.7 django_coplate_env
      ```
    - ② 가상환경 실행
      ```cmd
      $ source django_coplate_env/bin/activate
      ```
    - ③ 가상환경 실행 뒤 필요한 패키지 한꺼번에 설치
      ```cmd
      $ pip install django==2.2 django-allauth django-widget-tweaks pillow django-braces 
      ```
7. 업로드한 '코드'와 생성한 '가상환경'을 모두 활용하는 PythonAnywhere Web App 생성 (Webs - Add a new web app)
    - ① 'Select a Python Web framework'창에서 `Manual configuration/Python 3.7` 선택
    - ② 'Code:' 부분의 Source Code 입력 : `/home/wayofseeing(아이디)/coplate_project(프로젝트이름)/`
    - ③ 'Code:' 부분의 WSGI configuration file 수정
      - ③-① 19번째 줄부터 47번째 줄까지 코멘트 처리(`ctrl + /`)
        ```py
        # HELLO_WORLD = """<html>
        # <head>
        #     <title>PythonAnywhere hosted web application</title>
        # </head>
        # <body>
        # <h1>Hello, World!</h1>
        # <p>
        #     This is the default welcome page for a
        #     <a href="https://www.pythonanywhere.com/">PythonAnywhere</a>
        #     hosted web application.
        # </p>
        # <p>
        #     Find out more about how to configure your own web application
        #     by visiting the <a href="https://www.pythonanywhere.com/web_app_setup/">web app setup</a> page
        # </p>
        # </body>
        # </html>"""

        # def application(environ, start_response):
        #     if environ.get('PATH_INFO') == '/':
        #         status = '200 OK'
        #         content = HELLO_WORLD
        #     else:
        #         status = '404 NOT FOUND'
        #         content = 'Page not found.'
        #     response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
        #     start_response(status, response_headers)
        #     yield content.encode('utf8')
        ```
      - ③-② 76번째 줄부터 89번째 줄까지 코멘트 해제(`ctrl + /`) + path명을 내 프로젝트명으로 변경!
        ```py
        import os
        import sys

        # assuming your django settings file is at '/home/wayofseeing/mysite/mysite/settings.py'
        # and your manage.py is is at '/home/wayofseeing/mysite/manage.py'
        path = '/home/wayofseeing/coplate_project'
        if path not in sys.path:
            sys.path.append(path)

        os.environ['DJANGO_SETTINGS_MODULE'] = 'coplate_project.settings'

        # then:
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        ```
    - ④ 'Virtualenv:' 부분에 가상환경 경로 설정
      - `/home/wayofseeing/django_coplate_env`
8. 정적 파일 세팅
    - ① STATIC_ROOT 설정을 통해 프로젝트의 모든 static 파일을 모을 경로 지정
      - /home/wayofseeing/coplate_project/coplate_project/settings.py
        ```py
        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/2.2/howto/static-files/

        STATIC_ROOT = os.path.join(BASE_DIR, "static") # STATIC_ROOT 설정 추가
        STATIC_URL = '/static/'
        MEDIA_ROOT = os.path.join(BASE_DIR, "media")
        MEDIA_URL = '/uploads/'
        ```
        - STATIC_ROOT는 프로젝트 루트 폴더 안에 'static'이라는 폴더로 설정!
    - ② console에서 프로젝트 파일 안으로 들어와서 manage.py로 collectstatic 커맨드 실행
      ```cmd
      (django_coplate_env) ... ~/coplate_project $ python manage.py collecstatic
      ```
      - 이후 다시 `ls` 커맨드를 입력하면 프로젝트 루트 폴더 안에 'static' 폴더 생성된 것 확인 가능
      - 모든 스태틱 파일이 이곳으로 모인 것
    - ③ PythonAnywhere의 Wep 탭 하단에 있는 `Static Files:`에 URL 입력
      - '스태틱 파일' 경로 설정
        - URL : `/static/`
        - Directory : `/home/wayofseeing/coplate_project/static/`
      - '미디어 파일' 경로 설정
        - URL : `/uploads/`
        - Directory : `/home/wayofseeing/coplate_project/media/`
9. 배포 설정이 모두 완료되었으면, Web 탭 상단의 'Reload' 버튼 클릭
  - 상단에 `Configuration for wayofseeing.pythonanywhere.com` 문구가 나타나면 웹 사이트 접속 가능


## 'WSGI' 정리

- 클라이언트와 서버는 HTTP를 통해 소통함
- 클라이언트는 HTTP Request를 보내고, 서버는 Request를 처리해서 HTTP Response를 돌려줌
- 하지만 Request를 실제로 처리하는 부분은 Django 어플리케이션이기 때문에, 서버는 Request를 Django 어플리케이션으로 전달하고 Django 코드를 실행해야 함
- 이때, 웹 서버와 Django 프레임워크가 소통하는 방식이 바로 `WSGI`임!
  - WSGI 설정 파일은 Django 코드를 어떻게 실행할 것인지를 말해주는 파일임


## '정적 파일' 정리

- 정적 파일
  - 웹 사이트에 사용되는 모든 정적 파일은 각자의 URL이 있고, 정적 파일을 참조할 때는 항상 URL을 사용함
  - html코드 안에 이미지의 URL을 넣어주면(`<img src="/static/coplate/codeit.png>`), django는 이 이미지 파일의 URL에 해당하는 이미지 파일을 찾아서 웹 브라우저에게 돌려줌!
    - 하지만,실제로 운영할 때(=production 환경에서)는 django가 이 역할을 수행할 필요가 없음!
    - `django의 역할` : 필요한 데이터를 찾고, html 파일에 데이터를 렌더해주고 html 파일을 돌려주는 작업을 수행
    - 정적 파일은 '바뀌지 않는 파일'이기 때문에 django가 따로 처리할 로직이 없음 (그냥 파일을 돌려주기만 하면 됨!)

- '정적 파일'을 다루는 방법 : `웹 사이트를 개발할 때`와 `실제로 운영할 때`가 서로 다름!
  - **웹 사이트를 개발할 때(=development 환경에서)** 사용되는 방법
    - html코드 안에 이미지의 URL을 넣어주면(`<img src="/static/coplate/codeit.png>`), django는 이 이미지 파일의 URL에 해당하는 이미지 파일을 찾아서 웹 브라우저에게 돌려줌!
  - **실제로 운영할 때(=production 환경에서)** 사용되는 방법
    - 정적 파일에 대한 request가 들어오면(`/static/coplate/codeit.png`), 그 request를 django 어플리케이션으로 보내지 않고 웹 서버가 바로 정적 파일을 찾아서 클라이언트에게 response로 돌려줌 → **훨씬 효율적인 방법!**


- 서버가 정적 파일을 찾을 수 있도록 설정하기
  - 정적파일에 대한 request가 들어오면, 서버에 있는 특정 폴더 안을 찾아보도록 설정
  - 두 가지 종류의 정적 파일
    - `Static File` : CSS나 icon처럼 웹 사이트의 디자인에 사용되는 파일 (`STATIC_URL = /static/`)
      - URL 경로가 /static/으로 시작할 경우 '스태틱 파일' 폴더 확인!
    - `Media File` : 유저가 업로드한 정적 파일  (`MEDIA_URL = /uploads/`)
      - URL 경로가 /uploads/으로 시작할 경우 '미디어 파일' 폴더 확인!
  - 문제점
    - '미디어 파일'은 media 폴더 한 곳에 모여있지만, '스태틱 파일'은 여러 군데 흩어져 있음
      - coplate 앱에서 사용되는 스태틱 파일은 coplate 앱 안에 있음
      - admin 앱에서 사용되는 스태틱 파일은 admin 앱 안에 있음
    - ❗따라서 모든 스태틱 파일을 한 폴더 안에 모아주는 작업 필요 → `collectstatic` 커맨드 사용❗
      - `collectstatic` : 지정한 경로로 프로젝트의 모든 static 파일을 모아주는 커맨드
      - '지정 경로'는 settings 파일의 `STATIC_ROOT` 설정을 통해 지정
    