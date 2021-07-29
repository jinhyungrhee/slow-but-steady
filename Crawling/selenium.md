## 셀레니움

- 정교하게 만들어진 패키지
- GET, POST, urllib request로 크롤링을 할 수 없었던 부분까지 크롤링 가능
    - 사이트 접속 시 나중에 만들어지는 것(JavaScript)까지 크롤링 가능 : AJAX
- 실제 정교하게 만들어진 사이트는 사용자가 직접 키보드를 통해 입력했는지 확인하는 경우도 있음
    - 이 경우에는 fake-useragent만으로는 크롤링할 수 없음
- **브라우저 단위에서 엔진을 가지고 직접 접근해서 크롤링**을 할 수 있는 게 바로 `셀레니움`임!
- 주로 JavaScript가 실행돼서 동적으로 랜더링될 경우(login 등)에 셀레니움이나 브라우저를 통해서 엔진을 가지고 접근함

### Selenium 설치

`pip install selenium`

### 브라우저 엔진 다운

- selenium webdriver
    - 브라우저 별로 다름
    - 크롬드라이버 다운 (https://chromedriver.chromium.org/downloads)
    - 웹드라이버를 통해 어떤 사이트에 접근하여 스크린샷을 찍거나 키 입력 제어 가능
    - 웹드라이버 exe파일을 해당 가상환경 폴더에 넣어줌

### 코드로 이해하기

> selenium 임포트 (webdriver 사용)

```py
from selenium import webdriver
```

> webdriver 설정

- chrome, firefox 등 원하는 웹브라우저에 맞게 사용
- 다운받은 webdriver.exe가 존재하는 경로를 parameter로 넣어줌

```py
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')
```

> 크롬 브라우저 내부 대기
- 5초간 대기
- 관행적인 것임

```py
browser.implicitly_wait(5)
```

> 속성 확인
- 사용 가능한 메서드들 확인

```py
print(dir(browser))
```

> 브라우저 사이즈 변경

- 최대 크기(maximize_window()) 설정 가능
- 최소 크기(minimize_window()) 설정 가능

```py
browser.set_window_size(1000, 500)
```

> 페이지 이동

- 이동하기를 원하는 사이트 URL을 입력하면 해당 페이지로 이동

```py
browser.get('https://www.daum.net')
```