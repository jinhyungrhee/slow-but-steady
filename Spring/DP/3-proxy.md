# Proxy Pattern

- Proxy 패턴
    - Proxy는 대리인이라는 의미로 뭔가를 대신해서 처리하는 것
    - Proxy Class를 통해서 대신 전달하는 형태로 설계됨
    - 실제 Client는 Proxy로부터 결과를 받음
    - 개방폐쇄 원칙(OCP)과 의존역전 원칙(DIP)를 따름
        - Cache의 기능으로도 활용 가능
        - Spring에서는 AOP를 proxy 패턴으로 사용
            - AOP : 일괄적으로 특정 패키지에 전후에 있는 기능을 넣을 수 있는 것
            - 특정한 메서드 앞 뒤로 내가 원하는 기능을 주거나 앞 뒤로 넘어가는 argument에 대해서 조작 가능
            - 흩어져 있는 공통된 기능을 하나로 묶어줄 수도 있음
                - HTTP client가 어딘가로 통신하려고 할 때 HTTP Client code가 흩어져 있거나 REST Client 서비스가 뭉쳐있다고 하면 그 안에 있는 메서드들에 대해서 시간을 체크할 수 있음
                - DB에 insert하거나 transaction이 있는 쪽에 시간 관련 aop를 넣어서 **현재 시스템이 어느 부분에서 오래 걸리고 있는지, 어떤 메서드가 오래 걸려서 현재 서버가 느린 상태인지 확인 가능!**
            - ex) 시스템 내에서 특정 메서드의 수행 시간을 측정할 때 사용 

1. Cache 기능

    - 구현체 자체는 건드리지 않고 캐싱하는 기능 추가 

    - 브라우저 인터페이스(IBrowser.java)
    ```java
    public interface IBrowser {
        // show()메서드가 호출되면 Html을 리턴하는 형태
        Html show();
    }
    ```

    - Html 클래스(Html.java)
    ```java
    public class Html {
        // Html은 기본적으로 url을 가지고 있음
        private String url;
        
        // default 생성자에서 url 받아서 Html을 로딩하는 형태
        public Html(String url){
            this.url = url;
        }   
    }
    ```

    - 브라우저 클래스(Browser.java) : 크롬 등 url을 입력받아 화면에 보여주는 기능
    ```java
    public class Browser implements IBrowser{

        private String url;

        // default 생성자에서 url을 받음
        public Browser(String url){
            this.url = url;
        }

        @Override
        public Html show() {
            System.out.println("browser loading html from : "+url);
            // 새로운 Html파일 넘김
            return new Html(url);
        }
    }
    ```


    - Main.java
        - 프록시 사용 X : caching 없이 5번 모두 새롭게 html을 생성
    ```java
    public class Main {

        public static void main(String[] args) {
            
            Browser browser = new Browser("www.naver.com");
            browser.show();
            browser.show();
            browser.show();
            browser.show();
            browser.show();

    }
    }
    ```

    - 프록시 클래스 추가(BrowserProxy.java)
    ```java
    public class BrowserProxy implements IBrowser{

        private String url;
        // Html caching하기 위해 정의
        private Html html;

        // default 생성자로 url 받음
        public BrowserProxy(String url){
            this.url = url;
        }
        
        @Override
        public Html show() {
            // caching code
            // 기존 html이 없으면 새로운 html 생성
            if(html == null){
                this.html = new Html(url);
                System.out.println("BrowserProxy loading html from : "+url);
            }
            // 기존 html이 있으면 가지고 있는 html 리턴
            System.out.println("BrowserProxy use cache html : "+url);
            return html;
        }
    }
    ```

    - Main.java
        - 프록시 사용 O : 처음에만 html 객체 생성하고 나머지는 모두 기존 html 가져옴
    ```java
    public class Main {

        public static void main(String[] args) {
            
            IBrowser browser = new BrowserProxy("www.naver.com");
            browser.show();
            browser.show();
            browser.show();
            browser.show();
            browser.show();

        }
    }
    ```

2. AOP 기능

- AOP브라우저 클래스 (AopBrowser.java)
```java
public class AopBrowser implements IBrowser {

    private String url;
    private Html html;
    // aop는 '관점지향'임 - 앞과 뒤 체크
    // functional interface runnable 사용
    private Runnable before;
    private Runnable after;

    // default 생성자로 argument 3개 받음
    public AopBrowser(String url, Runnable before, Runnable after) {
        this.url =url;
        this.before = before;
        this.after = after;
    }
    
    @Override
    public Html show() {
        // html 로딩 시간 체크
        before.run();

        if (html == null) {
            this.html = new Html(url);
            System.out.println("AopBrowser html loading from : "+url);
            // 메서드 자체가 워낙 빠르므로 sleep() - try/catch 사용
            try {
                Thread.sleep(1500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        after.run();

        System.out.println("AopBrowser html cache : "+url);
        return html;
    }
}
```

- Main.java
```java
public class Main {

    public static void main(String[] args) {
      
        // 시간체크 - 동시성
        AtomicLong start = new AtomicLong();
        AtomicLong end = new AtomicLong();

        IBrowser aopBrowser = new AopBrowser("www.naver.com",
                // runnable 람다식 표현
                // 앞뒤로 실행시키고 싶은 메서드 람다식으로 넣어줌
                ()->{
                    System.out.println("before");
                    start.set(System.currentTimeMillis());
                },
                ()->{
                    long now = System.currentTimeMillis();
                    end.set(now - start.get());
                }
                );

        // 첫 번째 show()메서드가 걸린시간 : 1.5초
        aopBrowser.show();
        System.out.println("loading time : " + end.get());

        // 두 번째 show()메서드가 걸린시간 : 0초 (cache 제대로 작동)
        aopBrowser.show();
        System.out.println("loading time : " + end.get());
   }
}
```