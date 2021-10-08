

## controller 패키지 추가

- controller/ApiController.java
  ```java
  @RestController
  @RequestMapping("/api/restaurant")
  @RequiredArgsConstructor
  public class ApiController {

      private final WishListService wishListService;

      // swagger-ui로 받아보기 위한 것
      @GetMapping
      public WishListDto search(@RequestParam String query) {
          return wishListService.search(query);
      }
  }
  ```

- Springfox Boot Starter 추가
  ```java
  dependencies {
      implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
      implementation 'org.springframework.boot:spring-boot-starter-web'
      compileOnly 'org.projectlombok:lombok'
      annotationProcessor 'org.projectlombok:lombok'
      testImplementation 'org.springframework.boot:spring-boot-starter-test'
      // https://mvnrepository.com/artifact/io.springfox/springfox-boot-starter
      implementation group: 'io.springfox', name: 'springfox-boot-starter', version: '3.0.0'
  }
  ```

- swagger-ui로 query보내보고 해당하는 결과값 받아볼 수 있음
  - response body
    ```
    {
      "index": 0,
      "title": "장수갈비",
      "category": "한식>육류,고기요리",
      "address": "서울특별시 중구 충무로1가 25-45",
      "roadAddress": "서울특별시 중구 명동2길 54-1",
      "homepageLink": "",
      "imageLink": "http://post.phinf.naver.net/MjAyMDA4MTFfMjUz/MDAxNTk3MTI1MjA0NjI2.UBSDs0VNBH0P5PTD9r5c3TMgSsBBSoFWEJOf7fbU14Mg.j9negdrg3Tq2hLUpciMFxa0EA36xRKdlDLd_aVKEsv4g.PNG/IgCi4uIO9LMrtUMn3MfrPKQQ2_t4.jpg",
      "visitCount": 0,
      "lastVisitDate": null,
      "visit": false
    }
    ```
  - response headers
    ```
    connection: keep-alive 
    content-type: application/json 
    date: Fri08 Oct 2021 04:39:11 GMT 
    keep-alive: timeout=60 
    transfer-encoding: chunked 
    ```

## wishlist에 추가하는 메서드 구현

- ApiController.java
  ```java
  @Slf4j
  @RestController
  @RequestMapping("/api/restaurant")
  @RequiredArgsConstructor
  public class ApiController {

      private final WishListService wishListService;

      // swagger-ui로 받아보기 위한 것
      @GetMapping
      public WishListDto search(@RequestParam String query) {
          return wishListService.search(query);
      }

      // wishlist에 추가하는 메서드
      @PostMapping("")
      public WishListDto add(@RequestBody WishListDto wishListDto) {
          log.info("{}", wishListDto);

          // 데이터가 들어오면 wishListService를 넘김
          return wishListService.add(wishListDto);
      }

      // add가 되는지 확인하기 위해 전체 리스트를 가져오는 메서드
      @GetMapping("/all")
      public List<WishListDto> findAll() {
          return wishListService.findAll();
      }
  }
  ```

