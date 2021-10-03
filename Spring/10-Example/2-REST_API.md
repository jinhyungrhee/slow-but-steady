# 네이버 지역검색 API를 활용한 맛집 리스트 만들기 예제

## Naver API로 장소/이미지 검색 요청 & 결과 받기

1. res/application.properties를 yaml 확장자로 변경한 뒤 필요한 API정보들 추가
  ```yml
  naver:
  url:
    search:
      local: https://openapi.naver.com/v1/search/local.json
      image: https://openapi.naver.com/v1/search/image
  client:
    id: xxxxxxxx
    secret: xxxxxxxxxx
  ```

2. Naver Client 생성
  - NaverClient.java
    ```java
    package com.example.restaurant.naver;

    import com.example.restaurant.naver.dto.SearchImageReq;
    import com.example.restaurant.naver.dto.SearchImageRes;
    import com.example.restaurant.naver.dto.SearchLocalReq;
    import com.example.restaurant.naver.dto.SearchLocalRes;
    import org.springframework.beans.factory.annotation.Value;
    import org.springframework.core.ParameterizedTypeReference;
    import org.springframework.http.HttpEntity;
    import org.springframework.http.HttpHeaders;
    import org.springframework.http.HttpMethod;
    import org.springframework.http.MediaType;
    import org.springframework.stereotype.Component;
    import org.springframework.web.client.RestTemplate;
    import org.springframework.web.util.UriComponentsBuilder;

    @Component
    public class NaverClient {
        // SpringBoot에서 application.yaml에 지정한 값들을 찾아올 수 있음 (env나 시스템변수 설정으로도 가능)
        @Value("${naver.client.id}")
        private String naverClientId;

        @Value("${naver.client.secret}")
        private String naverClientSecret;

        @Value("${naver.url.search.local}")
        private String naverLocalSearchUrl;

        @Value("${naver.url.search.image}")
        private String naverImageSearchUrl;

        // 검색 요청 메서드 생성
        // 장소 검색
        public SearchLocalRes searchLocal(SearchLocalReq searchLocalReq) {
            // 요청 주소 생성
            var uri = UriComponentsBuilder.fromUriString(naverLocalSearchUrl)
                    // query parameter로 SearchLocalReq에 정의된 request가 들어가야 함
                    // 일일이 만들지 않고 미리 만들어 둔 형태를 가지고 사용
                    .queryParams(searchLocalReq.toMultiValueMap())
                    .build()
                    .encode()
                    .toUri();

            // 헤더 세팅 (naver api - 6.예시/호출 부분 참고)
            var headers = new HttpHeaders();
            headers.set("X-Naver-Client-Id", naverClientId);
            headers.set("X-Naver-Client-Secret", naverClientSecret);
            headers.setContentType(MediaType.APPLICATION_JSON);

            // 헤더를 엔티티에 담기 (request entity)
            var httpEntity = new HttpEntity<>(headers);

            // response type 지정
            var responseType = new ParameterizedTypeReference<SearchLocalRes>(){};

            // RestTemplate 통해서 요청을 보내고 응답 받기
            // (responseEntity에는 SearchLocalRes 값이 들어오게 됨)
            var responseEntity = new RestTemplate().exchange(
                    uri,
                    HttpMethod.GET,
                    httpEntity,
                    responseType
            );

            // 원했던 결과(SearchLocalRes)를 리턴시켜 줌 (getBody()를 통해 결과 return시킴)
            return responseEntity.getBody();
        }
        
        // 이미지 검색
        // 위와 동일한 형태에 req와 res만 바뀌었음!
        public SearchImageRes searchImage(SearchImageReq searchImageReq) {

            // 요청 주소 생성
            var uri = UriComponentsBuilder.fromUriString(naverImageSearchUrl)
                    // query parameter로 SearchImageReq에 정의된 request가 들어가야 함
                    // 일일이 만들지 않고 미리 만들어 둔 형태를 가지고 사용
                    .queryParams(searchImageReq.toMultiValueMap())
                    .build()
                    .encode()
                    .toUri();

            // 헤더 세팅 (naver api - 6.예시/호출 부분 참고)
            var headers = new HttpHeaders();
            headers.set("X-Naver-Client-Id", naverClientId);
            headers.set("X-Naver-Client-Secret", naverClientSecret);
            headers.setContentType(MediaType.APPLICATION_JSON);

            // 헤더를 엔티티에 담기 (request entity)
            var httpEntity = new HttpEntity<>(headers);

            // response type 지정
            var responseType = new ParameterizedTypeReference<SearchImageRes>(){};

            // RestTemplate 통해서 요청을 보내고 응답 받기
            // (responseEntity에는 SearchImageRes 값이 들어오게 됨)
            var responseEntity = new RestTemplate().exchange(
                    uri,
                    HttpMethod.GET,
                    httpEntity,
                    responseType
            );

            // 원했던 결과(SearchImageRes)를 리턴시켜 줌 (getBody()를 통해 결과 return시킴)
            return responseEntity.getBody();
        }
    }
    ```

