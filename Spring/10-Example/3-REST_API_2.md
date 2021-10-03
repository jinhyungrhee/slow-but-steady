# 네이버 지역검색 API를 활용한 맛집 리스트 만들기 예제

## Naver API와 결과물들을 가운데에서 잘 만들어주는 서비스 개발

1. 서비스 패키지와 클래스 추가
  - wishlist 아래 service 디렉토리에 WishListService 클래스 추가
    ```java
    package com.example.restaurant.wishlist.service;

    import com.example.restaurant.naver.NaverClient;
    import com.example.restaurant.naver.dto.SearchImageReq;
    import com.example.restaurant.naver.dto.SearchLocalReq;
    import com.example.restaurant.wishlist.dto.WishListDto;
    import lombok.RequiredArgsConstructor;
    import org.springframework.stereotype.Service;

    @Service
    @RequiredArgsConstructor
    public class WishListService {

        // NaverClient를 사용하여 필요한 내용들을 만들어주는 서비스 개발
        private final NaverClient naverClient;

        // controller를 통해서 들어온 결과를 리턴시킴
        public WishListDto search(String query){

            // << 1. 지역검색 >>
            var searchLocalReq = new SearchLocalReq();
            // 매개변수(query)를 query로 지정
            searchLocalReq.setQuery(query);

            // response는 naverClient의 searchLocalReq를 통해서 searchImageRes를 받아올 것임
            var searchLocalRes = naverClient.searchLocal(searchLocalReq);
            // 결과는 있을 수도, 없을 수도 있음
            // 결과 값이 있을 땐 - (1)
            if(searchLocalRes.getTotal() > 0) {
                // 지역 검색 결과가 있을 때, 첫 번째 item을 꺼냄
                // (getTotal() 자체가 0을 이미 넘었기 때문에 null pointer 에러 발생하지 않음)
                var localItem = searchLocalRes.getItems().stream().findFirst().get();
                // 첫 번재 item을 가지고 imageQuery 생성
                // imageQuery에 잡다한 문자들이 들어갈 수 있으므로, 조금 더 정확하게 동작하기 위해서 정규식 사용
                var imageQuery = localItem.getTitle().replaceAll("<[^>]*>", "");

                // << 2. 지역검색 결과를 가지고 이미지 검색 >>
                var searchImageReq = new SearchImageReq();
                searchImageReq.setQuery(imageQuery);

                // imageQuery를 가지고 naver에서 결과 가져옴
                var searchImageRes = naverClient.searchImage(searchImageReq);

                // 결과 체크
                if(searchImageRes.getTotal() > 0) {
                    // << 3. 두 검색 결과를 가지고 최종 결과를 만들어서 리턴 >>
                    var imageItem = searchImageRes.getItems().stream().findFirst().get();

                    // WishListDto 정의해서 리턴시킴
                    var result = new WishListDto();
                    
                    // 결과 리턴
                    result.setTitle(localItem.getTitle());
                    result.setCategory(localItem.getCategory());
                    result.setAddress(localItem.getAddress());
                    result.setRoadAddress(localItem.getRoadAddress());
                    result.setHomepageLink(localItem.getLink());
                    result.setImageLink(imageItem.getLink());

                    return result;


                }
            }
            // 결과 값이 없을 때는 빈 데이터로 바로 만들어버림 - (2)
            // (아무것도 없을 땐 return null; 해도 되지만 그냥 빈 값 만들어서 던짐)
            return new WishListDto();


        }
    }

    ```

2. wishListDto 추가
  - wishlist entity와 유사하지만 분리시키기 위해 dto 패키지 추가
    - 이유 : 데이터베이스의 엔티티가 변경되면 프론트엔드까지도 변수명에 영향을 끼침
      ```java
      package com.example.restaurant.wishlist.dto;

      import com.example.restaurant.db.MemoryDbEntity;
      import lombok.AllArgsConstructor;
      import lombok.Data;
      import lombok.NoArgsConstructor;

      import java.time.LocalDateTime;

      // 데이터베이스에 어떤 것을 저장할지 결정
      @NoArgsConstructor
      @AllArgsConstructor
      @Data
      public class WishListDto {
          // 직접 index 정의(더이상 MemoryDB 상속받지 않음)
          private int index;
          // 필요한 정보들 정의
          private String title;               // 음식명, 장소명
          private String category;            // 카테고리
          private String address;             // 주소
          private String roadAddress;         // 도로명
          private String homepageLink;        // 홈페이지 주소
          private String imageLink;           // 음식, 가게 이미지 주소
          private boolean isVisit;            // 방문여부
          private int visitCount;             // 방문 횟수
          private LocalDateTime lastVisitDate;// 마지막 방문 일자
      }
      ```
  
3. 테스트 클래스 생성
  - test/wishilist/service/WishListServiceTest.java
    ```java
    package com.example.restaurant.wishlist.service;

    import org.junit.jupiter.api.Assertions;
    import org.junit.jupiter.api.Test;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.boot.test.context.SpringBootTest;

    @SpringBootTest
    public class WishListServiceTest {

        @Autowired
        private WishListService wishListService;

        @Test
        public void searchTest() {
            var result = wishListService.search("갈비집");

            System.out.println(result);
            // result가 null값이면 안 된다
            Assertions.assertNotNull(result);
        }
    }
    ```

## Category = null 오류 뜬 이유
  - Naver에서 API 가이드라인 잘못 작성함
    - 실제로 category는 items 안에 들어있는 item중 하나였음!