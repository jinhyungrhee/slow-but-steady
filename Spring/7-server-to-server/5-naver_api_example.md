# Naver Open API 연동

- API결과를 String으로 받아서 간단하게 확인하기

## Open API 신청하기

- naver open api 접속
    - https://developers.naver.com/docs/common/openapiguide/

- Documents - 서비스 API - 검색 - 지역

- 사용 방법
    - Client ID와 Client Secret 값을 Http 헤더에 넣어서 전송
    - GET으로 호출

- naver 계정으로 login - 어플리케이션 등록(API 이용신청)
    - 신청하면 Client ID와 Client Secret이 발급됨!

- 처음에 바로 코딩하지 않고 Talend API에서 request 보내보기
    - 요청 예시
        - URI 
            - https://openapi.naver.com/v1/search/local.json?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&sort=random
        
        - header
            - X-Naver-Client-Id
            - X-Naver-Client-Secret

    - response 결과
        ```
        {
        "lastBuildDate": "Fri, 10 Sep 2021 15:01:07 +0900",
        "total": 5,
        "start": 1,
        "display": 5,
        "items":[
            {"title": "유안타<b>증권</b>", "link": "http://www.myasset.com/",…},
            {"title": "도이치<b>증권</b>", "link": "", "category": "금융,보험>투자기관", "description": "",…},
            {"title": "<b>주식</b>투자의신", "link": "https://multistock.modoo.at",…},
            {"title": "뉴지스탁", "link": "http://newsystock.blog.me/", "category": "금융,보험>주식,증권",…},
            {"title": "<b>주식</b>투자1번지", "link": "http://cafe.naver.com/toozabooza",…}
        ]
        }
        ```

## 코드로 작성

- server를 호출해서 Open API 사용하기
- 일단 테스트이므로 String으로 출력 결과 받아서 볼 것임!
- ServerApiController.java
    ```java
    @Slf4j
    @RestController
    @RequestMapping("/api/server")
    public class ServerApiController {

        // Naver Open API 호출하기
        
        // https://openapi.naver.com/v1/search/local.json
        // ?query=%EC%A3%BC%EC%8B%9D
        // &display=10
        // &start=1
        // &sort=random
        @GetMapping("/naver")
        public String naver(){

            // 주소
            URI uri = UriComponentsBuilder
                    .fromUriString("https://openapi.naver.com")
                    .path("/v1/search/local.json")
                    .queryParam("query","중국집")
                    .queryParam("display",10)
                    .queryParam("start",1)
                    .queryParam("sort", "random")
                    .encode(Charset.forName("UTF-8")) // 네이버에서 요청한 "query를 UTF-8로 인코딩해라" 
                    .build()
                    .toUri();

            log.info("uri : {}", uri);

            RestTemplate restTemplate = new RestTemplate();
            // header값 만들기 -> RequestEntity
            // GET으로 요청하기 때문에 Void 타입
            RequestEntity<Void> req = RequestEntity
                    .get(uri)
                    .header("X-Naver-Client-Id","xxxxxxxxxxxxxxxx")
                    .header("X-Naver-Client-Secret", "xxxxxxxxxx")
                    .build();

            // 일단 String으로 결과를 받음
            ResponseEntity<String> result = restTemplate.exchange(req, String.class);

            return result.getBody();
        }

        @GetMapping("/hello")
        public User hello(@RequestParam String name, @RequestParam int age){
            User user = new User();
            user.setName(name);
            user.setAge(age);

            return user;
        }

        @PostMapping("/user/{userId}/name/{userName}")
        public Req<User> post(
                        @RequestBody Req<User> user,
                        @PathVariable int userId,
                        @PathVariable String userName,
                        @RequestHeader("x-authorization") String authorization,
                        @RequestHeader("custom-header") String customHeader
        ){
            log.info("userId : {}, userName : {}", userId, userName);
            log.info("authorization : {}, custom : {}", authorization, customHeader);
            log.info("client req : {}", user);

            Req<User> response = new Req<>();
            response.setHeader(
                    new Req.Header()
            );

            response.setResBody(user.getResBody());

            return response;
        }
    }
    ```

