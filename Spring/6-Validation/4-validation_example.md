# Validation 모범 사례

- 이전까지는 Response가 Client 입장에서는 친절하지 않았음
- Global Exception 처리 + Spring Validation을 통해 Client가 잘 활용하도록 만들어줄 수 있음

## 특정 클래스에서만 동작하는 Advice로 만들기

- basePackageClasses 속성 사용
    - `@RestControllerAdvice(basePackageClasses = ApiController.class)` 
- 더이상 Global하지 않기 때문에 이름도 바꿔줌 => 'ApiControllerAdvice'
    - advice/ApiControllerAdvice.java
        ```java
        @RestControllerAdvice(basePackageClasses = ApiController.class)
        public class ApiControllerAdvice {

            @ExceptionHandler(value = Exception.class)
            public ResponseEntity exception(Exception e){
                // 에러난 것이 어떤 클래스인지 확인
                System.out.println(e.getClass().getName());
                // Internal Server Error에 body 빈 상태로 보냄
                return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");
            }

            @ExceptionHandler(value = MethodArgumentNotValidException.class)
            public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e){
                System.out.println("Global Controller Adivce");
                // body에 메시지 담아서 리턴
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
            }
            
        }
        ```

## 다시 GET으로 빈 값 받아보기

- Talend API GET request
    - `http://localhost:8080/api/user?name&age`

- console
    ```shell
    java.lang.NullPointerException
    ```

