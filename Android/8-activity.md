# 액티비티 & 인텐트

- 프레임워크에 있는 내부 구조들을 사용해서 안드로이드 프로그래밍을 할 수 있음

## 4가지 중요한 개념

1. 어플리케이션
2. **액티비티**
  - 하나의 job을 실행하는 가장 기본이 되는 단위
  - 내부에서의 다른 job들과의 연동이 가능함
3. 액티비티 스택
4. 태스크

- 안드로이드 스튜디오로 개발하면 최종적으로 `.apk`파일이 생성됨
- 이 `.apk` 파일이 패키지 형태로 만들어져서 폰에 설치가 되고 실행이 되는 것
  - 즉, 이것을 하나의 어플리케이션으로 볼 수 있는데
  - 하나의 어플리케이션은 여러 개의 화면이 서로 연동하면서 사용자에게 서비스를 제공함
  - 이때 기본적으로 한 화면을 구성하는 단위가 바로 **액티비티**!
    - 여러 개의 화면을 구성하려면 여러 개의 액티비티를 구성해야 함
    - 하나의 앱 안에서 여러 개의 액티비티들 간의 소통도 가능하고
    - 서로 다른 앱 간의 액티비티들의 소통도 가능함
    - 즉, 액티비티 하나가 별도의 독립적인 모듈이 된다!

## 어플리케이션

- 한 개 이상의 액티비티들로 구성됨
- 액티비티들은 애플리케이션 안에서 느슨하게 묶여 있다.

## 액티비티

- 애플리케이션을 구성하는 빌딩 블록

## 태스크

- 스택에 있는 액티비티들
- 안드로이드의 기본 커널 = 리눅스
  - 운영체제에서 애플리케이션은 하나의 독립적인 프로세스로 만들어져서 실행됨
  - 앱을 실행(런칭)시키면 리눅스 시스템 위에 프로세스가 하나 생성되고, 그 안에서 액티비티(안드로이드 객체)가 실행되는 것
  - 하나의 앱을 런칭하면 프로세스 특정 공간(= `스택` / `태스크`) 안에 하나의 액티비티가 실행됨
  - 또 다른 앱을 런칭하면 그에 해당하는 액티비티가 스택 공간 위에 쌓이게 됨
  - 이러한 스택에 쌓여있는 여러 액티비티들의 집합을 `태스크`라고 함!
  - 하나의 앱에서 여러 개의 스택(=또 다른 태스크)을 쌓을 수 있도록 구성할 수도 있음

## 액티비티 스택

- `Back 키`를 누르면 현재 액티비티를 제거(close)하고 이전 액티비티로 되돌아 감
  - 태스크 스택에 액티비티들을 쌓아서 프로그램을 실행시킴
- 사용자가 방문한 액티비티들은 어딘가에 저장(기억)됨
- 이러한 상태도 가능함
  - 액티비티 1에서 액티비티 2를 부르고(1위에 2가 쌓임), 액티비티 2가 다시 액티비티 1을 부르면 새로운 액티비티 1 객체를 생성하여 다시 2위에 1을 쌓는 것(스택 : 1 - 2 - 1)
  - 액티비티의 라이프 사이클을 잘 이해하고 프로그래밍 해야 함!


## 인텐트

- 하나의 액티비티에서 다른 액티비티로 call하는 방법
- 안드로이드 프레임워크에서 **액티비티들 간의 매개체가 되는 객체**

- 각각의 화면은 별도의 액티비티로 구현됨
  - 하나의 액티비티(화면)에서 다른 액티비티(화면)로 전환하려면 인텐트를 사용해야 함!

- 다른 액티비티를 시작하려면 액티비티의 실행에 필요한 여러 가지 정보들을 보내줘야 함
  - 그 때 필요한 정보들을 `인텐트` 객체에 실어서 보냄!
  - 안드로이드 프레임워크(-> 어플리케이션 밑에 존재)에 `ActivityManager`가 존재
    - 모든 Activty들에 대한 관리 담당
    - 일반적으로 ActivityManager는 PackageManager와 연동하여 Activity를 띄움
      - `PackageManager`
        - 생성된 .apk 파일(클래스와 리소스들을 압축하여 만든 파일)은 이는 package name(패키지를 구분하는 아주 중요한 naming)으로 구분됨
        - 스마트폰에 앱을 설치하면(.apk를 폰에 설치하면) 안드로이드의 PackageManager가 apk파일의 package name을 분석해서 이를 압축해제하고 package manager가 관리하는 각종 앱에 대한 정보들과 함께 앱을 설치하는 과정을 진행함
        - 즉, package manager는 핸드폰에 설치되어 있는 각종 앱의 package 정보들을 관리하는 역할을 수행!
          - 어떤 activity, service로 구성되어 있는지, 어떤 broadcast receiver, content provider로 구성되어 있는지 기재된 파일 => `manifest`
          - manifest를 parsing해서 정보 관리
  - 어플리케이션에서 인텐트를 만들어서 ActivityManager에게 전달함
  - ActivityManager는 인텐트에 (명시적/암묵적으로) 기재되어 있는 Activity를 확인하고 call함
    - 명시적 : Activity 이름을 기재함 (일반적으로 자신의 패키지(app)내에 있는 Activity를 call할 때 사용)
    - 암묵적 : 

