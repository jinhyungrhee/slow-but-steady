# 스레드

## 다중 스레딩
- 하나의 어플리케이션이 동시에 여러 가지 작업을 하는 것
- 이들 작업은 스레드(thread)라고 함
- 프로세스
  - 하나의 프로그램이 실행되는 하나의 큰 논리적 구조체
- 스레드
  - 프로세스 내에서 cpu를 실행시킬수 있는 최소 단위
  - 여러 개의 프로세스가 있을 경우, 프로세스들 간의 상태변화 및 context switching하는데 오버헤드가 많이 발생함

## 안드로이드에서의 프로세스와 스레드
- 어플리케이션이 시작되면 안드로이드 시스템은 새로운 리눅스 프로세스를 생성함
  - 이 프로세스 안에서 각종 액티비티나 컴포넌트들이 실행됨
- 기본적으로 어플리케이션 안의 모든 컴포넌트들은 동일한 프로세스의 동일한 스레드로 실행됨
- 하나의 스레드가 유저의 이벤트를 받아서 이벤트에 대한 처리를 한 뒤, 자신이 display하고 있는 UI에 그 이벤트에 대한 결과를 보여줌
  - 이러한 하나의 안드로이드 어플리케이션에서 실행되는 스레드를 메인 스레드(main thread)라고 함

## 메인 스레드
- 메인 스레드는 사용자 인터페이스 위젯에게 이벤트를 전달하거나 화면을 그리는 작업을 담당
  - 사용자 인터페이스에 대한 이벤트를 전달 받아서 그에 대한 각 컴포넌트의 실행을 전달하고, 실행된 결과를 받아서 화면에 보여주는 작업
- **UI 스레드**(User Interface Thread)라고 불리기도 함
  - 외부에서 user interaction을 받거나 내부적으로 처리하는 데이터를 받아서, 앱의 외부 컴포넌트 또는 내부 컴포넌트들과의 interaction을 통해서 작업을 수행함
- 데이터(또는 메시지)를 전달하기 위한 일종의 QUEUE를 관리하는 객체 => `LOOPER`
  - 내부적으로 메시지 큐를 통해 컴포넌트에게 이벤트를 전달하거나 전달받음 

## 프로세스와 스레드
- 일반적으로 하나의 프로세스 안에 메인 스레드가 있고, 메인 스레드 안의 액티비티라는 컴포넌트를 통해서 실행되는 구조
- 경우에 따라서는 하나의 앱 안에서 여러 개의 독립적인 프로세스를 생성해서 다중으로 실행되도록 구성할 수도 있음
  - 하나의 프로세스 안에는 기본적으로 프로세스를 처리하는 스레드가 생성되어 있음
  - 스레드들은 스레드들간의 통신을 통해 데이터를 주고받음

## 안드로이드의 단일 스레드 모델 원칙
1. UI스레드는 user interaction에 대한 작업을 블록시키면 안 됨
  - blocking I/O 작업이나 CPU Bounded 작업, network 작업 등 user interaction이 끊길 수 있는 작업을 할 때, 몇 초 이내의 응답이 발생하지 않을 경우 ANR(Android Not Responding) 에러 메시지를 발생시키고 중단됨
  - 이러한 무거운 작업(blocking I/O 작업이나 CPU Bounded 작업, network 작업)을 할 때는 Main Thread에서 돌리면 안 됨!(별도의 다른 thread를 만들어 작업함)
  - Thread는 자원을 공유함
    - cpu의 레지스터 값, 각 스레드가 현재 실행하는 순간의 cpu 자원을 제외한 모든 자원들을 하나의 프로세스에서 공유함
    - 그 말은 Thread도 UI 처리 자원에도 접근이 가능하다는 의미!
    - work thread를 만들더라도 그것은 UI 처리하는 결과를 반영하면 안 됨!
2. UI스레드 외부에서 안드로이드 UI 툴킷을 조작하면 안 됨 

## 작업 스레드
- 별도로 생성되는 스레드
- 배경 스레드(background thread)라고도 함

## 작업 스레드를 작성하는 방법
- Thread 클래스를 상속받아서 스레드를 작성하는 방법
  - Class definition한 뒤 객체를 생성
  - 해당 스레드 객체 안에는 run() 메서드가 있음
  - run()메서드 안에서 작성한 코드가 Thread에서 실행되는 것
- Runnable 인터페이스를 구현한 뒤 Thread 객체에 전달하는 방법
  - anonymous thread를 실행하는 인터페이스 => Runnable 인터페이스
    - interface 안에는 abstract 메서드 존재
    - Runnable 인터페이스에는 run()이라는 abstract 메서드가 존재
    - Runnable 인터페이스를 new를 통해 객체를 생성하면 그 안에 run() 메서드를 강제로 구현해야 함