- Null이 들어오면 안 됨 => **validation 필요!**
    1. Controller 단위에다가 `@Validated` annotation 붙임 --- (1)
    2. Request Parameter에다가 annotation 붙임 --- (2)
    - controller/ApiController.java
        ```java
        @RestController
        @RequestMapping("/api/user")
        @Validated // (1)
        public class ApiController {

            @GetMapping("")
            public User get(
                    @Size(min = 2) // (2)
                    @RequestParam String name,
                    
                    @NotNull // (2)
                    @Min(1)  // (2)
                    @RequestParam Integer age){
                User user = new User();
                user.setName(name);
                user.setAge(age);

                // 에러 발생시키기 (required = false) : 값 넣어주지 않아도 error 발생 X
                // 우리가 age 값을 넣어주지 않으면 null pointer error 발생
                int a = 10 + age;

                return user;
            }
            @PostMapping("")
            public User post(@Valid @RequestBody User user){
                System.out.println(user);

                return user;

            }

            @ExceptionHandler(value = MethodArgumentNotValidException.class)
            public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e){
                System.out.println("api controller");
                // body에 메시지 담아서 리턴
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
            }

        }
        ```
        ➡ @Validated에 의해서 Reqeust Parameter 변수들도 우리가 검증할 수 있게 됨!

    - 이렇게 변경했을 때
        - 빈 값으로 GET 요청 시(http://localhost:8080/api/user?name&age)
            - console에 리턴되는 에러 메시지
                ```shell
                org.springframework.web.bind.MissingServletRequestParameterException
                ```
        - 유효하지 않은 값으로 GET 요청 시(http://localhost:8080/api/user?name=a&age=1)
            - console에 리턴되는 에러 메시지
                ```shell
                javax.validation.ConstraintViolationException
                ```
        - 이것들은 ApiControllerAdvice의 methodArgumentNotValidException()에서 처리된 것이 아니라 **ApiControllerAdvice의 exception()**으로 처리된 것임!
            - mssingServletRequestParameterException()와 constraintViolationException()을 추가로 정의하여 Validation 진행

## 여러 가지 상황에 맞게 Exception 처리

1. methodArgumentNotValidException()
    - @Validated를 한 경우 값이 올바르지 않거나 특정한 값이 존재하지 않을 때 발생

2. constraintViolationException()
    - ???

3. missingServletRequestParameterException()
    - 빈 값이 들어왔을 때 발생

- 세 개 모두 구현함
    - advice/ApiControllerAdvice.java
    ```java
    @RestControllerAdvice(basePackageClasses = ApiController.class)
    public class ApiControllerAdvice {

        @ExceptionHandler(value = Exception.class)
        public ResponseEntity exception(Exception e){
            // 에러난 것이 어떤 클래스인지 확인
            System.out.println(e.getClass().getName());
            // 그 외의 에러는 Internal Server Error로 처리하도록 둠
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");
        }

        // 세 가지 모두 Client의 잘못 => Bad Request
        @ExceptionHandler(value = MethodArgumentNotValidException.class)
        public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        }

        @ExceptionHandler(value = ConstraintViolationException.class)
        public ResponseEntity constraintViolationException(ConstraintViolationException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        }

        @ExceptionHandler(value = MissingServletRequestParameterException.class)
        public ResponseEntity missingServletRequestParameterException(MissingServletRequestParameterException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        }

    }
    ```

- Talend API POST로 요청
    - POST Request Body
        ```js
        {
        "name" : "",
        "age" : 0
        }
        ```

- 각각의 return 코드에 break point 걸고 디버깅
    - methodArgumentNotValidException()에서 걸리는 것 확인
        - 에러 정보를 자세히 확인해보면 BindingResult 항목이 존재
    - 각 에러들을 돌면서 field 확인
        ```java
        @ExceptionHandler(value = MethodArgumentNotValidException.class)
        public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e){
            // 디버깅 해보면 여기에서 에러가 발생했고 에러 정보를 보면 BindingResult 항목이 존재
            BindingResult bindingResult = e.getBindingResult();
            // 각 에러들을 돌면서 Field 확인
            bindingResult.getAllErrors().forEach(error -> {
                // FieldError로 형변환
                FieldError field = (FieldError) error;

                String fieldName = field.getField();
                String message = field.getDefaultMessage();
                // 어떤 값이 잘못들어갔는지 출력해서 확인
                String value = field.getRejectedValue().toString();

                System.out.println("---------------");
                System.out.println(fieldName);
                System.out.println(message);
                System.out.println(value);
            });

            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        }
        ```

    - console 출력 결과
        ```shell
        ---------------
        age
        1 이상이어야 합니다
        0
        ---------------
        name
        크기가 1에서 10 사이여야 합니다

        ---------------
        name
        비어 있을 수 없습니다
        ```

- GET request도 확인(빈 값)
    - http://localhost:8080/api/user?name&age

- Response
    - 400 error 발생
        - ApiController에서 Validate가 실패한 것!
    - Response Body(에러 메시지)
        ```
        Required request parameter 'age' for method parameter type Integer is present but converted to null
        # 강의에서는
        # Required Integer parameter 'age' is not present
        ```
    - 이 메시지는 누가 만들었을까? => `디버깅`으로 확인

- 각각의 return 코드에 break point 걸고 디버깅
    - missingServletRequestParameterException()에 걸리는 것 확인
        - e를 확인해보면 해당 매개변수 안에 '값'이 안들어있기 때문에 에러 발생한 것
        - '메시지' 직접 만들어주기
        ```java
        @ExceptionHandler(value = MissingServletRequestParameterException.class)
        public ResponseEntity missingServletRequestParameterException(MissingServletRequestParameterException e){

            String fieldName = e.getParameterName();
            String fieldType = e.getParameterType();
            String invalidValue = e.getMessage();

            System.out.println(fieldName);
            System.out.println(fieldType);
            System.out.println(invalidValue);


            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        }
        ```

    - 다시 한번 빈 값으로 GET 요청해보면
        - console
            ```
            age
            Integer
            Required request parameter 'age' for method parameter type Integer is present but converted to null
            ```
        - 'age'라는 필드에 'Integer'타입이고 'age라는 Integer값이 꼭 필요함'
            - 하지만 지금은 빈 값으로 보내서 null로 바뀐 것

    - `age = 0`, `name을 빈 값`으로 GET 요청해보면 (http://localhost:8080/api/user?name&age= 0)
        - Response Body
            ```
            get.name: 크기가 2에서 2147483647 사이여야 합니다, get.age: 1 이상이어야 합니다
            ```
        
        - console
            ```
            ConstraintViolationImpl{interpolatedMessage='크기가 2에서 2147483647 사이여야 합니다', propertyPath=get.name, rootBeanClass=class com.example.exception.controller.ApiController, messageTemplate='{javax.validation.constraints.Size.message}'}
            ConstraintViolationImpl{interpolatedMessage='1 이상이어야 합니다', propertyPath=get.age, rootBeanClass=class com.example.exception.controller.ApiController, messageTemplate='{javax.validation.constraints.Min.message}'}
            ```
        - 즉, argument는 잘 맞았지만 validation에서 에러가 발생한 것 (=입력 값이 유효한 값이 아닌 것)
            - 바로 이때 **constraintViolationException()** 메서드를 탐!
                - console 메시지 직접 만들어주기
                    ```java
                    @ExceptionHandler(value = ConstraintViolationException.class)
                    public ResponseEntity constraintViolationException(ConstraintViolationException e){
                        // 이 Exception은 어떠한 Field가 잘못되었는지에 관한 정보를 담고 있음!
                        // 매개변수 안에 여러가지 에러들이 담겨 있음
                        e.getConstraintViolations().forEach(error ->{
                            // console 에러 메시지 만들기
                            String field = error.getLeafBean().toString();
                            String message = error.getMessage();
                            String invalidValue = error.getInvalidValue().toString();

                            System.out.println("---------------");
                            System.out.println(field);
                            System.out.println(message);
                            System.out.println(invalidValue);

                        });
                        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
                    }
                    ```
                - console 메시지 확인
                    - field 값이 제대로 출력되지 않음(문제 발생)
                    ```
                    ---------------
                    com.example.exception.controller.ApiController@2f8d7d27
                    1 이상이어야 합니다
                    0
                    ---------------
                    com.example.exception.controller.ApiController@2f8d7d27
                    크기가 2에서 2147483647 사이여야 합니다
                    ```

                - (문제 해결) Stream을 생성한 뒤 List로 만들어서 가져오기
                    ```java
                    @ExceptionHandler(value = ConstraintViolationException.class)
                    public ResponseEntity constraintViolationException(ConstraintViolationException e){
                        // 이 Exception은 어떠한 Field가 잘못되었는지에 관한 정보를 담고 있음!
                        // 매개변수 안에 여러가지 에러들이 담겨 있음
                        e.getConstraintViolations().forEach(error ->{
                            // console 에러 메시지 만들기

                            // iterator 또는 splitter를 통해 Stream 만들기
                            Stream<Path.Node> stream = StreamSupport.stream(error.getPropertyPath().spliterator(), false);
                            // Stream을 List로 변경
                            List<Path.Node> list = stream.collect(Collectors.toList());
                            
                            // field명만 List에서 가져옴
                            String field = list.get(list.size() -1).getName();
                            String message = error.getMessage();
                            String invalidValue = error.getInvalidValue().toString();

                            System.out.println("---------------");
                            System.out.println(field);
                            System.out.println(message);
                            System.out.println(invalidValue);

                        });
                        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
                    }
                    ```

                - console 메시지 정상적으로 출력
                    ```
                    ---------------
                    age
                    1 이상이어야 합니다
                    0
                    ---------------
                    name
                    크기가 2에서 2147483647 사이여야 합니다
                    ```

- 전체 코드로 보기
    - advice/ApiControllerAdvice.java
        ```java
        @RestControllerAdvice(basePackageClasses = ApiController.class)
        public class ApiControllerAdvice {

            @ExceptionHandler(value = Exception.class)
            public ResponseEntity exception(Exception e){
                // 에러난 것이 어떤 클래스인지 확인
                System.out.println(e.getClass().getName());
                // 그 외의 에러는 Internal Server Error로 처리하도록 둠
                return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");
            }

            // 세 가지 모두 Client의 잘못 => Bad Request
            @ExceptionHandler(value = MethodArgumentNotValidException.class)
            public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e){
                // 디버깅 해보면 여기에서 에러가 발생했고 에러 정보를 보면 BindingResult 항목이 존재
                BindingResult bindingResult = e.getBindingResult();
                // 각 에러들을 돌면서 Field 확인
                bindingResult.getAllErrors().forEach(error -> {
                    // FieldError로 형변환
                    FieldError field = (FieldError) error;

                    String fieldName = field.getField();
                    String message = field.getDefaultMessage();
                    // 어떤 값이 잘못들어갔는지 출력
                    String value = field.getRejectedValue().toString();

                    System.out.println("---------------");
                    System.out.println(fieldName);
                    System.out.println(message);
                    System.out.println(value);
                });

                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
            }

            @ExceptionHandler(value = ConstraintViolationException.class)
            public ResponseEntity constraintViolationException(ConstraintViolationException e){
                // 이 Exception은 어떠한 Field가 잘못되었는지에 관한 정보를 담고 있음!
                // 매개변수 안에 여러가지 에러들이 담겨 있음
                e.getConstraintViolations().forEach(error ->{
                    // console 에러 메시지 만들기
                    // iterator 또는 splitter를 통해 Stream 만들기
                    Stream<Path.Node> stream = StreamSupport.stream(error.getPropertyPath().spliterator(), false);
                    // Stream을 List로 변경
                    List<Path.Node> list = stream.collect(Collectors.toList());
                    
                    // field명만 list에서 가져옴
                    String field = list.get(list.size() -1).getName();
                    String message = error.getMessage();
                    String invalidValue = error.getInvalidValue().toString();

                    System.out.println("---------------");
                    System.out.println(field);
                    System.out.println(message);
                    System.out.println(invalidValue);

                });
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
            }

            @ExceptionHandler(value = MissingServletRequestParameterException.class)
            public ResponseEntity missingServletRequestParameterException(MissingServletRequestParameterException e){
                // console 에러 메시지 만들기
                String fieldName = e.getParameterName();
                String fieldType = e.getParameterType();
                String invalidValue = e.getMessage();

                System.out.println(fieldName);
                System.out.println(fieldType);
                System.out.println(invalidValue);


                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
            }
        }
        ```

    - 어떤 에러가 발생하더라도 동일한 값들을 출력할 수 있도록 해놓은 것

## ErrorResponse 내려주기

- ErrorResponse 클래스 생성
    - dto/ErrorResponse.java
        ```java
        public class ErrorResponse {

            String statusCode;
            String RequestUrl;
            String code;
            String message;
            String resultCode;

            List<Error> errorList;

            public String getStatusCode() {
                return statusCode;
            }

            public void setStatusCode(String statusCode) {
                this.statusCode = statusCode;
            }

            public String getRequestUrl() {
                return RequestUrl;
            }

            public void setRequestUrl(String requestUrl) {
                RequestUrl = requestUrl;
            }

            public String getCode() {
                return code;
            }

            public void setCode(String code) {
                this.code = code;
            }

            public String getMessage() {
                return message;
            }

            public void setMessage(String message) {
                this.message = message;
            }

            public String getResultCode() {
                return resultCode;
            }

            public void setResultCode(String resultCode) {
                this.resultCode = resultCode;
            }

            public List<Error> getErrorList() {
                return errorList;
            }

            public void setErrorList(List<Error> errorList) {
                this.errorList = errorList;
            }
        }
        ```
    
    - dto/Error.java
        ```java
        public class Error {

            private String field;
            private String message;
            private String invalidValue;

            public String getField() {
                return field;
            }

            public void setField(String field) {
                this.field = field;
            }

            public String getMessage() {
                return message;
            }

            public void setMessage(String message) {
                this.message = message;
            }

            public String getInvalidValue() {
                return invalidValue;
            }

            public void setInvalidValue(String invalidValue) {
                this.invalidValue = invalidValue;
            }
        }
        ```

    - advice/ApiControllerAdvice.java
        - errorMessage 객체 생성
        - errorList에 추가
        - errorResponse를 만들어줌
            - HttpServletRequest : 매개변수로 현재 Request 받아오는 것 가능!
        - ResponseEntity Body에 errorResponse객체 넣어줌
        ```java
        @RestControllerAdvice(basePackageClasses = ApiController.class)
        public class ApiControllerAdvice {

            @ExceptionHandler(value = Exception.class)
            public ResponseEntity exception(Exception e){
                // 에러난 것이 어떤 클래스인지 확인
                System.out.println(e.getClass().getName());
                // 그 외의 에러는 Internal Server Error로 처리하도록 둠
                return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");
            }

            // 세 가지 모두 Client의 잘못 => Bad Request
            @ExceptionHandler(value = MethodArgumentNotValidException.class)
            public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e, HttpServletRequest httpServletRequest){
                // 매개변수로 현재 Request 받아오는 것 가능!

                // Error Response 내려주기
                List<Error> errorList = new ArrayList<>();

                // 디버깅 해보면 여기에서 에러가 발생했고 에러 정보를 보면 BindingResult 항목이 존재
                BindingResult bindingResult = e.getBindingResult();
                // 각 에러들을 돌면서 Field 확인
                bindingResult.getAllErrors().forEach(error -> {
                    // FieldError로 형변환
                    FieldError field = (FieldError) error;
                    // field 만들기
                    String fieldName = field.getField();
                    String message = field.getDefaultMessage();
                    // 어떤 값이 잘못들어갔는지 출력
                    String value = field.getRejectedValue().toString();
                    

                    // 에러 객체 만들기
                    Error errorMessage = new Error();
                    errorMessage.setField(fieldName);
                    errorMessage.setMessage(message);
                    errorMessage.setInvalidValue(value);
                    // errorList에 에러 메시지 추가
                    errorList.add(errorMessage);
                    
                });

                // response에서 넣어줌
                ErrorResponse errorResponse = new ErrorResponse();
                errorResponse.setErrorList(errorList);
                errorResponse.setMessage("");
                // 어떤 정보를 요청했고 어떤 에러가 발생했는지 (URI)
                errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
                errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
                errorResponse.setResultCode("FAIL");
                
                // 작성한 메시지 Response Body에 넣어줌
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
            }

            @ExceptionHandler(value = ConstraintViolationException.class)
            public ResponseEntity constraintViolationException(ConstraintViolationException e, HttpServletRequest httpServletRequest){
                // 이 Exception은 어떠한 Field가 잘못되었는지에 관한 정보를 담고 있음!
                // 매개변수 안에 여러가지 에러들이 담겨 있음

                List<Error> errorList = new ArrayList<>();

                e.getConstraintViolations().forEach(error ->{
                    // console 에러 메시지 만들기
                    // iterator 또는 splitter를 통해 Stream 만들기
                    Stream<Path.Node> stream = StreamSupport.stream(error.getPropertyPath().spliterator(), false);
                    // Stream을 List로 변경
                    List<Path.Node> list = stream.collect(Collectors.toList());
                    
                    // field명만 list에서 가져옴
                    String field = list.get(list.size() -1).getName();
                    String message = error.getMessage();
                    String invalidValue = error.getInvalidValue().toString();

                    // 에러 객체 만들기
                    Error errorMessage = new Error();
                    errorMessage.setField(field);
                    errorMessage.setMessage(message);
                    errorMessage.setInvalidValue(invalidValue);
                    // errorList에 에러 메시지 추가
                    errorList.add(errorMessage);

                });

                // response에서 넣어줌
                ErrorResponse errorResponse = new ErrorResponse();
                errorResponse.setErrorList(errorList);
                errorResponse.setMessage("");
                // 어떤 정보를 요청했고 어떤 에러가 발생했는지 (URI)
                errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
                errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
                errorResponse.setResultCode("FAIL");

                // 작성한 메시지 Response Body에 넣어줌
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
            }

            @ExceptionHandler(value = MissingServletRequestParameterException.class)
            public ResponseEntity missingServletRequestParameterException(MissingServletRequestParameterException e, HttpServletRequest httpServletRequest){

                List<Error> errorList = new ArrayList<>();

                // console 에러 메시지 만들기
                String fieldName = e.getParameterName();
                // 어차피 잘못들어온 것이기 때문에 값이 없음
                String invalidValue = e.getMessage();

                // 에러 객체 만들기
                Error errorMessage = new Error();
                errorMessage.setField(fieldName);
                errorMessage.setMessage(e.getMessage());
                // errorList에 에러 메시지 추가
                errorList.add(errorMessage);

                // response에서 넣어줌
                ErrorResponse errorResponse = new ErrorResponse();
                errorResponse.setErrorList(errorList);
                errorResponse.setMessage("");
                // 어떤 정보를 요청했고 어떤 에러가 발생했는지 (URI)
                errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
                errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
                errorResponse.setResultCode("FAIL");

                // 작성한 메시지 Response Body에 넣어줌
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
            }
        }
        ```

    - GET 요청 시 error Response
        - GET request
            - http://localhost:8080/api/user?name&age= 0
        - Response Body
            ```js
            {
            "statusCode": "400 BAD_REQUEST",
            "code": null,
            "message": "",
            "resultCode": "FAIL",
            "errorList":[
                {
                "field": "name",
                "message": "크기가 2에서 2147483647 사이여야 합니다",
                "invalidValue": ""
                },
                {
                "field": "age",
                "message": "1 이상이어야 합니다",
                "invalidValue": "0"
                }
            ],
            "requestUrl": "/api/user"
            }
            ```

    - POST 요청 시 error Response
        - POST request
            ```js
            {
            "name" : "",
            "age" : 0
            }
            ```
        - Response Body
            ```js
            {
            "statusCode": "400 BAD_REQUEST",
            "code": null,
            "message": "",
            "resultCode": "FAIL",
            "errorList":[
                {
                "field": "name",
                "message": "크기가 1에서 10 사이여야 합니다",
                "invalidValue": ""
                },
                {
                "field": "age",
                "message": "1 이상이어야 합니다",
                "invalidValue": "0"
                },
                {
                "field": "name",
                "message": "비어 있을 수 없습니다",
                "invalidValue": ""
                }
            ],
            "requestUrl": "/api/user"
            }
            ```

    ➡ Client가 우리에게 요청하는 값들을 검증하는 부분을 일관되게 전부 처리해줌
    ➡ methodArgumentNotValidException(), constraintViolationException(), missingServletRequestParameterException() 세 개의 메서드만 잘 정의한다면 내가 만든 서버를 이용하는 클라이언트는 편리하게 서버를 이용할 수 있음 (친절하게 에러 메시지를 내려줄 수 있음!)


## 정리

- Spring Framework는 방대한 양을 가진 서버 프레임워크(=엔터프라이즈 프레임워크)임
- ApiController가 4~5개 되는 경우 또는 주소를 10개 이상 제공하는 경우(매우 복잡한 경우)
    - 일관되게 적용시키기 위해서는 `Spring Validaiton`과 `Global Exception`, `ControllerAdvice`를 통해서 예외들에 대해서 숨길 것은 숨기며 일반적인 메시지를 내보내는 것이 가능함!