# Swagger

## Swagger란

- 개발자가 개발한 REST API를 편리하게 문서화 해주는 프로젝트 
- 이를 통해서 관리 및 제3의 사용자가 내 프로젝트에 대해서 API를 편리하게 호출하고 테스트할 수 있도록 문서화해주는 라이브러리
- 다른 언어 프레임워크에도 존재
    - Spring은 어노테이션을 사용하여 내가 만든 컨트롤러를 모두 공개하거나 일부 숨기는 것 가능
    - Spring은 어노테이션을 사용하여 조금 더 디테일하게 설명 달아주는 것도 가능
- Spring Boot에서는 간단한게 `springfox-boot-starter`를 gradle dependencies에 추가해서 사용 가능
    - swagger UI같은 것들을 따로 설정해주지 않아도 사용 가능
- 주의!
    - **운영환경**과 같은 외부에 노출되면 안 되는 곳에는 사용X
    - 공개하더라도 막 수정해도 괜찮은 부분에서만 사용하는 것 추천
- 주요 어노테이션
    |Annotation|설명|
    |--|--|
    |@Api|클래스를 스웨거의 리소스로 표시|
    |@ApiOperation|특정 경로의 오퍼레이션 HTTP 메서드 설명|
    |@ApiParam|오퍼레이션 파라미터에 메타 데이터 설명|
    |@ApiResponse|오퍼레이션의 응답 지정|
    |@ApiModelProperty|모델의 속성 데이터를 설명|
    |@ApiImplicitParam|메서드 단위의 오퍼레이션 파라미터를 설명|
    |@ApiImplicitParams||    

## 프로젝트에서 Swagger 설정하기

- 초기 프로젝트 설정에는 Swagger가 없으므로 maven repository에서 가져와야 함!
    - springfox 검색 후 Springfox Boot Starter 클릭
        - 3.0.0 에서 gradle 코드 복사해서 가져오기
            - 이전에는 Springfox Swagger2(2.9.2)와 Springfox Swagger UI(2.9.2)를 많이 사용했음
- build.gradle dependencies에 붙여넣고 새로고침!
- 오른쪽 gradle 탭에 들어가서 dependency가 잘 걸려있는지 확인!
    - Dependencies/compileClasspath/

- 이렇게 설정이 완료되면, 앞으로 작성하는 모든 controller가 공개됨!!

## Swagger 사용하기

- ApiController 생성
    - controller/ApiController.java
        ```java
        @RestController
        @RequestMapping("/api")
        public class ApiController {

            @GetMapping("/hello")
            public String hello(){
                return "hello";
            }
        }
        ```

- 이제 Talend API 대신 Swagger-ui를 사용하여 테스트할 수 있음
    - http://localhost:9090/swagger-ui/
        - 뒤에 반드시 `/` 필요!
    - swagger-ui에 접속하면 우리가 작성한 controller들이 나타남
        - basic-error-controller
            - spring에서 기본적으로 생성하는 controller
        - api-controller
            - 우리가 작성한 controller
            - 여기에 우리가 만든 메서드들이 담겨 있음
    - Talend API에서는 일일이 주소를 설정해줘야 했지만 swagger-ui에서는 `try-it-out`과 `Execute` 버튼을 클릭하면 간단하게 요청이 보내짐

## 중간 정리

- 내가 만든 서버의 API를 내부/외부 사용자들에게 문서를 주지 않고도 swagger-ui만을 이용하여 직접 들어와서 test해볼 수 있도록 함
- 사용자들이 조금 더 알아볼 수 있도록 변경해주면 좋음!

## Swagger 설정하기

- case1) 하나는 path variable로 받고 하나는 query parameter로 받는 경우
    - @Api, @ApiParam 어노테이션 사용
        - controller/ApiController.java
            ```java
            // swagger-ui에서 외부에 보여지는 이름 설정
            @Api(tags = {"API 정보를 제공하는 Controller"})
            @RestController
            @RequestMapping("/api")
            public class ApiController {

                @GetMapping("/hello")
                public String hello(){
                    return "hello";
                }

                // 하나는 path variable로 받고 하나는 query parameter로 받음 
                @GetMapping("/plus/{x}")
                public int plus(
                        // 설명 보충하기 - 너무 많은 annotation은 가독성을 해칠 수 있음
                        @ApiParam(value = "x값")
                        @PathVariable int x,

                        @ApiParam(value = "y값")
                        @RequestParam int y){
                    return x+y;
                }
                
            }
            ```