- WishListService.java에 add메서드와 findAll메서드 구현
  ```java
  @Service
  @RequiredArgsConstructor
  public class WishListService {

      private final NaverClient naverClient;
      // DB 불러오기
      private final WishListRepository wishListRepository;

      public WishListDto search(String query){

          var searchLocalReq = new SearchLocalReq();
          searchLocalReq.setQuery(query);

          var searchLocalRes = naverClient.searchLocal(searchLocalReq);
          if(searchLocalRes.getTotal() > 0) {

              var localItem = searchLocalRes.getItems().stream().findFirst().get();
              var imageQuery = localItem.getTitle().replaceAll("<[^>]*>", "");

              var searchImageReq = new SearchImageReq();
              searchImageReq.setQuery(imageQuery);

              var searchImageRes = naverClient.searchImage(searchImageReq);

              if(searchImageRes.getTotal() > 0) {
                  var imageItem = searchImageRes.getItems().stream().findFirst().get();

                  var result = new WishListDto();

                  result.setTitle(localItem.getTitle());
                  result.setCategory(localItem.getCategory());
                  result.setAddress(localItem.getAddress());
                  result.setRoadAddress(localItem.getRoadAddress());
                  result.setHomepageLink(localItem.getLink());
                  result.setImageLink(imageItem.getLink());

                  return result;


              }
          }
          return new WishListDto();
      }

      // 추가
      public WishListDto add(WishListDto wishListDto) {
          // Dto를 entity로 바꾼 다음에 저장
          var entity = dtoToEntity(wishListDto);
          // 데이터베이스 불러오기
          var saveEntity = wishListRepository.save(entity); // save했을 때 entity가 return됨
          return entityToDto(saveEntity); // wishListDto가 return됨

      }

      // dto -> entity
      private WishListEntity dtoToEntity(WishListDto wishListDto) {
          var entity = new WishListEntity();
          entity.setIndex(wishListDto.getIndex());
          entity.setTitle(wishListDto.getTitle());
          entity.setCategory(wishListDto.getCategory());
          entity.setAddress(wishListDto.getAddress());
          entity.setRoadAddress(wishListDto.getRoadAddress());
          entity.setHomepageLink(wishListDto.getHomepageLink());
          entity.setImageLink(wishListDto.getImageLink());
          entity.setVisit(wishListDto.isVisit());
          entity.setVisitCount(wishListDto.getVisitCount());
          entity.setLastVisitDate(wishListDto.getLastVisitDate());
          return entity;
      }

      // entity -> dto
      private WishListDto entityToDto(WishListEntity wishListEntity) {
          var dto = new WishListDto();
          dto.setIndex(wishListEntity.getIndex());
          dto.setTitle(wishListEntity.getTitle());
          dto.setCategory(wishListEntity.getCategory());
          dto.setAddress(wishListEntity.getAddress());
          dto.setRoadAddress(wishListEntity.getRoadAddress());
          dto.setHomepageLink(wishListEntity.getHomepageLink());
          dto.setImageLink(wishListEntity.getImageLink());
          dto.setVisit(wishListEntity.isVisit());
          dto.setVisitCount(wishListEntity.getVisitCount());
          dto.setLastVisitDate(wishListEntity.getLastVisitDate());
          return dto;
      }

      // findAll() 메서드 구현
      public List<WishListDto> findAll() {
          
          // 처음에 엔티티를 입력받음
          // listall()에 stream 걸고 map을 통해서 entity를 Dto로 다 변경함
          // 이후 collector를 통해 List로 바꾸어줌
          return wishListRepository.listall()
                  .stream()
                  .map(it -> entityToDto(it)).collect(Collectors.toList());
      }
  }

  ```

- MemoryDbEntity.java의 index와 WishListDto.java의 index 타입 Integer로 변경
  - Refactor - Type Migration 이용
  - MemoryDbEntity.java
    ```java
    @NoArgsConstructor
    @AllArgsConstructor
    @Data
    // 모든 데이터베이스를 가진 애들은 이 MemoryDbEntity를 상속받아서 사용
    public class MemoryDbEntity {
        // index라는 변수 하나만 가지고 있음
        // int는 defualt값이 0이라서 db에 0값이 들어갈 수 있으므로 Integer로 변경! (오른쪽 클릭 - Type Migration - Refactor)
        protected Integer index;
    }
    ```
  - WishListDto.java
    ```java
    @NoArgsConstructor
    @AllArgsConstructor
    @Data
    public class WishListDto {
        // 직접 index 정의(더이상 MemoryDB 상속받지 않음)
        // int는 default가 0이므로 integer로 변경(Refactor 이용해 변경!)
        private Integer index;
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

## 방문추가 & 삭제 기능 구현

- ApiController.java
  ```java
      ...

      // 삭제 기능 추가
      @DeleteMapping("/{index}")
      public void delete(@PathVariable int index) {
          wishListService.delete(index);
      }

      // 방문여부 기능 추가
      @PostMapping("/{index}")
      public void addVisit(@PathVariable int index) {
          wishListService.addVisit(index);
      }
  ```

- WishListService.java
  ```java
      ...

      // delete() 메서드 구현
      public void delete(int index) {
          wishListRepository.deleteById(index);
      }

      // addVisit() 메서드 구현
      public void addVisit(int index) {
          // 원하는 인덱스 찾아오기 (있을 수도 없을 수도 있음)
          var wishItem = wishListRepository.findById(index);
          if(wishItem.isPresent()){
              // 값이 있으면 udpate
              var item = wishItem.get();
              item.setVisit(true);
              item.setVisitCount(item.getVisitCount()+1);
          }
      }
  ```

## Template과 연결하기

- controller 디렉토리에 PageController.java 생성
  ```java
  @Controller
  @RequestMapping("/pages")
  public class PageController {

      // 타임리프에서 특정한 Html을 view로 보낼 때 사용
      @GetMapping("/main")
      public ModelAndView main() {
          return new ModelAndView("main");
      }
  }
  ```