## 결과 확인

- GET 요청을 사용했기 때문에 웹 브라우저에서도 결과 확인 가능
    - 결과
        ```
        { "lastBuildDate": "Fri, 10 Sep 2021 15:33:36 +0900", "total": 5, "start": 1, "display": 5, "items": [ { "title": "딘타이펑 명동점", "link": "http://www.dintaifung.co.kr/", "category": "중식>중식당", "description": "", "telephone": "", "address": "서울특별시 중구 명동1가 59-1", "roadAddress": "서울특별시 중구 명동7길 13 명동증권빌딩", "mapx": "310404", "mapy": "551834" }, { "title": "초류향", "link": "", "category": "중식>중식당", "description": "", "telephone": "", "address": "서울특별시 중구 다동 164-2", "roadAddress": "서울특별시 중구 다동길 24-10", "mapx": "310128", "mapy": "552188" }, { "title": "란주라미엔", "link": "", "category": "중식>중식당", "description": "", "telephone": "", "address": "서울특별시 중구 충무로1가 25-9", "roadAddress": "서울특별시 중구 명동8나길 49", "mapx": "310273", "mapy": "551463" }, { "title": "크리스탈제이드 소공점", "link": "http://www.crystaljade.co.kr", "category": "중식>중식당", "description": "", "telephone": "", "address": "서울특별시 중구 소공동 21-1", "roadAddress": "서울특별시 중구 남대문로7길 16 한국빌딩 B1", "mapx": "310191", "mapy": "551829" }, { "title": "하이디라오 명동점", "link": "https://www.facebook.com/HaidilaoKorea/", "category": "음식점>중식>중식당", "description": "", "telephone": "", "address": "서울특별시 중구 을지로2가 199-13", "roadAddress": "서울특별시 중구 명동3길 36", "mapx": "310419", "mapy": "551947" } ] }
        ```
    - JSON Validator로 깔끔하게 보기
        ```js
        {
        "lastBuildDate":"Fri, 10 Sep 2021 15:33:36 +0900",
        "total":5,
        "start":1,
        "display":5,
        "items":[
            {
                "title":"딘타이펑 명동점",
                "link":"http://www.dintaifung.co.kr/",
                "category":"중식>중식당",
                "description":"",
                "telephone":"",
                "address":"서울특별시 중구 명동1가 59-1",
                "roadAddress":"서울특별시 중구 명동7길 13 명동증권빌딩",
                "mapx":"310404",
                "mapy":"551834"
            },
            {
                "title":"초류향",
                "link":"",
                "category":"중식>중식당",
                "description":"",
                "telephone":"",
                "address":"서울특별시 중구 다동 164-2",
                "roadAddress":"서울특별시 중구 다동길 24-10",
                "mapx":"310128",
                "mapy":"552188"
            },
            {
                "title":"란주라미엔",
                "link":"",
                "category":"중식>중식당",
                "description":"",
                "telephone":"",
                "address":"서울특별시 중구 충무로1가 25-9",
                "roadAddress":"서울특별시 중구 명동8나길 49",
                "mapx":"310273",
                "mapy":"551463"
            },
            {
                "title":"크리스탈제이드 소공점",
                "link":"http://www.crystaljade.co.kr",
                "category":"중식>중식당",
                "description":"",
                "telephone":"",
                "address":"서울특별시 중구 소공동 21-1",
                "roadAddress":"서울특별시 중구 남대문로7길 16 한국빌딩 B1",
                "mapx":"310191",
                "mapy":"551829"
            },
            {
                "title":"하이디라오 명동점",
                "link":"https://www.facebook.com/HaidilaoKorea/",
                "category":"음식점>중식>중식당",
                "description":"",
                "telephone":"",
                "address":"서울특별시 중구 을지로2가 199-13",
                "roadAddress":"서울특별시 중구 명동3길 36",
                "mapx":"310419",
                "mapy":"551947"
            }
        ]
        }
        ```


## 앞으로 해야 할 것

- `4.출력결과`의 `필드`들을 Class로 다 정의해서 object로 잘 떨어질 수 있게끔 만들어줘야 함!