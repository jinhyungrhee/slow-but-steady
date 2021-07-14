## Rest API

- Rest API란?
    - Rest API : GET, POST, DELETE, PUT:UPDATE, REPLACE(FECTH : UPDATE, MODIFY)
    - 과거에는 GET과 POST방식으로 게시판의 글들을 수정하거나 삭제했음 (글 조회는 GET 방식)
    - 지금은 어떤 글을 입력하거나 수정할 때는 **PUT** 을 이용해 주소창으로 요청할 수 있고  
        수정(REPLACE)할 때에는 **FETCH**를 자주 사용함
    - **중요(사용 이유)** : URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미함
    - 예시
        - ex) `GET : www.movies.com/movies` : 영화를 전부 조회
        - ex) `GET : www.movies.com/movies/:id` : 해당 아이디를 가진 영화를 조회 => url정보로 자원의 상태를 파악할 수 있음!
        - ex) `POST : www.movies.com/movies/` : (url이 동일하더라도) 영화를 생성
        - ex) `PUT : www.movies.com/movies/` : (url이 동일하더라도) 영화를 수정
        - ex) `DELETE : www.movies.com/movies/` : (url이 동일하더라도) 영화를 삭제
    - url의 변화 없이 통신의 요청하는 방식에 따라 다르게 작동할 수 있음!
    - 개발 시 매우 편리

## 코드

```py
import requests # http통신과 관련된 메서드 모두 제공

# 세션 활성화
s = requests.Session() # requests모듈 => session, cookies, get, post, rest(put,delete)등 메서드 활용해서 쉽게 보낼 수 있도록 만들어짐!(편리)

# 예제1
r = s.get('https://api.github.com/events') # event정보를 요청하겠구나 알 수 있음

# 수신상태 체크
r.raise_for_status() # 만약 에러가 발생하면 예외처리 하고 종료됨! -> 에러가 발생하지 않아야 통과됨!

# 출력
#print(r.text)

# 예제2
# 쿠키 설정(정석)
jar = requests.cookies.RequestsCookieJar() # 서버에서 요구하는 쿠키 정보가 많거나 쿠키 정보를 디테일하게 입력하고 싶을 때 사용!
# 쿠키 삽입 -> 이 정보들이 서버에 넘어감!
jar.set('name', 'niceman', domain="httpbin.org", path='/cookies') # Jar을 활용하면 쿠키정보 "디테일"하게 설정 가능!

# 요청
r = s.get('http://httpbin.org/cookies', cookies=jar)

# 출력
#print(r.text)

# 예제3
r = s.get('https://github.com', timeout=5) # timeout=5 : 서버가 느릴 경우 5초까지 기다림

# 출력
#print(r.text)

# 예제4 - post방식
r = s.post('http://httpbin.org/post', data={'id':'test77', 'pw':'1111'}, cookies=jar) #form 데이터 뿐만 아니라 쿠키도 거의 필수적으로 받음!

# 출력
#print(r.text) # header파일과 서버에서 받은 정보 다시 보내줌(login같은 것 처리 시 유용)
#print(r.headers) # 우리가 세션과 쿠키를 사용했기 때문에 헤더파일 정보'Connection': 'keep-alive' 리턴 -> 이때부터 계속 요청하면 서버는 동일한 클라이언트로 인식

# 예제5
# 요청(POST)
payload1 = {'id':'test11', 'pw':'7771'} # form데이터 변수로 따로 할당
payload2 = (('id', 'test22'), ('pw', '7772')) # 튜플 형태로도 form데이터 전송 가능

r = s.post('http://httpbin.org/post', data=payload2)

# 출력
#print(r.text)

# 예제 6(Rest API - PUT)
r = s.put('http://httpbin.org/put', data=payload1) # 데이터를 수정하거나 삽입하려는 것 알 수 있음(put)

# 출력 - 응답 데이터
#print(r.text)

# 예제 7(Rest API - DELETE)
r = s.delete('http://httpbin.org/delete', data={'id': 1}) # 서버에 id가 1번인 것 삭제(delete)요청 -> 테스트 서버라 실제로 삭제되지는 않음!

# 출력 - 응답 데이터
print(r.text)

r = s.delete('https://jsonplaceholder.typicode.com/posts/1') # post에 있는 1번을 지워달라는 요청
# 이처럼 url로 자원의 행동을 실행시킬 수 있는 것 => Rest API
print(r.ok)
print(r.text) # {} : 형식적으로 삭제 완료했다는 의미
print(r.headers)

s.close()
```

