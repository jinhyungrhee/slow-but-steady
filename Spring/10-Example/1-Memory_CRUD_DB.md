# 네이버 지역검색 API를 활용한 맛집 리스트 만들기 예제

## Memory CRUD DB 개발

1. DB 구성
  - MemoryDbRepositoryIfs<T> 인터페이스 생성 (main)
    ```java
    package com.example.restaurant.db;

    import java.util.List;
    import java.util.Optional;

    // generic Type 지정
    public interface MemoryDbRepositoryIfs<T> {
        // 인덱스를 받아서 타입에 대한 엔티티를 찾아서 리턴하는 메서드
        Optional<T> findById(int index);
        // 저장하는 메서드
        T save(T entity);
        // 삭제하는 메서드
        void deleteById(int index);
        // 전체를 리턴시키는 메서드
        List<T> listall();
    }
    ```
  - MemoryDbRepositoryAbstract<T> 추상 클래스 생성 (main)
    ```java
    package com.example.restaurant.db;

    import java.util.ArrayList;
    import java.util.List;
    import java.util.Optional;

    // MemoryDbRepositoryAbstract 이름의 abstract 클래스 생성 (MemoryDbRepositoryIfs<T> 상속받음)
    // MemoryDbEntity를 상속받은 generic Type이 필요한 것! (T는 MemoryDbEntity를 상속받음) : generic Type에 와일드카드 걸어서 사용(<T extends MemoryDbEntity>)
    abstract public class MemoryDbRepositoryAbstract<T extends MemoryDbEntity> implements MemoryDbRepositoryIfs<T> {

        // 데이터를 저장할 arrayList 필요 (DB 대용)
        // 리스트에다가 데이터를 쭉 넣는 형태
        private final List<T> db = new ArrayList<>();
        // 데이터베이스에서 자동으로 생성되는 pk(=index id)
        private int index = 0;


        // implements methods
        // index를 사용하기 위해서는 db가 사용하는 entity가 정의되어 있어야 함(데이터에 해당하는 공통적인 사항 정의)
        @Override
        public Optional<T> findById(int index) {
            // filter 통해 검색 (filter는 db stream에 들어있는 type(T)에 대한 부분임)
            // getIndex()는 MemoryDbEntity에 정의된 index를 의미함
            // generic Type에 와일드카드를 걸었기 때문에 generic Type에 해당되는 변수에서 getIndex()라는 메서드가 접근이 가능함!
            // = 'MemoryDbEntity'를 상속받은 애들은 모두 getIndex() 메서드를 가지고 있기 때문에
            //   해당 메서드를 통해 데이터베이스에서 해당 인덱스에 해당하는 데이터를 찾아서 첫번째 값을 optional(있을 수도 없을 수도)하게 데이터를 리턴함
            return db.stream().filter(it -> it.getIndex() == index).findFirst();
        }
        
        // 데이터를 받아서 밀어 넣어주기
        @Override
        public T save(T entity) {

            var optionalEntity = db.stream().filter(it -> it.getIndex() == entity.getIndex()).findFirst();
            // optionalEntity의 getIndex()를 가지고 데이터베이스에서 첫번째부터 쭉 돌다가 동일한 것이 있으면 이미 있는 데이터가 리턴됨
            // 그러면 else문으로 직행

            // 두가지 케이스 존재
            if(optionalEntity.isEmpty()){
                // db에 데이터가 없는 경우(데이터를 새로 추가)
                index++;
                // 저장하려는 엔티티에 인덱스 세팅
                entity.setIndex(index);
                // db에 현재 받은 엔티티 저장
                db.add(entity);
                return entity;
            } else {
                // db에 이미 데이터가 있는 경우(데이터 업데이트)
                // 사전에 이미 있던 인덱스의 데이터를 가져와서
                var preIndex = optionalEntity.get().getIndex();
                // 새로운 데이터에 setIndex()를 통해서 해당 값을 세팅
                entity.setIndex(preIndex);
                // 기존에 있던 데이터 삭제
                deleteById(preIndex);
                // 새롭게 받아온 엔티티를 밀어넣어줌
                db.add(entity);
                return entity;
            }
        }

        // 데이터베이스에서 인덱스로 삭제하기
        @Override
        public void deleteById(int index) {
            // db stream에 filter를 걸어서 인덱스와 동일하면 optional한 객체를 찾아옴
            var optionalEntity = db.stream().filter(it -> it.getIndex() == index).findFirst(); 
            // 이미 데이터가 있는 경우에는
            if(optionalEntity.isPresent()) {
                // remove() 사용하여 해당 object와 동일한 object를 지움 (get()으로 해당 엔티티와 동일한 object찾음)
                db.remove(optionalEntity.get());
            }
        }

        @Override
        public List<T> listall() {
            // db에 있는 모든 내용을 리턴시킴
            return db;
        }
    }
    // 모든 추상화된 MemoryDbRepository가 만들어짐!
    ```
  - MemoryDbEntity 엔티티 클래스 생성  (main)
    ```java
    package com.example.restaurant.db;

    import lombok.AllArgsConstructor;
    import lombok.Data;
    import lombok.NoArgsConstructor;

    @NoArgsConstructor
    @AllArgsConstructor
    @Data
    // 모든 데이터베이스를 가진 애들은 이 MemoryDbEntity를 상속받아서 사용
    public class MemoryDbEntity {
        // index라는 변수 하나만 가지고 있음
        protected int index;
    }
    ```
