## beautifulsoup4

- bs4 설치  
`pip install beautifulsoup4`

- find() vs find_all()
    - find() : title처럼 딱 하나만 있는 경우 주로 사용. 또는 여러 개중 딱 하나만 필요한 경우(맨 처음 것)
    - find_all() : 공통점이 있고 한번에 여러개 가져올 경우에 사용  

    => 언제 find()를 쓰는지 find_all()을 쓰는지 구분하는 것 중요!


## 코드 정리
```py
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is h2 area</h2>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there wer three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            <a data-test="test" data-io="link3" href="http://example.com/little" class="sister" id="link3">Title</a>
        </p>
        <p class="story">
            story....
        </p>
    </body>
</html>
"""
# requests.get()으로 가져온 html문서라고 가정
# <a data-test="test" data-io="link3" : 이거는 사용자가 임의대로 만든 속성값임!

# 예제1 (BeautifulSoup 기초)
# bs4 초기화
soup = BeautifulSoup(html, 'html.parser') # 첫번째 인자로 웹에서 가져온 데이터 문서 입력(=requests.get('https://~').text)
# 두번째 인자 (xml인지 html인지 구분)

# 타입 확인
print('soup', type(soup)) # <class 'bs4.BeautifulSoup'>
print('prettify', soup.prettify()) # 파싱 후 형식(html)에 맞게 트리구조로 보여주는 함수

# h1 태그 접근
h1 = soup.html.body.h1 # 위에서부터 순서대로 나열
print('h1', h1)

# p 태그 접근
p1 = soup.html.body.p # 해당 태그가 여러 개일 경우 첫번째 자식만 가져옴! (첫번째 p태그에 위치!)
print('p1', p1)

# 다음 태그로 접근
p2 = p1.next_sibling.next_sibling # 두번 호출 (첫번째 -> text는 출력X, 두번째 -> 태그 출력)
#p2 = p1.next_sibling.next_sibling.next_sibling.next_sibling # 네번 호출
print('p2', p2)

""" 이런식으로 접근함!
<p class="title"><b>The Dormouse's story</b></p>(*호출1*)
(*2*)<p class="story">Once upon a time there wer three little sisters. -2:<p>
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
    <a data-io="link3" href="http://example.com/little" class="sister" id="link3">Title</a>
</p>(*3*)
(*4*)<p class="story">
"""

# 텍스트 출력1
print('h1 >> ', h1.string) # .string() : 태그 하위의 텍스트 출력하는 함수

# 텍스트 출력1
print('p >> ', p1.string)

# 함수 확인 - dir()
#print(dir(p2))

# 다음 엘리먼트 확인
print(list(p2.next_element))
#print(list(p2.next_element.next_element)) # ? 
#print(p2.next_element.next_element.next_element) # ? - 패턴? 

# 반복 출력 확인
for v in p2.next_element:
    pass
    #print(v)

# 예제2(Find, Find_all)
# bs4 초기화

soup2 = BeautifulSoup(html, 'html.parser')

# a 태그 모두 선택
link1 = soup.find_all('a') # 리스트의 형태로 문서에 존재하는 a태그 전부 출력 (limit=2 옵션: 두개만 출력)

# 리스트 요소 확인
print('links', link1)

# 타입 확인
#print(type(link1)) # <class 'bs4.element.ResultSet'>

# ***중요***
# 태그 이외의 속성 값을 이용해서 가져올 수 있음
# 또는 태그 하위에 있는 string문자열로도 조건을 만들어서 가져올 수 있음

link2 = soup.find_all("a", class_="sister") # id="link2", string="Title", string=["Elsie"]
#link2 = soup.find_all("a", string=["Elsie", "Title"])
print(link2)

for t in link2: # 조건에 따라 가져온 것을 반복문으로 출력하는 패턴 (**중요**)
    print(t)

# 처음 발견한 a 태그 선택
link3 = soup.find("a")

print()
print(link3)
print(link3.string) # 둘다 문자열 가져오는 것
print(link3.text) # 둘다 문자열 가져오는 것

# 다중 조건 (***중요***)
link4 = soup.find("a", {"class":"sister", "data-io": "link3"})

print()
print(link4) # 태그 전체 출력
print(link4.text) # 하위의 문자열에 접근해서 출력
print(link4.string) # 하위의 문자열에 접근해서 출력

# '태그'(+속성값)로 접근 : find, find_all
# --------------------------------------------------------------
# 'CSS 선택자'로 접근 : select_one, select

# 예제3(select, select_one)
# 태그(p) + 클래스(.) + 자식선택자(>)

link5 = soup.select_one('p.title > b') # 조금 더 전문가스럽고 세부적으로 가져올 수 있음!
print()
print(link5)
print(link5.text)
print(link5.string)

link6 = soup.select_one('a#link1')
print()
print(link6)
print(link6.text)
print(link6.string)

link7 = soup.select_one("a[data-test='test']") # 클래스(.)나 아이디(#)가 아닌 "사용자가 임의대로 지정한 속성값"은 "대괄호([])"사용!
print()
print(link7)
print(link7.text)
print(link7.string) # text보다는 주로 string 많이 사용

# 선택자에 맞는 전체 선택
link8 = soup.select('p.story > a')
print()
print(link8) # 3개 모두 가져와서 리스트로 저장 -> for문 돌려서 하나씩 확인
#print(link8.string)

link9 = soup.select('p.story > a:nth-of-type(2)') # p태그 하위의 a태그 중 '2번째'인 것 가져옴(순서)
print()
print(link9)

link10 = soup.select("p.story")
print()
print(link10)

for t in link10:
    temp = t.find_all("a")
    #print(temp)

    if temp:
        for v in temp:
            print('>>>>>', v)
            print('>>>>>', v.string)
    else:
        print('------', t)
        print('------', t.string)
```