## 주의할 점
- 네트워크 관련 작업은 네트워크 상황에 따라 delay를 예측하기 어렵기 때문에, 별도의 작업 스레드를 만들어서 작업 수행
- 스레드에서 직접적으로 사용자 인터페이스 위젯을 변경하면 안 됨!
  - 스레드에서 작업한 결과를 메인 스레드에 넘겨줘야 함
  ```java
  public void onClick(View v) {
    new Thread(new Runnable() {
      public void run() {
        Bitmap b = loadImageFromNetwork("http://example.com/image.png");
        mImageView.setImageBitmap(b); // wrong!
      }
    }).start();
  }
  ```

## 해결 가능한 3가지 방법
1. Activity.runOnUiThread(Runnable)  
: UI스레드에서 Runnable(스레드) 객체를 넘겨 받아서 거기에서 해당 Runnable(스레드) 객체가 실행되도록 하는 것
2. View.post(Runnable)  
: 적용할 뷰에 직접 post로 Runnable 객체를 넣어줌.   
  post()를 호출하면 메인 스레드의 메시지 큐 안에 runnable 객체의 작업이 들어감.  
  그러한 작업들이 메인 스레드에서 하나씩 꺼내져서 LOOPER에서 실행됨.  
  (전달받은 UI 작업이 메인 스레드에서 실행되는 것)  
3. View.postDelayed(Runnable, long)  
: 특정 시간의 delay를 설정하여 Runnable 객체를 실행함

## Handler 클래스를 사용하는 방법
- Runnable 객체를 post() 메서드를 사용하여 UI 스레드로 보냄
- UI스레드에서 Handler객체를 생성해서 가지고 있으면, 작업스레드에서 Handler객체에 접근할 수 있음
  - Handler는 동일한 어플리케이션에서 공유되는 자원이기 때문!
- Handler객체에 post()를 해주면 Handler가 작업을 받아서 그 안에서 처리함

## Async 클래스 사용 방법
- AsyncTask 클래스는 1.5버전부터 추가된 클래스로, 작업 스레드와 관련된 복잡한 부분을 쉽게 처리해주는 클래스임
  - 대표적으로 네트워크를 통해 특정 데이터를 다운받는 작업
  - 네트워크로부터 다운로드 받는 작업을 일련화/세분화시켜서 처리하는 클래스
  - Async클래스는 일종의 abstract class

## Async 클래스
- AsyncTask<> 클래스를 상속받아서 특정 클래스를 정의하는 방식으로 사용
- 반드시 구현해야 하는 abstract 메서드
  - doInBackground()
  - onPostExecute()
- 과정
  - onPreExcute() : UI스레드 -> doInBackground() : 작업 스레드 -> publishProgress() : 작업 스레드 -> onProgressUpdate() : UI스레드 -> onPostExecute() : UI스레드 -> onCancelled() : UI스레드
    - onPreExcute() : 어떤 작업을 위한 준비단계
    - doInBackground() : 실제 작업을 background에서 실행하는 실행단계
    - publishProgress() + onProgressUpdate() : 작업 실행 중간 중간 UI를 업데이트시켜서 보여줌
    - onPostExecute() : 작업이 완료가 되면 해당 작업이 UI스레드에서 실행/업데이트 되도록 함
- 위와 같은 작업들을 배분해서 수행할 수 있는 메서드들을 실행할 수 있는 구조체를 제공 (작업을 일반화시킴)
- 제네릭 타입으로 세 개의 argument를 받음
  - 제네릭 타입 : 자기가 어떤 타입으로 정의하냐에 따라 해당 타입으로 지정됨!
  - `private class DownloadImageTask extends AsyncTask<String, Void, Bitmap>`
  - 세 개의 argument (type들은 제네릭하게 정의하여 직접 지정할 수 있음)
    - 첫 번째(ex String) : 객체로 만들어서 실행할 때 doInBackground()에 넘겨주는 parameter
    - 두 번째(ex Void) : publishProgress()에 넘겨주는 parameter
    - 세 번째(ex Bitmap) : 작업이 끝나고 post()해줄 때 전달되는 result값
- 실제 실행할 때는 메인 메서드(혹은 onClick()메서드)에서 해당 task객체를 생성해서 `.execute()`메서드를 사용해서 실행시킴
  - 그 안에는 전달할 parameter(세 개의 인자 중 첫 번째 인자)가 들어감!

## 정리

- 네트워크 작업, cpu작업, response가 느린 작업들을 work 스레드(별도의 작업 스레드)나 AsyncTask로 분리하고 그 결과를 UI스레드에 반영함