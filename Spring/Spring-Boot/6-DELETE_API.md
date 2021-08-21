# DELETE Method

- DELETE

    - 리소스 삭제
    - Delete
    - 멱등성 O
        - 삭제된 데이터나 현재 있는 데이터나 삭제된 결과는 동일하기 때문
    - 안정성 X
        - 삭제하는 순간 데이터가 삭제됨
    - Path Variable 사용
    - Query Parameter로 값을 받기도 함
    - DataBody에 값을 넣을 수는 있지만 권장하는 방법은 아님
        - 보통 데이터베이스 인덱스 아이디 값이나 사용자의 unique한 값으로 사용함

- Delete Request

    - `http://localhost:8080/api/delete/100?account=user100`
        - Path Variable : 100 (100번째 유저)
        - Query Parameter : ?account=user100 (유저 계정)
    - Delete 경우 Request가 틀리지 않는 이상 200 리턴
        - 삭제가 제대로 처리 되었거나 데이터가 없는 상태에서 삭제를 요청한 경우 데이터가 존재하지 않는 것은 동일하기 때문에(**멱등성**) 항상 똑같은 응답을 받게 됨!

- 정리
    - DELETE는 GET과 동일하지만 리소스를 삭제하는 동작만 차이가 있음!
    - "리소스가 존재하지 않습니다"라는 에러 값을 던질 필요가 없음!
        - 이전에 존재해서 삭제한 것이나 이미 삭제가 되어서 없는 상태에서 다시 삭제를 요청한 것이나 결과적으로 같은 상태이기 때문 (멱등성) => 200 리턴

- 코드 정리

    - DeleteApiController.java
    ```java
    @RestController
    @RequestMapping("/api")
    public class DeleteApiController {

        // Path Variable로 삭제할 userId 받을 예정
        // Query Parameter로는 사용자 계정 받음
        @DeleteMapping("/delete/{userId}")
        public void delete(@PathVariable String userId, @RequestParam String account) {

            System.out.println(userId);
            System.out.println(account);
        }
    }
    ```
