## GET 방식 데이터 통신

- query정보가 url상에 노출되기 때문에 게시판 형태나 공개적인 서비스 사이트에서 주로 활용
    - 로그인이나 중요한 원문 데이터(길이가 긴 데이터)들을 보낼 때는 POST방식 활용

### urlopen()

- .geturl() : url주소를 가져오는 메서드
- .status() : 수신 상태를 출력하는 메서드
- .getcode() : 수신 상태를 출력하는 메서드
- .getheaders() : 헤더 정보 출력
- .read('byte수') : 입력한 바이트 수만큼 정보를 읽어옴
- .decode('디코딩방식') : 디코딩 방식 변경

### urlparse()

- .urlparse() : url정보를 분리(parsing)해서 보여줌 
- .urllib.parse.urlencode() : url을 원하는 형태로 인코딩

### 코드 흐름(중요)

```py
import urllib.request
from urllib.parse import urlparse

# 기본 요청1(encar)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url) # 다운로드 받지 않고 수신된 정보를 변수에 저장

# 여러 정보 => urlopen()을 사용하면 사용 가능한 메서드들!

print('type : {}'.format(type(mem))) # {} -> format함수 사용
# mem의 타입 : <class 'http.client.HTTPResponse'> -> 수신된 데이터를 해당 클래스 안에서 구조적으로 가지고 있음!

print('geturl : {}'.format(mem.geturl())) # .geturl() -> url주소 가져오는 메서드
print('status : {}'.format(mem.status)) # .status -> 수신 상태(200) 출력
print('headers : {}'.format(mem.getheaders())) # .getheaders -> 헤더 정보 출력
print('getcode : {}'.format(mem.getcode())) # .getcode -> 수신 상태(200) 출력
print('read : {}'.format(mem.read(100).decode('utf-8'))) # .read(byte수) -> 바이트수만큼 읽어옴 / .decode('utf-8') -> 'utf-8'로 디코딩 방식 변경
# .read(400) -> 지정된 byte수가 너무 크면 utf-8로 해석할 수 없는 정보가 포함될 수 있기 때문에 position error 발생

# !!중요!! : urlparse()함수
# print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test')))
# (결과) parse : ParseResult(scheme='http', netloc='www.encar.co.kr', path='', params='', query='test=test', fragment='')
# -> url정보를 분리(parsing)해서 보여줌 // query 정보만 보고 싶으면 맨뒤에 '.query'추가
print('parse : {}'.format(urlparse('http://www.encar.co.kr?id=test&pw=1111').query)) # "URLPARSE 사용(1)"


# 기본 요청2(ipify)
API = "https://api.ipify.org"

# GET 방식 parameter
values = {
    'format' : 'json' # 'json', 'jsonp', 'text'등은 웹에서 수신하고 발신하는데 사용하는 데이터의 규약(형식)임
}

print('before param : {}'.format(values)) # 바뀌기 전 : 딕셔너리 형태
params = urllib.parse.urlencode(values) # url 인코딩 => "URLPARSE 사용(2)"
print('after param : {}'.format(params)) # 바뀐 후 : 이퀄(=) 형태 / 쿼리 형태

# 요청 URL 생성
URL = API + "?" + params
print("요청 URL = {}".format(URL))

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read() # 안에 byte수를 지정하지 않으면 전부 읽어옴

# 수신 데이터 디코딩
text = data.decode('UTF-8') # python3의 기본 'utf-8'
print('response : {}'.format(text))

```