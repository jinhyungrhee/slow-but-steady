# Annotation 정리

- Spring에는 수많은 annotation 존재
- 많이 코딩해보면서 몸에 익히는 것이 중요

|Annotation|의미|
|--|--|
|@SpringBootApplication|Spring boot application으로 설정|
|@Controller|View를 제공하는 controller로 설정 / ViewResolver사용 / response가 기본적으로 HTML 형태|
|@RestController|Rest API를 제공하는 controller로 설정 / response가 기본적으로 object mapper를 통한 JSON 형태|
|@RequestMapping|URL 주소를 맵핑 / 원하는 Http Method지정 / 지정하지 않으면 모든 Http Method가 동작함 / 이를 세분화시킨 것이 아래의 Mapping들|
|@GetMapping|Http GetMethod URL 주소 맵핑|
|@PostMapping|Http PostMethod URL 주소 맵핑|
|@PutMapping|Http PutMethod URL 주소 맵핑|
|@DeleteMapping|Http DeleteMethod URL 주소 맵핑|
|@ReqeustParam|URL Query Parameter 맵핑 / URL에 query parameter로 들어오는 형태를 지정할 때 사용|
|@RequestBody|Http Body를 Parsing 맵핑 / Http Body에 들어있는 JSON을 Object로 맵핑하기 위해 사용|
|@Valid|POJO Java class의 검증|
|@Configuration|1개 이상의 bean을 등록할 때 설정 / Spring의 configuration을 설정할 때 사용|
|@Component|1개의 Class 단위로 등록할 때 사용|
|@Bean|1개의 외부 library로부터 생성한 객체를 등록할 때 사용 / 직접 new로 객체 생성한 뒤 Bean으로 등록|
|@Autowired|DI를 위한 곳에 사용 / 명시적으로 주입받고 싶은 곳에 사용(기본적으로 생성자로 된 메서드에 들어오는 건 spring이 알아서 주입)|
|@Qualifier|@Autowired 사용 시 bean이 2개 이상일 때 명시적으로 사용|
|@Resource|@Autowired + @Qualifier의 개념으로 이해|
|@Aspect|AOP 적용시 사용|
|@Before|AOP 메소드 이전 호출 지정|
|@After|AOP 메소드 호출 이후 지정 / 예외 발생 포함|
|@Around|AOP 이전,이후 모두 포함 / 예외 발생 포함|
|@AfterReturning|AOP 메소드의 호출이 정상일 때만(메소드가 정상적으로 실행되었을 때만) 실행|
|@AfterThrowing|AOP시 해당 메소드가 예외 발생 시 지정|