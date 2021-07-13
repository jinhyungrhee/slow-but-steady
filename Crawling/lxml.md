## lxml 사용하기

- 파싱(parsing) : xml이나 html의 부분을 어떤 구조에 맞게 내가 원하는 데이터를 가져오는 것
    - ex) 특수문자 제거해서 가져오기, 한글로된 부분만 가져오기 등

- lxml 다운로드
    - 실행된 가상환경 안에서 pip install
        ```
        pip install xlml
        ```

- requests 다운로드
    - requests와 urllib3 다운로드 됨(pip list 통해 확인!)
        ```
        pip install requests
        ```

- cssselect 다운로드
    - cssselect() 사용하기 위함
        ```
        pip install cssselect
        ```

- GET vs POST
    - GET : url주소 상의 쿼리 정보를 네이버 서버에 넘기는 방식 (사용자가 어디에서 무엇을 클릭했는지 알 수 있음)
        - 로그인하지 않아도 괜찮은 정보들
    - POST : 쿼리 정보가 숨겨져서 서버에 넘기는 방식
        - 보안이 중요시되는 정보들(로그인 페이지, 은행 사이트 등)

```py
import requests
import lxml.html

def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """

    # 스크랩핑 대상 URL 
    response = requests.get("https://www.naver.com") # GET, POST

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    # 결과 출력
    for url in urls:
        # url 출력
        print(url)
        # 파일 쓰기 
        # 생략 - text파일로 저장할지, excel 파일로 저장할지, DB로 저장할지 코드를 짜 넣음


def scrape_news_list_page(response): # url부분만 parsing하는 코드 작성
    # URL 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    # print(response.content)
    root = lxml.html.fromstring(response.content)
    # print(root)
    for a in root.cssselect('.thumb_area .thumb_box .popup_wrap a.btn_popup'): # 인자로 원하는 css 선택자 입력
        # 링크
        url = a.get('href') # 선택한 태그 중 원하는 정보가 담긴 속성 지정
        urls.append(url)
    return urls


# 스크랩핑 시작
if __name__ == "__main__":
    main()
```