## JSON 데이터

- JSON이란?
    - 경량 데이터 교환 형식. XML 대체중
    - 특정 언어에 종속되지 않음

- REST 형식 : url을 보고 어떤 것을 몇 개 요청했는지 알 수 있는 것(주로 '/'로 이루어짐)

- json.loads() : str타입의 데이터를 dict타입의 데이터로 변환


## 코드 흐름
```py
import json
import requests # 둘이 한 쌍으로 많이 사용

s = requests.Session() # 세션 열기

# 100개 JSON 데이터 요청
r = s.get('https://httpbin.org/stream/100', stream=True) # stream=True : 텍스트 형태의 데이터를 내부적으로 직렬화해서 가져옴

# 수신 확인
print(r.text)

# Encoding 확인(*중요*)
print('Before Encoding : {}'.format(r.encoding)) # .encoding : 인코딩 속성 확인 => utf-8

if r.encoding is None: # encoding 타입이 None인 경우
    r.encoding = 'UTF-8'

print('After Encoding : {}'.format(r.encoding))

for line in r.iter_lines(decode_unicode=True): # decode_unicode=True : charset방지(글자깨짐방지)를 위해 true로 설정
    # 라인 출력 후 타입 확인
    # print(line) # raw data
    # print(type(line)) # 문자열(str)
    
    # JSON(Dict) 변환 후 타입 확인
    b = json.loads(line) # str -> dict
    # print(b) # 출력 결과는 동일
    # print(type(b)) # 하지만 데이터 타입 '딕셔너리(dict)'

    # 정보 내용 출력
    for k, v in b.items():
        print("key : {}, value : {}".format(k, v))
    
    print()
    print()

s.close() # 세션 종료

r = s.get('https://jsonplaceholder.typicode.com/todos/1')

# Header 정보
print(r.headers)  # header정보를 확인해보면 서버에서 json 데이터를 내려보내준다는 것 확인 가능! ('Content-Type': 'application/json;)

# 본문 정보
print(r.text)

# json 변환
print(r.json()) # .json()과 json.loads() 차이? -> 변환할 값이 단일 레코드(1개)인 경우 사용가능한 메서드 (데이터에 바로 적용 가능)

# key 반환
print(r.json().keys()) # 데이터를 json으로 변환해서 key값만 리턴 : dict_keys(['userId', 'id', 'title', 'completed'])

# value 반환
print(r.json().values()) # 데이터를 json으로 변환해서 value값만 리턴 : dict_values([1, 1, 'delectus aut autem', False])

# 인코딩타입 반환
print(r.encoding) # utf-8

# 바이너리 정보 확인
print(r.content) # b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'

s.close() # 세션 종료 -> 세션을 사용하여 요청할 때마다 마지막에 세션을 닫아줘야 하는지? 아니면 세션을 한번 열고 한번만 닫아주면 되는지?
```