- case2) request param을 object로 받는 경우(GET)

    - controller/ApiController.java
        ```java
        @Api(tags = {"API 정보를 제공하는 Controller"})
        @RestController
        @RequestMapping("/api")
        public class ApiController {

            @GetMapping("/hello")
            public String hello(){
                return "hello";
            }

            @GetMapping("/plus/{x}")
            public int plus(
                    @ApiParam(value = "x값")
                    @PathVariable int x,

                    @ApiParam(value = "y값")
                    @RequestParam int y){
                return x+y;
            }
            
            // request param을 object로 받는 경우
            // UserReq를 받는 GET 컨트롤러 생성
            @ApiResponse(code=502, message="사용자의 나이가 10살 이해일 때") // 에러에 대한 응답 설정
            @ApiOperation(value = "사용자의 이름과 나이를 리턴하는 메서드") // api 뒤에 붙는 설명
            @GetMapping("/user")
            public UserRes user(UserReq userReq) { // annotation을 여기에 붙이지 않고 UserReq/UserRes 안에서 붙임!
                return new UserRes(userReq.getName(), userReq.getAge());
            }
        }
        ```

    - dto/UserReq.java 생성
        ```java
        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        public class UserReq {

            @ApiModelProperty(value = "사용자의 이름", example = "steve", required = true)
            private String name;

            @ApiModelProperty(value = "사용자의 나이", example = "10", required = true)
            private int age;
        }
        ```

    - dto/UserRes.java 생성
        ```java
        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        public class UserRes {

            @ApiModelProperty(value = "사용자의 이름", example = "steve", required = true)
            private String name;

            @ApiModelProperty(value = "사용자의 나이", example = "10", required = true)
            private int age;
        }
        ```

- case3) request param을 object로 받는 경우(POST)
    - controller/ApiController.java
    ```java
    @Api(tags = {"API 정보를 제공하는 Controller"})
    @RestController
    @RequestMapping("/api")
    public class ApiController {

        @GetMapping("/hello")
        public String hello(){
            return "hello";
        }
        @GetMapping("/plus/{x}")
        public int plus(
                @ApiParam(value = "x값")
                @PathVariable int x,

                @ApiParam(value = "y값")
                @RequestParam int y){
            return x+y;
        }
        
        // request param을 object로 받는 경우

        @ApiResponse(code=502, message="사용자의 나이가 10살 이해일 때")
        @ApiOperation(value = "사용자의 이름과 나이를 리턴하는 메서드")
        @GetMapping("/user")
        public UserRes user(UserReq userReq) {
            return new UserRes(userReq.getName(), userReq.getAge());
        }

        // UserReq를 받는 POST 컨트롤러 생성
        @PostMapping("/user")
        public UserRes userPost(@RequestBody UserReq req){
            return new UserRes(req.getName(), req.getAge());
        }
    }
    ```

- case4) GET에 붙는 변수가 많을 때 일일이 swagger annotation 다는 것은 불편할 수 있음!
    - parameter에 붙이는 대신 메서드 자체에도 붙일 수 있음!
    - ApiController.java
        ```java
        @Api(tags = {"API 정보를 제공하는 Controller"})
        @RestController
        @RequestMapping("/api")
        public class ApiController {

            @GetMapping("/hello")
            public String hello(){
                return "hello";
            }

            // 메서드 자체에 swagger 어노테이션 붙이기 - 배열로 여러 가지 받을 수 있음
            @ApiImplicitParams({
                    @ApiImplicitParam(name = "x", value = "x 값", required = true, dataType = "int", paramType = "path"),
                    @ApiImplicitParam(name = "y", value = "y 값", required = true, dataType = "int", paramType = "query")
            })
            @GetMapping("/plus/{x}")
            public int plus(@PathVariable int x, @RequestParam int y){
                return x+y;
            }
            
            @ApiResponse(code=502, message="사용자의 나이가 10살 이해일 때")
            @ApiOperation(value = "사용자의 이름과 나이를 리턴하는 메서드") 
            @GetMapping("/user")
            public UserRes user(UserReq userReq) {
                return new UserRes(userReq.getName(), userReq.getAge());
            }

            @PostMapping("/user")
            public UserRes userPost(@RequestBody UserReq req){
                return new UserRes(req.getName(), req.getAge());
            }
        }
        ```

    - 메서드 안의 매개변수에 붙었던 annotation들을 위로 따로 빼놓은 것!