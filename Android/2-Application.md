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
    - R.java라는 파일로 변환돼서 각 리소스의 ID가 부여되는 상태로 만들어짐
    1. drawable
        - 해상도 별로 아이콘 파일들이 저장됨
        - 일반적으로 **이미지 파일**을 이곳에 가져다 놓음
    2. layout
        - 화면의 구성을 정의함
        - UI를 구성하는 XML파일이 위치함
        - 뷰 그룹에 해당하는 파일들
    3. values
        - 문자열과 같은 리소스 저장
        - 이 앱에서 사용할 각종 정보들(color, string)을 자기 나름대로 define
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

- xmlns:android
    - XML 이름공간의 선언
    - 안드로이드 도구에 안드로이드 이름공간에 정의된 속성들을 참조하려고 한다는 것을 암시
    - XML 파일에서 항상 최외각 태그는 이 속성을 정의해야 함!

- android:id
    - TextView 요소에 유일한 아이디를 할당
    - 이 아이디를 이용하여 소스 코드에서 이 텍스트 뷰를 참조할 수 있음

- androidLlayout_width
    - 화면에서 얼마나 폭을 차지할 것인지 정의
    - `match_parent`는 전체 화면의 폭을 다 차지하는 것 의미

- android:layout_height
    - 화면에서 길이를 얼마나 차지할 것인지 정의
    - `wrap_content`는 콘텐츠를 표시할 정도만 차지하는 것 의미

- android:text
    - 화면에 표시하는 텍스트 설정
    - 하드코딩으로 사용할 수도 있고 문자열 리소스의 개념을 사용할 수도 있음


## XML

- 요소(element)
    - 시작 태그로 시작되어 종료 태그로 끝나는 논리적인 구성 요소
    - ex) \<Greeting>Hello, world!\<Greeting>

- 속성(attribute)
    - 요소의 속성
    - 이름-값의 쌍으로 구성
        - ex) \<img src="dog.jpg" alt="by anon"/>

## 리소스

- 안드로이드에서 취급하는 레이아웃, 이미지, 문자열 등을 의미 
- 코드와 리소스 분리
    - 안드로이드가 탑재된 장치들이 다양해지면서 언어나 화면 크기에 따라 리소스를 다르게 할 필요성 有
- 문자열도 XML로 기술하는 것이 바람직

## 정리

- 어플리케이션은 컴포넌트들의 조합으로 만들어짐

- 코드와 리소스는 철저하게 분리시켜야 함

- 코드와 리소슨느 개발 도구에 의하여 자동으로 생성되는 `R.java`에 의해 서로 연결됨