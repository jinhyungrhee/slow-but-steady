# Singleton Pattern

- Singleton 패턴
    - 어떠한 **클래스(객체)가 유일하게 1개만 존재**할 때 사용
    - 서로 자원을 공유할 때 주로 사용
        - 실물 세계 : 프린터 공유
        - 프로그래밍 : TCP Socket 통신에서 서버와 연결된 connect 객체에 주로 사용
        - Spring : bean클래스/객체들은 singleton으로 관리됨
            - 직접 생성하지 않고 application context라는 것을 통해 spring에서 관리
    - 사용
        1. 기본적으로 default 생성자로 private으로 막아버림
        2. getInstance()라는 메서드를 통해서 생성되어 있는 객체를 가지고 오거나 객체가 없는 경우 새로 생성
        
    - 어떠한 클래스에서도 static 메서드를 통해서 getInstance()를 했을 때 동일한 객체를 얻을 수 있음!
    - getInstance()를 사용하는 것은 모두 Signleton이라고 생각하면 됨!

- 코드 예제 : 특정 서버와 통신 시 한 번 연결한 connect통해서 계속 사용

    - SocketClient.java
    ```java
    public class SocketClient {

        // singleton은 자기 자신을 객체로 가지고 있어야 함!
        private static SocketClient socketClient = null;

        // singleton은 기본생성자(default 생성자)를 통해 생성할 수 없도록 private으로 막는 것
        private SocketClient() {

        }
        // static 메서드를 통해서 getInstance() 메서드를 제공해야 함!
        // 바깥에서 어떠한 클래스에서라도 바로 SocketClient.getInstance() 메서드 접근 가능
        public static SocketClient getInstance() {

            // 현재 내가 가진 객체가 null인지 아닌지 check
            // null인 경우(없는 경우) 새로운 SocketClient 객체 생성 - 최초 한번만 생성
            if(socketClient == null){
                socketClient = new SocketClient();
            }
            // null이 아닌 경우(있는 경우) 자신이 가지고 있는 socketClient 리턴
            return socketClient;
        }

        public void connect() {
            System.out.println("connect");
        }

    }
    ```

    - AClazz.java
    ```java
    public class AClazz {
        // 각각의 class는 socketClient를 가지고 있음!
        private SocketClient socketClient;

        // 기본생성자에서 초기화시킴
        public AClazz() {
            //this.socketClient = new SocketClient(); // 디폴트 생성자 막아놨기 때문에 불가
            this.socketClient = SocketClient.getInstance(); // getInstance()이용해 socketClient할당!
        }

        // socketClient를 리턴해주는 get method 생성
        public SocketClient getSocketClient() {
            return this.socketClient;
        }
    }
    ```

    - BClazz.java
    ```java
    package com.company.design.singleton;

    public class BClazz {
        // 각각의 class는 socketClient를 가지고 있음!
        private SocketClient socketClient;
        
        // 기본생성자에서 초기화시킴
        public BClazz() {
            //this.socketClient = new SocketClient(); // 막아놨으므로 불가
            this.socketClient = SocketClient.getInstance(); // getInstance()이용해 socketClient 할당!
        }

        // socketClient를 리턴해주는 get method
        public SocketClient getSocketClient() {
            return this.socketClient;
        }
    }
    ```

    - Main.java
    ```java
    public class Main {

        public static void main(String[] args) {
            // 각각 서로다른 클래스로부터 인스턴스 생성
            AClazz aClazz = new AClazz();
            BClazz bClazz = new BClazz();

            // 각각의 클래스에서 가져온 두 클라이언트가 동일한지 확인
            SocketClient aClient = aClazz.getSocketClient();
            SocketClient bClient = bClazz.getSocketClient();

            System.out.println("두개의 객체가 동일한가?");
            System.out.println(aClient.equals(bClient));
    }
    }
    ```