## 인텐트의 종류

- 명시적 인텐트(explicit intent)
  - "애플리케이션 A의 컴포넌트 B를 구동시켜라"처럼 명확하게 지정
  - 인텐트 객체를 하나 생성하여 사용
    - 수 많은 종류의 인텐트 생성자가 오버라이드 되어 있음!
    ```java
    Intent intent = new Intent(this, NextActivity.class); // 현재 액티비티, 콜할 액티비티
    startActivity(intent); // 만들어진 intent를 startActivity()메서드를 통해 Activity Manager에게 전달 => 액티비티 실행
    ```

- 암시적 인텐트(implicit intent)
  - 암묵적으로 실행시킬 내용을 기술
    - 그것을 실행시키도록 지정되어 있는 액티비티를 실행시키도록 하는 것
  - "지도를 보여줄 수 있는 컴포넌트면 어떤 것이라도 OK"
  - 기본 기능
    - 구글 지도 보여주기
    - 전화 연결
    - 연락처 보기
    - 갤러리 보기
    - 웹브라우저 접속
  - 애플리케이션에서 직접 구현할 필요 없이 이러한 앱들과 연동시켜주기만 하면 됨
    - 내 액티비티에서 이런 기능을 하는 액티비티를 실행시켜서 자기의 태스크 스택에 쌓으면 됨

## manifest 파일에 정의된 Activtiy

- Android.Manifest.xml
  ```xml
  <activity
      android:name=".MainActivity" // 이름
      android:exported="true"> // 외부 노출 여부
      <intent-filter> // 언제 자기가 실행된 intent를 받을지 지정
          <action android:name="android.intent.action.MAIN" /> // MainActivity가 런칭이 될 때 실행되는 Activity

          <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
  </activity>
  ```

- 기본적으로 하나의 Activity는 하나의 layout을 별도로 구성하도록 권장됨!

- 액티비티를 한꺼번(클래스 + 레이아웃)에 추가하는 방법 
  1. package name 오른쪽 클릭
  2. new - activity - empty activity
    - '레이아웃 추가' 체크!
  - 결과 : manifest 파일
    ```xml
    <activity
        android:name=".SecondActivity"
        android:exported="true" />
    <activity
        android:name=".MainActivity"
        android:exported="true">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />

            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>
    ```

## 여러 페이지로 된 어플리케이션 작성

- 액티비티 여러 개 추가하고 각 액티비티마다 화면을 다르게 구성
- 인텐트로 화면 전환 기능 구현

## 액티비티에서 결과 받기 (명시적 인텐트 사용)

- 액티비티들 간의 데이터 연동 
- 인텐트에다가 데이터(int, String, pointer등)를 **Bundle형태**로 만들어서 전달
  ```java
  public class MainActivity extends Activity {
    ...
    // 서브 액티비티 시작
    Intent in = new Intent(MainActivity.this, SubActivity.class);
    startActivityForResult(in, COMMAND);

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
      ... // 여기서 값을 전달받음
    }
  }
  ```

- 값을 저장하고, 값을 읽는 메서드
  - 전달하는 쪽 (SubActivity -> Intent)
    - 하나의 key, value쌍으로 만들어서 보냄
      - putExtra(String name, int value)
      - putExtra(String name, float value)
      - putExtra(String name, int[] value)
      - putExtra(String name, String value)

  - 받는 쪽 (Intent -> MainActivity)
    - 받는 Type을 미리 알아야 함
      - int getIntExtra(String name, int defaultValue)
      - float getFloatExtra(String name, float defaultValue)
      - int[] getArrayExtra(String name)
      - String getStringExtra(String name)

## 액티비티 결과 주고받는 앱

