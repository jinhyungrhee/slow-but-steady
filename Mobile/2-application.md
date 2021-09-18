# 어플리케이션 기본구조

## 일반적인 어플리케이션 작성 절차

1. 사용자 인터페이스 작성(XML)
    - XML을 이용하여 사용자 인터페이스 화면을 디자인
2. 자바 코드 작성(JAVA)
    - 자바를 이용하여 코드 작성
3. 매니페스트 파일 작성(XML)
    - 어플리케이션을 구성하고 있는 컴포넌트를 기술하고 실행 시 필요한 권한을 지정

## 패키지 폴더

- java
    - 자바 소스 파일들이 들어있는 폴더
    - 폴더 안의 kr.co.company.hello는 패키지의 이름임

- Gradle Scripts
    - 그레이들(Gradle)은 빌드 시 필요한 스크립트임

- res
    - 각종 리소스(자원)들이 저장되는 폴더
    1. drawable
        - 해상도 별로 아이콘 파일들이 저장됨
    2. layout
        - 화면의 구성을 정의함
    3. values
        - 문자열과 같은 리소스 저장
    4. menu
        - 메뉴 리소스들이 저장되어 있음

- manifest
    - XML 파일로 앱의 전반적인 정보(앱의 이름이나 컴포넌트 구성 등)를 가지고 있음

## 패키지

- 클래스들을 보관하는 컨테이너
- 일반적으로 인터넷 도메인 이름을 역순으로 사용
    - ex) kr.co.company.hello;

## @Override

- 어노테이션 중 하나
    - 어노테이션 : 컴파일러에게 추가적인 정보를 주는 것
- 해당 메서드가 부모 클래스의 메서드를 재정의(오버라이드)했다는 것을 나타냄

## onCreate() 메서드

- 액티비티가 생성되는 순간에 딱 한번 호출되는 메서드
- 모든 초기화와 사용자 인터페이스 설정이 여기에 들어감!
- `super.onCreate(savedInstanceState);`
    - 부모 클래스인 ActionBarActivity 클래스의 onCreate()를 호출하는 코드
- `setContentView(R.layout.activity_main);`
    - setContentView() : 액티비티의 화면을 설정하는 함수
    - R.layout.activity_main : activity_main.xml 파일을 의미

## TIP

- 필요한 패키지 쉽게 추가하기
    - File - Settings - Editor - General - Auto Import
        - `Add unambigious imports on the fly` 옵션 체크
        - `Optimize imports on the fly` 옵션 체크

## 어플리케이션 시작 지점

- 안드로이드에는 main()이 없다!
- 액티비티 별로 실행됨
- 액티비티 중에서는 **onCreate()** 메서드가 **가장 먼저 실행**됨!!

## 사용자 인터페이스 작성 방법

1. 자바 코드를 사용하는 방법
2. XML을 사용하는 방법 (**안드로이드 선호 방법**)
    - 안드로이드에서는 UI 화면 구성을 XML을 이용하여 **선언적**으로 나타내는 방법 선호
        - 어플리케이션 외관(XML)과 어플리케이션 로직(java코드)를 서로 분리
        - 빠르게 UI 구축 가능

    - java 코드를 이용한 UI(사용자 인터페이스)
        ```java
        TextView tv = new TextView(this);
        tv.setText("HEllo, World!");
        ```

    - XML을 이용한 UI(사용자 인터페이스)
        - activity_main.xml
            ```xml
            <?xml version="1.0" encoding="utf-8"?>
            <TextView xmlns:android="https://schemas.android.com/apk/res/android"
                android:id="@+id/textview"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="Hello, world!"/>
            ```
        - UI 컴포넌트들은 XML의하나의 요소로 표현됨
        - TextView 컴포넌트는 \<TextView .../> 요소로 표현됨

## \<TextView> 속성

