## urlopen

- 직접 다운로드 X (<-> urlretrive는 직접 path에 저장하는 함수)
- urlopen으로 웹에서 수신된 데이터를 가지고 있으면서 그 자체를 다른 함수에서 매개변수로 받는 패턴으로 사용!
    - urlopen으로 수신한 데이터를 다른 함수로 넘길 때 주로 사용


    ```py
    import urllib.request as req
    from urllib.error import URLError, HTTPError # FOR 주소 오타로 인한 예외처리

    # 다운로드 경로 및 파일명
    path_list = ["C:/test1.jpg", "C:/index.html"]

    # 다운로드 리소스 url
    target_url = ["https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MzFfMTM0%2FMDAxNjIyNDUzMjgxODA4.Pjaa4pnjw0LIoVnt-JbzDa77Njo5tq_K0iqB5uZC0Ucg.SlxnAeTWnCQlDmLBlakMCT9WdOcq3Msbp77b49VneX8g.PNG.yhmnm1%2F20210531_181848.png&type=sc960_832", "http://google.com"]

    for i, url in enumerate(target_url): # enumerate() : 인덱스 붙여줌
        # 예외 처리
        try:
            # 웹 수신 정보 읽기
            response = req.urlopen(url) # urlopen은 직접 다운로드하지 않고 데이터를 변수에 넘겨줌(변수가 데이터 저장)

            # 수신 내용
            contents = response.read()

            print("-----------------------------------------------")

            # 상태 정보 중간 출력
            print("Header Info-{} : {}".format(i, response.info())) # 첫번째 : 인덱스 번호, 두번째 : 헤더정보 가져오는 함수
            print("HTTP Status Code: {}".format(response.getcode())) # HTTP status code 가져오는 함수
            print()
            print("-----------------------------------------------")

            with open(path_list[i], 'wb') as c: # contents를 binary 파일로 path에 씀 - * with문 * : write가 끝나고 자동으로 닫힘!
                c.write(contents)

        except HTTPError as e: # 서버가 죽어있거나 권한이 없을 때(404) 발생하는 에러
            print("Download faile.")
            print("HTTPError Code : ", e.code)
        except URLError as e: # 잘못된 url 사용했을 경우에 발생하는 에러
            print("Download failed.")
            print("URL Error Reason : ", e.reason)
        
        # 성공
        else:
            print()
            print("Download Succed.")
    ```

- 정리
    - urlopen함수는 수신된 데이터를 담을 수 있음
        - `response = req.urlopen(url)`
    - 리턴 값이 저장된 변수가 곧 클래스 객체이기 때문에 그 클래스가 가지고 있는 함수(info(), getcode())를 편리하게 사용할 수 있음!