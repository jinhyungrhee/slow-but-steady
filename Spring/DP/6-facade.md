# Facade Pattern

- Facade 패턴

    - '건물의 앞쪽, 정면'이라는 뜻
        - 건물의 뒤쪽에 무엇이 있는지 우리는 알 수 없음
    - 여러 개이 객체와 실제 사용하는 서브 객체의 사이에 복잡한 의존관계가 있을 때, 중간에 facade라는 객체를 두고 여기에서 제공하는 interface만을 활용하여 기능을 사용하는 방식
    - 자신이 가지고 있는 각 클래스의 기능을 명확히 알아야 함!
    - 여러 개의 객체를 합쳐서 특정한 기능을 만들 때 사용
    - 여러 가지 객체의 **의존성**들을 내부로 숨겨주는 형태의 패턴

- 코드 예제

    - FTP 클래스(Ftp.java)
    ```java
    public class Ftp {
        // ftp는 port 22번으로 특정 host에 붙음
        private String host;
        private int port;
        private String path;
        
        // default 생성자에서 받음
        public Ftp(String host, int port, String path) {
            this.host = host;
            this.port = port;
            this.path = path;
        }
        
        // ftp가 제공하는 메서드
        // 1.원격체에 연결
        public void connect() {
            System.out.println("FTP host : "+host+" Port : "+port+"로 연결합니다.");
        }
        // 2.해당 디렉토리(path)로 이동
        public void moveDirectory() {
            System.out.println("FTP path : "+path+" 로 이동합니다.");
        }
        // 3.연결해제
        public void disConnect() {
            System.out.println("FTP 연결을 종료합니다.");
        }   
    }
    ```
    - Writer클래스(Writer.java)
    ```java
    public class Writer {
        // 만들 파일 이름
        private String fileName;

        public Writer(String fileName) {
            this.fileName = fileName;
        }
        
        // 제공 메서드
        // 1.파일 연결
        public void fileConnect() {
            String msg = String.format("Reader %s로 연결합니다", fileName);
            System.out.println(msg);
        }
        
        // 2. 파일에 내용 씀
        public void write() {
            String msg = String.format("Reader %s로 내용을 씁니다", fileName);
            System.out.println(msg);
        }

        // 3. 파일 연결 해제
        public void fileDisconnect() {
            String msg = String.format("Reader %s로 연결합니다", fileName);
            System.out.println(msg);
        }
    }
    ```
    
    - Reader 클래스(Reader.java)
    ```java
    public class Reader {

        // 읽어올 파일 이름
        private String fileName;

        // default 생성자에서 파일 이름 받음
        public Reader(String fileName) {
            this.fileName = fileName;
        }

        // Reader가 제공하는 메서드
        // 1.파일 연결
        public void fileConnect() {
            String msg = String.format("Reader %s로 연결합니다", fileName);
            System.out.println(msg);
        }
        // 2.파일에서 내용 읽어옴
        public void fileRead() {
            String msg = String.format("Reader %s의 내용을 읽어옵니다", fileName);
            System.out.println(msg);
        }
        // 3.파일 연결 해제
        public void fileDisconnect() {
            String msg = String.format("Reader %s로 연결 종료합니다", fileName);
            System.out.println(msg);
        }

    }
    ```

    - 각각의 객체에 의존하는 경우 (Main.java)
    ```java
    public class Main {

        public static void main(String[] args) {
            // facade를 사용하지 않으면 객체를 다 일일이 만들어야 하는 번거로움이 있음!
            // 각각의 객체에 의존
            Ftp ftpClient = new Ftp("www.foo.co.kr", 22, "/home/etc");
            ftpClient.connect();
            ftpClient.moveDirectory();

            Writer writer = new Writer("text.tmp");
            writer.fileConnect();
            writer.write();

            Reader reader = new Reader("text.tmp");
            reader.fileConnect();
            reader.fileRead();
            
            // 다 읽고 썼으면 끊는 것은 역순으로 진행
            reader.fileDisconnect();
            writer.fileDisconnect();
            ftpClient.disConnect();
        }
    }
    ```

    - **facade 클래스 생성**(SftpClient.java)
    ```java
    public class SftpClient {

        // 객체를 한번 감쌈으로써 SftpClient가 모든 의존성을 가져감
        private Ftp ftp;
        private Reader reader;
        private Writer writer;

        // 생성자에서 모두 받음
        public SftpClient(Ftp ftp, Reader reader, Writer writer) {
            this.ftp = ftp;
            this.reader = reader;
            this.writer =writer;
        }

        // host, port, path, fileName 네 가지 값만 받아도 객체를 이용할 수 있도록 오버로딩
        // host, port, path, fileName을 받아서 ftp, reader, writer 모두 생성 가능
        public SftpClient(String host, int port, String path, String fileName) {
            this.ftp = new Ftp(host, port, path);
            this.reader = new Reader(fileName);
            this.writer = new Writer(fileName);
        }

        // 여러 가지 객체를 합쳐서 새로운 복합적인 기능 생성
        // 새로운 인터페이스 제공
        public void connect() {
            ftp.connect();
            ftp.moveDirectory();
            writer.fileConnect();
            reader.fileConnect();
        }
        public void disConnect() {
            writer.fileDisconnect();
            reader.fileDisconnect();
            ftp.disConnect();
        }
        public void read() {
            reader.fileRead();
        }
        public void write() {
            writer.write();
        }
        
    }
    ```

    - **facade 객체 사용**(Main.java)
        - 여러 가지 의존성을 가진 것들을 새로운 인터페이스 형태로 제공
    ```java
    public class Main {

        public static void main(String[] args) {
            SftpClient sftpClient = new SftpClient("www.foo.co.kr", 22, "/home/etc", "text.tmp");
            sftpClient.connect();
            sftpClient.write();
            sftpClient.read();
            sftpClient.disConnect();

        }
    }
    ```