# Observer Pattern

- Observer 패턴

    - 변화가 일어났을 때 미리 등록된 다른 클래스에 통보해주는 패턴을 구현
    - Swing, JWT, GUI, Android등에서 event listener가 옵저버 패턴의 표준적인 예!
    - 특정한 이벤트(버튼 클릭 등)가 발생했을 때 리스너를 통해서 메세지를 전달해주는 형태
        - 객체에 리스너를 등록해두고 거기에 대해서 이벤트를 전달해줌

- 코드 예제

    - eventListener 인터페이스 생성(IButtonListener.java)
    ```java
    public interface IButtonListener {
        // event를 받을 수 있는 메서드
        void clickEvent(String event);
    }
    ```

    - 버튼 클래스 생성(Button.java)
    ```java
    public class Button {
        // 버튼 이름
        private String name;
        // 리스너
        private IButtonListener buttonListener;

        // default 생성자에서 리스너 할당 받음
        /*
        public Button(IButtonListener iButtonListener) {
            this.buttonListener = iButtonListener;
        }
        */
        // Swing과 비슷하게 만들면
        public Button(String name) {
            this.name = name;
        }

        // button에 대한 click
        public void click(String message){
            // message를 리스너를 통해서 전달
            buttonListener.clickEvent(message);
        }

        // Swing에 있는 Button 클래스와 유사한 방식 - addListener
        public void addListener(IButtonListener buttonListener) {
            this.buttonListener = buttonListener;
        }
    }
    ```

    - main.java
    ```java
    public class Main {

        public static void main(String[] args) {
            Button button = new Button("버튼");
        
            // 익명 클래스로 이벤트 전달 받아서 넣기
            button.addListener(new IButtonListener() {
                @Override
                public void clickEvent(String event) {
                    System.out.println(event);
                }
            });

            // 여기서 click이 발생하면 내부에서 listener를 통해서 전달
            button.click("메시지 전달 : click1");
            button.click("메시지 전달 : click2");
            button.click("메시지 전달 : click3");
            button.click("메시지 전달 : click4");
        }
    }
    ``` 