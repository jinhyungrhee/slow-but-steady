## lxml 사용하기2

- session이란?
    - web은 한 번 요청(request)이 들어오면 응답(request)한 뒤 연결이 끊김!
    - 그렇기 때문에 Session을 이용해서 유저가 로그인 했는지 등 여러 가지 상황정보 저장 및 유지
    - 서버에서 일정한 시간 동안 연결의 흐름을 가지고 서비스를 제공받을 수 있음
    - selenium을 이용한 고급 스크랩핑에서 자주 사용

        ```py
        import requests
        from lxml.html import fromstring, tostring

        def main():
        """
        네이버 메인 뉴스 스탠드 스크랩핑 메인함수
        """
        # 세션 사용
        session = requests.Session()

        # 스크랩핑 대상 URL 
        response = session.get("https://www.naver.com") # GET, POST

        # 신문사 링크 리스트 획득
        urls = scrape_news_list_page(response)
        ```

- lxml - fromstring, tostring
    - fromstring : 웹에서 수집된 데이터를 string타입으로 바꾸어줌
    - tostring : 중간 점검 시 콘솔에서 예쁘게 코드 확인 가능

- 주의!!  
    `for a in root.xpath('//div[@class="thumb_area"]'):`
        - 이처럼 밖이 작은 따옴표로 묶여있으면 안에는 큰 따옴표 사용!
        - 반대로 밖이 큰 따옴표로 묶여있으면 안에는 작은 따옴표 사용!

```py
import requests
from lxml.html import fromstring, tostring

def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """
    # 세션 사용
    session = requests.Session()

    # 스크랩핑 대상 URL 
    response = session.get("https://www.naver.com") # GET, POST

    # 신문사 링크 딕셔너리 획득
    urls = scrape_news_list_page(response)

    # 딕셔너리 확인
    # print(urls)

    # 결과 출력

    for name, url in urls.items():
        # url 출력
        print(name, url)
        # 파일 쓰기 
        # 생략 - text파일로 저장할지, excel 파일로 저장할지, DB로 저장할지 코드를 짜 넣음


def scrape_news_list_page(response): # url부분만 parsing하는 코드 작성
    # URL 딕셔너리 선언
    urls = {}

    # 태그 정보 문자열 저장
    # print(response.content)
    root = fromstring(response.content)
    # print(root)
    for a in root.xpath('//div[@class="thumb_area"]/div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]'): # 전체를 포함하는 상위 부모의 루트를 가져와야함!
        
        # a 구조 확인
        # print(a)

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))

        name, url = extract_contents(a)
        # 딕셔너리 삽입
        urls[name] = url

    return urls

def extract_contents(dom):
    # 링크 주소
    link = dom.xpath('./div[@class="popup_wrap"]/a[@class="btn_popup"]')[0].get("href") # 현재 경로 아래 div태그 아래의 a태그 -> # 제거 해야함

    # 신문사 명
    name = dom.xpath('./a/img')[0].get("alt") # 현재 경로 아래 a태그 아래의 a태그

    return name, link

# 스크랩핑 시작
if __name__ == "__main__":
    main()
```