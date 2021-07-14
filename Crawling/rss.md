## RSS

- RSS란?
    - 사이트를 직접 방문하지 않고도 새로운 글이나 소식을 알 수 있도록 업데이트 정보를 다양한 형태(**주로 xml**)로 제공
    - 사이트에서 보내주는 소식지 같은 것
    - (rss) feed라고 하기도 함

### 코드 흐름
```py
import urllib.request
import urllib.parse

# 행정 안전부 : "https://www.mois.go.kr"
# 행정 안전부 RSS API URL
API  = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp" # ?이후 쿼리 부분은 계속 바뀌기 때문에 동적으로 만들어줌

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num)) # params리스트 안에 딕셔너리 형태로 값(쿼리) 넣어줌

# 중간 확인
# print(params)

# 연속해서 4회 요청
for c in params:
    # 파라미터 출력
    # print(c)
    # URL 인코딩
    param = urllib.parse.urlencode(c) # 쿼리 형태(=)로 변환

    # URL 완성
    url = API + "?" + param
    # URL 출력
    print("url : ", url)

    # 요청
    res_data = urllib.request.urlopen(url).read() # .read()까지 달아주면 요청하는 동시에 데이터 읽어옴!
    # print(res_data) # raw데이터 넘어오기 때문에 디코딩 필요! 

    # 수신 후 디코딩
    contents = res_data.decode("UTF-8")

    # 출력
    print("-" * 100)
    print("-" * 100)
    print(contents)

```