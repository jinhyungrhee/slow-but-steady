## 큰 규모의 포털사이트에서 데이터 가져올 때 주의사항

- 실제 사용자가 데이터를 요청했는지 아니면 파이썬 코드로 데이터를 요청했는지 포털사이트들은 판별 가능
- 그렇기 때문에 코드에서 최대한 클라이언트 헤더정보를 만들어서 보내야 원하는 데이터를 수신할 수 있음!

## 실시간 검색어 또는 인기 검색어 창

- AJAX(비동기 통신)
    - 처음에 홈페이지가 랜더링될 때에는 빠져 있지만 이후에 추가로 network에서 또 한 번 요청을 해서 후에 부가적으로 그려넣는 방식

## 정리

1. 데이터를 해당 url로 요청했는데 원하는 정보가 들어있지 않을 때

    - network 탭에서 다른 url정보를 살펴봐야 함 -> AJAX(비동기 통신) 가능성! 

2. 별도의 요청이 있었을 시 해당 url에서 Preview나 Response탭 확인 -> 찾는 정보가 맞는지 아닌지 알 수 있음!
    
    - 이 url을 직접 접근하면 에러 발생! 
    - 헤더 정보 편집 필요
        - 파이썬 코드로 작성해서 요청하면 user-agent는 '파이썬 엔진'으로 나옴  
        - 포털사이트 서버에서는 브라우저가 아니라고 인식해 403에러 발생시킴  
        => **user-agent와 referer의 정보를 직접 만들어서 넘겨 줘야 함!**
        - fake-useragent 다운  : `pip install fake-useragent`


## 코드 흐름
```py
import json # json 타입으로 데이터 받아오기 때문(설치x)
import urllib.request as req
from fake_useragent import UserAgent

# Fake Header 정보(가상으로 User-agent 생성)
ua = UserAgent()
#print(ua.ie)
#print(ua.msie)
#print(ua.chrome) # 크롬, android 등
#print(ua.safari) # ios, ipad 등
#print(ua.random) # user-agent값 랜덤으로 생성

# 헤더 정보 생성 : 크롬 개발자도구를 보고 이 정보를 찾아내서 입력할 수 있는 것 매우 중요!!!
headers = {
    'User-agent' : ua.ie, # 가상의 user-agent
    'referer' : 'https://finance.daum.net/' # 통해서 들어온 경로
}

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8') # url을 바로 보내는 것이 아니라 Request객체 클래스 안에다가 'url'과 'headers'정보 함께 넣어서 보냄

# 응답 데이터 확인(Json Data)
#print('res', res)

# 응답 데이터 str -> json 변환 및 data 값 출력
rank_json = json.loads(res)['data'] # 'data'가 key값임!

# 중간 확인
#print('중간 확인 : ', rank_json, '\n')

for elm in rank_json:
    # print(type(elm))
    print('순위 : {}, 금액 : {}, 회사명: {}'.format(elm['rank'], elm['tradePrice'], elm.get('name'))) # key값으로 불러올 때 get()메서드도 사용가능
    # 파일(csv, 엑셀, TXT) 저장 및 db 저장하는 코드 작성
```