- 메인 액티비티에서 버튼을 누르면 서브 액티비티를 시작함
- 서브 액티비티에서 문자열을 입력하고 '입력완료'버튼을 누르면 서브 액티비티는 문자열을 메인 액티비티로 전달한 후 종료함
  - 문자열을 메인 액티비티로 반환할 때도 Intent에 값을 넣어서 전달함
  - 액티비티를 부른 쪽에서 데이터를 전달받고 싶으면, 전달받을 데이터가 있다고 명시하는 메서드 사용
    - `startActivityForResult()` : 이를 사용하면 자기가 보낸 Activity가 종료를 할 때 항상 result를 받게 되어 있음
    - `onActivityResult(int requestCode, int resultCode, Intent data)` : 이 메서드에서 result를 콜백으로 받음
      - subActivity는 Intent 객체에 데이터를 달아서 전달함
- 메인 액티비티에서는 이 문자열을 받아서 텍스트 뷰를 통하여 화면에 표시함

## 암시적인 인텐트

- 어떤 작업을 하기를 원하지만 그 작업을 담당하는 컴포넌트의 이름을 명확하게 모르는 경우에 사용
  - 암시적으로 인텐트에 원하는 작업을 작성한 뒤, 그 인텐트를 Activity Manager에게 전달
  - 그러면 Activity Manager는 일을 담당할 수 있는 Activity들의 리스트 중에서 지정된 Activity를 실행시켜 줌
- 기본적으로 정의된 것 (= 이러한 기능들을 기본적으로 제공하는 것은 '스마트폰'이라고 함!)
  - 전화걸기
  - 연락처 관리
  - 카메라
  - 웹브라우저 실행
- 형식
  ```java
  Intent intent = new Intent(Intent.ACTION_SEND); // 원하는 action이 들어감!
  intent.putExtra(Intent.EXTRA_EMAIL, recipientArray);
  startActivity(intent);
  ```
- 액션의 종류
  |상수|타겟 컴포넌트|액션|
  |--|--|--|
  |ACTION_VIEW|액티비티|데이터를 사용자에게 표시함|
  |ACTION_EDIT|액티비티|사용자가 편집할 수 있는 데이터를 표시함|
  |ACTION_MAIN|액티비티|태스크의 초기 액티비티로 설정함|
  |ACTION_CALL|액티비티|전화 통화를 시작함|
  |ACTION_SYNC|액티비티|모바일 장치의 데이터를 서버 상의 데이터와 일치시킴|
  |ACTION_DIAL|액티비티|전화 번호를 누르는 화면을 표시함|

  - 예시
    - 액션 데이터형식(URI형식 - Uniform Resource Identifier)
    - ACTION_VIEW content://contacts/people/1 : 1번 연락처 정보를 표시
    - ACTION_DIAL content://contacts/people/1 : 1번 연락처로 전화걸기 화면을 표시
    - ACTION_VIEW tel:0101234567 : 0101234567번 전화번호로 전화걸기 화면을 표시
    - ACTION_DIAL tel:0101234567 : 0101234567번 전화번호로 전화걸기 화면을 표시
    - ACTION_EDIT content://contacts/people/1 : 1번 연락처 정보를 편집
    - ACTION_VIEW content://contacts/people/ : 연락처 리스트를 표시

## 멀티태스킹

- 동시에 여러 태스크를 실행
- 현재의 태스크를 배경(background)로 보내고 다른 태스크를 전경(foreground)에서 시작할 수 있음
  - foreground : 현재 실행되는 액티비티
  - background : 뒤에서 돌고 있는, 화면에 나타나지 않는 상태

- 동작 원리
  - 일반적으로 하나의 앱이 실행되면 empty 태스크 스택이 하나 생성되고, 거기에 launching된 액티비티가 하나 쌓이게 됨
  - 다른 앱이 또 실행되면 또 다른 empty 태스크 스택을 하나 생성하고 거기에 launching한 액티비티를 하나 쌓음
  - 하나의 액티비티가 실행되었을 때 기본적으로 풀 스크린을 채우도록 하는데
  - 그 상황에서 다른 액티비티도 실행시키면 현재 foreground에서 돌고 있던 태스크가 background로 보내지고, 지금 실행된 액티비티가 foreground로 오게 됨!

- 멀티 태스킹의 예
  - 안드로이드 시스템에서는 여러 개의 액티비티가 태스크로 묶여서 foreground, background, sleep 등의 상태로 변경되며 운영됨
    - 홈버튼을 누르면 배경화면이 전경테스크에 오게됨
    - 그 상태에서 계산기를 누르면 계산기 액티비티가 전경태스크로 오고 배경화면은 배경태스크로 이동
    - 이 상태에서 다시 홈버튼을 누르면 배경이 전경태스크로 오고, 계산기 액티비티는 배경태스크로 감
    - 그리고 캘린더 앱을 누르면 캘린더 액티비티가 전경태스크로 오고, 배경화면과 계산기는 둘다 배경태스크로 이동함

