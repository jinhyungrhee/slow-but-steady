# URI

- URI(Uniform Resource Identifier)
    - 인터넷에서 특정 자원을 나타내는 주소값
    - 해당 값은 유일함(응답은 달라질 수 있음)
        - 요청 : https://www.fastcampus.co.kr/resource/sample/1
        - 응답 : fastcampus.pdf, fastcampus.docx
    - URI는 거기에 있는 resource 정보가 변경될 수 있음

- URL(Unifom Resource Locator)
    - 인터넷 상에서의 자원, 특정 파일이 어디에 **위치**하는지 식별하는 주소
        - 요청 : https://www.fastcampus.co.kr/fastcampus.pdf
    - 특정 서버, 특정 컴퓨터의 특정 폴더에 있는 파일임!
    - URL은 정확하게 지정된 위치이기 때문에 resource 정보가 변경될 수 없음

- **URL은 URI의 하위개념이다!**

- URI 설계 원칙(RFC-3986)
    1. 슬래시 구분자(/)는 계층 관계를 나타내는 데 사용
    - https://fastcampus.co.kr/classes/java/curriculums/web-master

    2. URI 마지막 문자로 슬래시(/)는 포함하지 않음
    - https://fastcampus.co.kr/classes/java/curriculums/web-master/ (X)  

    3. 하이픈(-)은 URI 가독성을 높이는데 사용
    - https://fastcampus.co.kr/classes/java/curriculums/web-master

    4. 밑줄(_)은 사용하지 않음
    - https://fastcampus.co.kr/classes/java/curriculums/web_master/ (X)

    5. URI 경로에는 소문자가 적합함
    - https://fastcampus.co.kr/classes/java/curriculums/web-master (O)
    - https://fastcampus.co.kr/classes/JAVA/curriculums/web-master (X)

    6. URI에 파일 확장자는 포함하지 않음
    - https://fastcampus.co.kr/classes/java/curriculums/web-master.jsp (X)

    7. 프로그래밍 언어에 의존적인 확장자를 사용하지 않음
    - https://fastcampus.co.kr/classes/java/curriculums/web-master.do (X)

    8. 구현에 의존적인 경로를 사용하지 않음
    - https://fastcampus.co.kr/servlet/classes/java/curriculums/web-master (X)

    9. 세션ID를 포함하지 않음
    - https://fastcampus.co.kr/classes/java/curriculums/web-master?session-id=abcdef (X)

    10. 프로그래밍 언어의 Method명을 이용하지 않음
    - https://fastcampus.co.kr/classes/java/curriculums/web-master?action=intro (X)

    11. 명사에는 단수보다 복수형을 사용하고 컬렉션에 대한 표현은 복수로 사용함
    - https://fastcampus.co.kr/classes/java/curriculums/web-master (O)

    12. 컨트롤러 이름으로는 동사나 동사구 사용
    - https://fastcampus.co.kr/classes/java/curriculums/web-master/re-order (O)

    13. 경로 부분 중 변하는 부분은 유일한 값으로 대체
    - (생략).../curriculums/web-master/lessons/{lesson-id}/user/{user-id}
    - (생략).../curriculums/web-master/lessons/2/users/100
        - 유일한 값 = path variable

    14. CRUD 기능을 나타내는 것은 URI에 사용하지 않음
    - GET: (생략).../curriculums/web-master/lessons/2/users/100/READ (X)
    - DELETE: (생략).../curriculums/web-master/lessons/2/users/100 (O)

    15. URI Query Parameter 디자인
    - URI 쿼리 부분으로 컬렉션 결과에 대해서 필터링 가능
    - (생략).../curriculums/web-master?chapter=2

    16. URI 쿼리는 컬렉션의 결과를 페이지로 구분하여 나타내는데 사용
    - (생략).../curriculums/web-master?chpater=2&page=0&size=10&sort=asc

    17. API에 있어서 서브 도메인은 일관성 있게 사용해야 함
    - https://fastcampus.co.kr  (메인 도메인)
    - https://api.fastcampus.co.kr (패캠의 api를 담당하는 서브 도메인임을 알 수 있음)
    - https://api-fastcampus.co.kr (패캠의 api를 담당하는 서브 도메인임을 알 수 있음)

    18. 클라이언트 개발자 포탈 서브 도메인은 일관성 있게 만듦
    - https://dev-fastcampus.co.kr
    - https://developer-fastcampus.co.kr
    - 실제 운영 환경/프로덕션 환경(= 사용자들이 사용하는 환경)을 개발하기 전에 미리 개발하고 테스트하기 위해 만든 개발환경 (dev 혹은 developer이 앞에 붙은 도메인 사용)