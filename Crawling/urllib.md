## urllib 사용법

- urllib.request import하기

```py
import urllib.request as req # alias 사용
```

- `urlretrieve()` : 다운로드 받을 파일과 수신 정보(header)값 리턴
    - header 정보로 서버와 여러가지 정보 수신함(개발자도구-Network-F5-항목click-Headers)
    - header로 송수신 - `status code : 200`이여야 정상 처리된 것!


        ```py
        import urllib.request as req # 이름이 길어서 alias 지정

        # 파일 URL
        img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MzBfMTk5%2FMDAxNjIyMzg2NzU1ODE0.mvm033Pt21ohO39tCOWV2FSzAZFCpHKgXElPUI8y2Ssg.ZswpoFDBIAw6mXwGs9Ums0MW60zbm1jr1Ib54_0BPC4g.JPEG.sonamu_amc%2F108.jpg&type=sc960_832'
        html_url = 'http://google.com' # 페이지 소스코드를 다운로드 받음

        # 다운받을 경로
        save_path1 = 'C:/test1.jpg'
        save_path2 = 'C:/index.html'

        # 예외 처리
        try:
            file1, header1 = req.urlretrieve(img_url, save_path1) # header값도 수신 정보값으로 받아올 수 있음(req.urlretireve사용)
            file2, header2 = req.urlretrieve(html_url, save_path2) # 첫번째 인자 : source url , 두번째 인자 : 저장 경로
        except Exception as e:
            print('Download failed')
            print(e)
        else: # 정상적으로 실행되었을 경우
            # Header 정보 출력
            print(header1)
            print(header2)

            # 다운로드 파일 정보
            print('Filename1 {}'.format(file1))
            print('Filename2 {}'.format(file2))
            print()

            # 성공
            print('Download Succeed')

        ```

- HTTP 통신 : 한번 요청과 수신이 이루어진 뒤 끊어지는 방식   
        -> 쿠키 값을 이용해서 세션(연결)을 유지시킴

- 결과
    - 지정한 경로에 페이지 소스가 html파일로 다운 -> 데이터를 웹에서 수집하는 것(크롤링)의 시작임!
        - 타겟 url을 요청해서 url에 있는 모든 정보를 내 컴퓨터로 가져오는 것
    - 파싱(parsing) : 이렇게 가져온 페이지 정보에서 특정한 정보들을 찾는 것