2. DB에 들어갈 entity 구성
  - WishListEntity 클래스 생성 (main)
    ```java
    package com.example.restaurant.wishlist.entity;

    import com.example.restaurant.db.MemoryDbEntity;
    import lombok.AllArgsConstructor;
    import lombok.Data;
    import lombok.NoArgsConstructor;

    import java.time.LocalDateTime;

    // 데이터베이스에 어떤 것을 저장할지 결정
    @NoArgsConstructor
    @AllArgsConstructor
    @Data
    public class WishListEntity extends MemoryDbEntity { // MemoryDbEntity 상속받음

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
3. DB가 잘 동작하는지 테스트
  - WishListRepository 클래스 생성(MemoryDbRepositoryAbstract 상속) (main)
    ```java
    package com.example.restaurant.wishlist.repository;

    import com.example.restaurant.db.MemoryDbRepositoryAbstract;
    import com.example.restaurant.wishlist.entity.WishListEntity;
    import org.springframework.stereotype.Repository;

    // MemoryDbRepositoryAbstract를 상속받음
    // 'WishListEntity'를 type으로 지정 -> 추상클래스에서 모든 <T>부분이 'WishListEntity'로 대체되어 동작함
    // @Repository -> '데이터베이스로 동작하는 곳' 의미
    @Repository
    public class WishListRepository extends MemoryDbRepositoryAbstract<WishListEntity> {
    }
    ```
  - 테스트를 위한 test/wishlist/repository/WishListRepositoryTest.java 생성 (test)
    ```java
    package com.example.restaurant.wishlist.repository;

    import com.example.restaurant.wishlist.entity.WishListEntity;
    import org.junit.jupiter.api.Assertions;
    import org.junit.jupiter.api.Test;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.boot.test.context.SpringBootTest;

    @SpringBootTest
    public class WishListRepositoryTest {

        // WishListRepository를 spring으로부터 주입받음
        @Autowired
        private WishListRepository wishListRepository;

        // 테스트에 많이 사용될 것 같은 메서드 따로 빼서 구현
        // 객체 생성 메서드
        private WishListEntity create() {
            var wishList = new WishListEntity();
            wishList.setTitle("title");
            wishList.setCategory("category");
            wishList.setAddress("address");
            wishList.setRoadAddress("roadAddress");
            wishList.setHomepageLink("");
            wishList.setImageLink("");
            wishList.setVisit(false);
            wishList.setVisitCount(0);
            wishList.setLastVisitDate(null);

            // 디폴트값으로 만들어서 리턴시킴
            return wishList;
        }

        // 네가지 모두 테스트 (+ 이미 데이터 존재하는 경우 count값(index) 증가하는지 확인 테스트)
        // 저장
        @Test
        public void saveTest() {
            var wishListEntity = create();
            var expected = wishListRepository.save(wishListEntity); // save에 대한 결과
            
            // 결과 기대값 예측
            // null이면 안됨
            Assertions.assertNotNull(expected);
            // 첫번째 데이터를 기대하고, 그것이 첫번째 인덱스(1)를 가지고 있으면 정상적으로 save 되었음을 알 수 있음
            Assertions.assertEquals(1, expected.getIndex());

        }

        // 값을 update했을 때 index값 변하는지 Test
        @Test
        public void updateTest() {
            var wishListEntity = create();
            var expected = wishListRepository.save(wishListEntity); // save에 대한 결과(expected == 1)

            // 1번 index에 대해서 update (title만 변경)
            expected.setTitle("update test");
            var saveEntity = wishListRepository.save(expected);

            // title이 제대로 update되었는지 확인
            Assertions.assertEquals("update test", saveEntity.getTitle());
            // count(index)가 증가했는지 확인
            // title만 변경했으므로 전체 리스트의 크기는 그대로 1이여야 함!
            Assertions.assertEquals(1, wishListRepository.listall().size());
        }

        // 검색 (해당 엔티티 찾아오기)
        @Test
        public void findByIdTest() {
        
            // 값을 찾기 위해서도 저장 먼저 필요
            var wishListEntity = create();
            wishListRepository.save(wishListEntity);
            
            // expected 값은 따로 찾기 (optional -> optional값은 항상 있기 때문에 notNull 의미가 없음)
            // 1번이라는 값을 찾았을 때
            var expected = wishListRepository.findById(1);
            // 안에 값이 있으면
            Assertions.assertEquals(true, expected.isPresent());
            // 데이터를 꺼냈을 때 인덱스가 1이어야 함 (기대)
            Assertions.assertEquals(1, expected.get().getIndex());

        }
        // 삭제
        @Test
        public void deleteTest() {

            // 삭제하기 위해서도 save먼저 필요
            var wishListEntity = create();
            wishListRepository.save(wishListEntity);

            // 1번을 찾아서 지워줌
            wishListRepository.deleteById(1);

            // 기대하는 값
            int count = wishListRepository.listall().size();
            // 기대값 체크
            // (데이터 넣었다가 삭제했으므로 전체 리스트의 크기는 0)
            Assertions.assertEquals(0, count);

        }

        // 전부 출력
        @Test
        public void listAllTest() {
            // 여러 개 save하여 테스트
            var wishListEntity1 = create();
            wishListRepository.save(wishListEntity1);

            var wishListEntity2 = create();
            wishListRepository.save(wishListEntity2);

            // 기대하는 값
            int count = wishListRepository.listall().size();
            // 기대값 체크
            // (데이터 두 개 넣었으므로 전체 리스트의 크기는 2)
            Assertions.assertEquals(2, count);
            
        }
    }
    // 특별한 에러가 없으면 잘 찾아지는 것!
    ```