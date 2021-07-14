## Reqeust 사용하기

- Session 이용하여 데이터 수신 상태 확인
    - .status_code : 정상적으로 수신 완료되었으면 200 리턴
    - .ok : 정확하게 수신이 완료되었으면 true리턴 / 서버가 죽어있거나 응답이 없으면 false 리턴

    ```py
    import requests

    # 세션 활성화
    s = requests.Session() # 세션 열기
    r = s.get('https://www.naver.com') # get방식으로 요청

    # 수신 데이터
    # print(r.text)

    # 정확이 수신했는지 알기 위한 속성 값 활용
    # 1. 수신 상태 코드
    print('Status Code : {}'.format(r.status_code)) # 정상적으로 수신 완료하면 200 리턴

    # 2. 확인
    print('OK? : {}'.format(r.ok)) # true면 정확하게 수신이 완료됨 <-> 서버가 죽어있거나 응답이 없으면 false 리턴

    # 세션 비활성화
    s.close() # 세션 닫기
    ```

- 쿠키란?
    - 쿠키 정보를 클라이언트에 저장해놓았다가 클라이언트가 다시 접속했을 때 클라이언트를 식별함
    - 로그인 정보 유지, 장바구니 등

- 쿠키 정보 송수신 테스트 사이트  
    `https://httpbin.org/`

### 정리
- 서버 측에서는 이 클라이언트가 정상적으로 접근해서 내가 주는 데이터를 수신해가는지 확인하기 위해서 **쿠키 정보**나 **헤더 정보**를 확인함
    - 클라이언트가 정상적인 클라이언트인지 확인

- GET방식으로 요청할 때 `쿠키`와 `헤더 정보`를 실어서 우리가 만든 코드가 정상적으로 요청을 하는 것임을 서버에게 알려줘야 함
- 서버가 요구하는 대로 정보를 실어서(payload) 요청을 할 수 있게 만들어주는 기능 => **Requests 모듈의 강력한 기능!**

### 코드 흐름
```py
import requests

s = requests.Session()

# 쿠키 Return 
r1 = s.get('https://httpbin.org/cookies', cookies={'name': 'kim1'}) # get방식으로 요청
print(r1.text)

# 쿠키 Set - 서버쪽에 쿠키를 저장할 때 쓰는 메서드
r2 = s.get('https://httpbin.org/cookies/set', cookies={'name': 'kim2'}) # REST API - '서버 쪽에 저장하려는구나' url로 의미상 확인 가능
print(r2.text)

# User-Agent
url = 'https://httpbin.org'
headers = {'user-agent': 'nice-man_1.0.0_win10_ram16_home_chrome'}

# Header 정보 전송
r3 = s.get(url, headers=headers) # 원하면 쿠키 값도 함께 전송 가능 " ,cookies={'name': 'kim1'} "
print(r3.text) # html 소스가 넘어왔으면 정확하게 header값이 전송되었음을 알 수 있음!

# 세션 비활성화
s.close()

# With문 사용(권장) -> 파일, DB, HTTP : 코드 간결, 외부 리소스 작업 시 안전(자동 반환)
with requests.Session() as s:
    r = s.get('https://daum.net')
    print(r.text)
    print(r.ok)
    # with문이 끝날 때 자동적으로 close()호출됨!
```