3. 요청 변수 변수화 (전부)
  - SearchLocalReq.java
    ```java
    package com.example.restaurant.naver.dto;

    import lombok.AllArgsConstructor;
    import lombok.Data;
    import lombok.NoArgsConstructor;
    import org.springframework.util.LinkedMultiValueMap;
    import org.springframework.util.MultiValueMap;

    @NoArgsConstructor
    @AllArgsConstructor
    @Data
    public class SearchLocalReq {
        // 4가지 요청 변수
        private String query = "";

        private int display = 1;

        private int start = 1;

        private String sort = "random";

        // queryParam()에서 미리 만들어둔 형태로 사용하기 위해 MultiValueMap 메서드 생성
        public MultiValueMap<String, String> toMultiValueMap() {
            var map = new LinkedMultiValueMap<String, String>();

            map.add("query", query);
            map.add("display", String.valueOf(display));
            map.add("start", String.valueOf(start));
            map.add("sort", sort);

            return map;
        }
    }
    ```
  - SearchImageReq.java
    ```java
    package com.example.restaurant.naver.dto;

    import lombok.AllArgsConstructor;
    import lombok.Data;
    import lombok.NoArgsConstructor;
    import org.springframework.util.LinkedMultiValueMap;
    import org.springframework.util.MultiValueMap;

    @NoArgsConstructor
    @AllArgsConstructor
    @Data
    public class SearchImageReq {
        // 5가지 요청 변수
        private String query = "";

        private int display = 1;

        private int start = 1;

        private String sort = "sim";

        private String filter = "all";

        // queryParam()에서 미리 만들어둔 형태로 사용하기 위해 MultiValueMap 메서드 생성
        public MultiValueMap<String, String> toMultiValueMap() {
            var map = new LinkedMultiValueMap<String, String>();

            map.add("query", query);
            map.add("display", String.valueOf(display));
            map.add("start", String.valueOf(start));
            map.add("sort", sort);
            map.add("filter", filter);

            return map;
        }
    }

    ```

4. 출력 결과 변수화 (필요한 것만)
  - SearchLocalRes.java
    ```java
    package com.example.restaurant.naver.dto;

    import lombok.AllArgsConstructor;
    import lombok.Data;
    import lombok.NoArgsConstructor;

    import java.util.List;

    @NoArgsConstructor
    @AllArgsConstructor
    @Data
    public class SearchLocalRes {
        // 필요한 출력 결과만 정의
        private String lastBuildDate;
        private int total;
        private int start;
        private int display;
        private String category;
        // "item/items" -> items 안에 item들이 리스트 형태로 들어있다는 의미
        private List<SearchLocalItem> items;
        // 자세한 내용은 내부 클래스로 정의
        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        public static class SearchLocalItem {
            private String title;
            private String link;
            private String description;
            private String telephone;
            private String address;
            private String roadAddress;
            private String mapx;
            private String mapy;
        }
    }
    ```
  - SearchImageRes.java
    ```java
    package com.example.restaurant.naver.dto;

    import lombok.AllArgsConstructor;
    import lombok.Data;
    import lombok.NoArgsConstructor;

    import java.util.List;

    @NoArgsConstructor
    @AllArgsConstructor
    @Data
    public class SearchImageRes {
        // 필요한 출력 결과만 정의
        private String lastBuildDate;
        private int total;
        private int start;
        private int display;
        // "item/items" -> items 안에 item들이 리스트 형태로 들어있다는 의미
        private List<SearchImageItem> items;
        // 자세한 내용은 내부 클래스로 정의
        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        public static class SearchImageItem {
            private String title;
            private String link;
            private String thumbnail;
            private String sizeheight;
            private String sizewidth;
        }
    }
    ```

5. 테스트 하기
  - 테스트 디렉토리 오른쪽 클릭 - new 디렉토리 맨 아래 resources 생성
  - 새로 생성된 resources 디렉토리에 application.yaml 복사/붙여넣기
  - test디렉토리에 NaverClientTest.java 클래스 생성
    ```java
    package com.example.restaurant.naver;

    import com.example.restaurant.naver.dto.SearchImageReq;
    import com.example.restaurant.naver.dto.SearchLocalReq;
    import org.junit.jupiter.api.Test;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.boot.test.context.SpringBootTest;

    @SpringBootTest
    public class NaverClientTest {

        @Autowired
        private NaverClient naverClient;

        @Test
        public void searchLocalTest() {

            var search = new SearchLocalReq();
            search.setQuery("갈비집");

            var result = naverClient.searchLocal(search);
            System.out.println(result);
        }

        @Test
        public void searchImageTest(){
            var search = new SearchImageReq();
            search.setQuery("갈비집");

            var result = naverClient.searchImage(search);
            System.out.println(result);
        }
    }
    ```