- 오버뷰 화면
  - 최근에 사용된 액티비티들과 태스크들을 보여주는 화면

## 액티비티 생애주기

- 액티비티는 여러가지 유저의 interaction에 따라서 상태 천이를 하고, 이에 따라 불리는 callback 메서드를 지정함으로써 액티비티의 상태를 관리할 수 있음!

- 상태
  - 실행 상태(resumed, running) 
    - 액티비티가 전경에 위치하고 있으며 사용자의 포커스를 가지고 있음

  - 일시멈춤 상태(paused)
    - 다른 액티비티가 전경에 있으며 포커스를 가지고 있지만 현재 액티비티의 일부가 아직도 화면에서 보이고 있는 상태

  - 정지 상태(stopped)
    - 액티비티가 배경에 위치하는 상태

- 객체의 생성 단계 
  - onCreate() -> `Created` -> onStart() -> `Started(visible)` -> onResume() -> `Resumed(visible)`

- 일시 멈춤 상태
  - 어떤 액티비티가 다른 액티비티에 의해 background로 가는 전 단계 (중간 단계의 상태)
  - background로 가기 전에 popup창을 띄울 경우, 뒤에 부분적으로 액티비티가 보이는 상태
  - `Resumed(visible)` -> onPause() -> `Paused(partially visible)`
  - `Paused(partially visible)` -> onResume() -> `Resumed(visible)` : 다시 foreground로 돌아간 상황

- 정지되었다가 다시 실행하는 경우
  - `Paused(partially visible)` -> onStop() -> `Stopped(hidden)` : 완전히 background로 들어간 상황
    - 이 때는 바로 다시 Resumed 상태로 갈 수 없음!
  - `Stopped(hidden)` -> onRestart() -> onStart() -> `Started(visible)` -> onResume() -> `Resumed(visible)`

- 객체의 종료 단계
  - 코드에서 finish()를 호출하거나 메인 액티비티에서 Back키를 누르는 경우(= 앱 종료)
  - `Resumed(visible)` -> onPause() -> `Paused(partially visible)` -> onStop() -> `Stopped(hidden)` -> onDestroy() -> `Destroyed`


- **foreground로 가는 두 단계**
  - onCreate() -> `Created` -> onStart() -> `Started(visible)` -> onResume() -> `Resumed(visible)`

- **background로 가는 두 단계** 
  - `Resumed(visible)` -> onPause() -> `Paused(partially visible)` -> onStop() -> `Stopped(hidden)`

- 중요한 콜백 메서드 (본인이 원하는 곳에 override해서 넣을 수 있음)
  - onCreate()
    - 액티비티가 생성되면서 호출
    - 중요한 구성요소들을 초기화

  - onPause()
    - 사용자가 액티비티를 떠나고 있을 때, 이 메서드가 호출됨
    - 그 도안 이루어졌던 변경사항을 저장

- 생애주기가 중요한 이유
  - 앱에 대한 상태에 따라서 생애주기를 제대로 관리해주지 않으면 액티비티가  데이터를 유실하거나 상태가 망가지는 경우 발생할 수 있음!

## 인텐트 필터

- 인텐트 : 액티비티들 간의 매개체 
  - 액티비티들은 자기가 불렸을 때 자기가 받고자 하는 상태만 걸러서 받을 수 있음(filtering)
  - 자신이 원하는 액션(처리)에 대해서만 받도록 설정 가능!
- 컴포넌트는 자신들이 처리할 수 있는 인텐트의 종류를 인텐트 필터에 기록함
- manifest파일의 \<activity>안에 \<intent-filter> 추가
  - manifest : 해당 application이 어떤 구조와 정보를 가지고 있는지 기술해놓은 문서
  ```xml
  <activity ...>
    <intent-filter>
      <action android:name = "android.intent.action.MAIN" />
      <category android:name = "android.intent.category.LAUNCHER" />
    </intent-filter>
  </activity>
  ```

## 액티비티 상태 저장

- 애플리케이션이나 액티비티의 상세(detail)에 따라서 메모리의 상태가 천차만별로 달라짐
  - 데이터 변형, 왜곡 등이 발생 가능함
- 데이터의 상태를 임시로 저장하기 위한 callback 메서드 제공

- 예시
  - `Activity Running` 상태에서 background 상태로 갈 때(또는 천이할 때) 액티비티의 상태를 저장 : **onSaveInstanceState()**
    - Bundle 객체를 argument로 받음
    - Bundle 객체에다가 데이터를 넣어서 저장!
    - .putXXX() 메서드 사용하여 저장!
  - background 상태에서 다시 foreground 상태로 돌아올 때 액티비티의 상태를 복구 : **onRestoreInstanceState()**