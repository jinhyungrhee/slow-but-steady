# 사용자 인터페이스 기초

## GUI 컴포넌트
- Java GUI 라이브러리
    - Swing
    - JavaFX
    - AWT
    - 라이브러리가 기본적으로 리소스를 많이 사용하기 때문에 안드로이드에는 맞지 않음

- 안드로이드는 독자적인 사용자 인터페이스 컨트롤 사용
    - 안드로이드 라이브러리가 별도의 인터페이스 제공
    - UI 컴포넌트
        - 버튼, 리스트, 스크롤바, 체크박스, 메뉴, 대화상자

## 뷰와 뷰그룹

- UI 컴포넌트들은 하나 하나가 뷰(View)라는 객체 밑에서 생성됨
- 뷰들은 화면에 display되기 위해서 뷰그룹(ViewGroup)안에 포함되어야 함
    - 뷰그룹 안에 여러 뷰들을 배치하는 형식!

- **뷰그룹(ViewGroup)**
    - 다른 뷰들을 담는 컨테이너 기능 수행
    - ViewGroup 클래스에서 상속받아서 작성됨
    - 흔히 `레이아웃`이라고 불림
    - 선형 레이아웃, 테이블 레이아웃, 상대적 레이아웃 등
    - 각 레이아웃은 정해진 정책에 따라서 뷰들을 배치함

- **뷰(View)**
    - `컨트롤` 또는 `위젯`이라고 불림
    - 사용자 인터페이스를 구성하는 기초적인 빌딩 블록
    - 버튼, 텍스트 필드, 체크박스 등
    - View 클래스를 상속받아서 작성됨

## UI 작성하는 절차

1. 뷰그룹을 생성함
2. 필요한 뷰를 추가
    - 안드로이드 프레임워크 안에 있는 윈도우 시스템과 뷰매니저가 해당 XML을 파싱해서 그 안에 들어있는 뷰그룹에 해당하는 객체를 생성하고 뷰에 대한 객체를 생성함
3. 액티비티 화면으로 설정함
    - 생성된 객체들은 윈도우 시스템에 의해서 뷰에 대한 hierarchy를 생성하게 되고, 그 hierarchy가 해당 activity에 root view로 설정이 되어서 화면에 그려짐
    - 해당 activity와 연계되어 있는 뷰그룹과 뷰들에 대한 객체를 해당 activity에서 접근할 수 있음
        - view에 설정되어 있는 Id를 통해 view를 가지고 와서 적용 가능

## XML로 UI를 작성하면 좋은점

- XML을 작성해놓으면 뷰 매니저와 윈도우 시스템에 의해서 XML에 있는 UI 컴포넌트가 객체로 그대로 만들어짐
    - 코드를 아무런 변경을 하지 않더라도 화면에 보여지는 그대로 객체가 만들어짐

## 뷰

- View 클래스는 모든 뷰/위젯들(TextView, ImageView, EditText, SurfaceView, Button, Scroll등)의 부모 클래스임
- View 클래스가 가지고 있는 필드나 메서드는 모든 뷰에서 공통적으로 사용 가능
- 뷰의 필드와 메서드
    - id : 뷰의 식별자
    - 뷰의 위치와 크기
        - match_parent : 부모의 크기를 꽉 채운다(fill_parent도 같은 의미)
        - wrap_content : 뷰가 나타내는 내용물의 크기에 맞춘다
        - 숫자 : 크기를 정확히 지정

- 뷰의 크기 단위

    - px(pixels)
        - 화면의 실제 픽셀을 나타냄
        - 장치마다 화면의 밀도가 다르기 때문에 권장되지 않음

    - dp(density-independent pixels)
        - 화면의 밀도가 160dpi 화면에서 하나의 물리적인 픽셀을 의미
        - 크기를 160dpi로 지정하면 화면의 밀도와는 상관없이 항상 1인치가 됨
        - dp로 뷰의 크기를 지정하면 화면의 밀도가 다르더라도 항상 동일한 크기로 표시됨

    - sp(scale-independent pixels)
        - 화면 밀도와 사용자가 지정한 폰트 크기에 영향을 받아서 변환됨
        - 폰트 크기를 지정하는 경우에 추천

    - pt(points)
        - 1/72 인치를 표시

    - mm(milimeters)
        - 밀리미터를 나타냄

    - in(inches)
        - 인치를 나타냄

- 색상
    - 16진수로 투명도와 빛의 3원색인 RGB값 표시
    - #RRGGBB
    - #AARRGGBB
        - AA는 투명도

- 화면에 보이기 속성

    - visible(0) : 화면에 보이게 함. 디폴트값.
    - invisible(1) : 표시되지 않음. 하지만 배치에서 공간은 차지.
    - gone(2) : 완전히 숨겨짐.

- 마진&패딩
    - 패딩 : 뷰의 경계와 뷰의 내용물 사이의 간격 (테두리 내부 간격)
        - paddingLeft, paddingRight, paddingTop, paddingBottom
    - 마진 : 자식 뷰 주위의 여백 (테두리 외부 간격)
        - layout_marginLet, layout_marginRight, layout_marginTop, layout_marginBottom

### 텍스트뷰

- 수정 불가능한 텍스트뷰

### 에디트 텍스트

- 수정 가능한 텍스트뷰
- 속성
    |속성|설명|
    |--|--|
    |android:autoText|자동으로 타이핑 오류를 교정|
    |android:drawableBottom|텍스트의 아래에 표시되는 이미지 리소스|
    |android:drawableRight|텍스트의 오른쪽에 표시되는 이미지 리소스|
    |android:editable|편집가능|
    |android:text|표시되는 텍스트|
    |android:singleLine|true면 한 줄만 받음|
    |android:inputType|입력의 종류|
    |android:hint|입력 필드에 표시되는 힌트 메시지|

- inputType 속성
    |inputType|설명|
    |--|--|
    |none|편집이 불가능한 문자열|
    |Text|일반적인 문자열|
    |textMultiLine|여러 줄로 입력 가능|
    |textPostalAddress|우편번호|
    |textEmailAddress|이메일 주소|
    |textPassword|패스워드|
    |textVisiblePassword|패스워드 화면에 보이기|
    |number|숫자|
    |numberSigned|부호가 붙은 숫자|
    |numberDecimal|소수점이 있는 숫자|
    |phone|전화번호|
    |datetime|시간|

### 이미지뷰

- 아이콘과 같은 이미지들을 간단히 표시하는데 사용
- 속성
    |속성|설정 메서드|설명|
    |--|--|--|
    |adroid:adjustViewBounds|setAdjustViewBounds(boolean)|drawable의 종횡비를 유지하기 위하여 이미지뷰의 가로,세로를 조정|
    |android:cropToPadding||true면 패딩 안에 맞춰서 이미지를 자름|
    |android:maxHeight|setMaxHeight(int)|이미지 뷰의 최대 높이|
    |android:maxWidth|setMaxWidth(int)|이미지 뷰의 최대 너비|
    |android:scaleType|setScaleType(ImageView.ScaleType)|이미지 뷰의 크기에 맞추어 어떻게 확대나 축소할 것인지 방법 선택|
    |android:src|setImageResource(int)|이미지 소스|
    |android:int|setColorFilter(int, PorterDuff.Mode)|이미지 배경 색상|
- 안드로이드에서 이미지 사용
    - 이미지를 drawable 폴더로 복사해서 사용

## 레이아웃

- 뷰그룹
- 뷰들을 화면에 배치하는 방법
- 레이아웃 클래스는 뷰들의 위치와 크기를 결정
- 종류
    - LinearLayout
    - TableLayout
    - GridLayout
    - RelativeLayout
    - TableLayout

### 선형 레이아웃(LinearLayout)

- 종류
    1. 수평 배치
    2. 수직 배치

- 속성
    |속성|메서드|설명|
    |--|--|--|
    |orientation|setOrientation(int)|'horizontal'은 수평, 'vertical'은 수직으로 배치|
    |gravity|setGravity(int)|x축과 y축 상에 자식을 어떻게 배치할 것인가 결정|
    |baselineAligned|setBaselineAligned(boolean)|false로 설정하면 자식뷰들의 기준선을 정렬하지 않음|

- gravity 속성 값
    |상수|값|설명|
    |--|--|--|
    |top|0x30|객체를 컨테이너 상단에 배치, 크기 변경X|
    |bottom|0x50|객체를 컨테이너 하단에 배치, 크기 변경X|
    |left|0x03|객체를 컨테이너 좌측에 배치, 크기 변경X|
    |right|0x05|객체를 컨테이너 우측에 배치, 크기 변경X|
    |center_vertical|0x10|객체를 컨테이너 수직의 중앙에 배치, 크기 변경X|
    |fill_vertical|0x70|객체를 컨테이너의 수직을 채우도록 배치|
    |center_horizontal|0x01|객체를 컨테이너 수평의 중앙에 배치, 크기 변경X|
    |fill_horizontal|0x07|객체를 컨테이너의 수평을 채우도록 배치|
    |center|0x11|객체를 컨테이너의 수평, 수직의 중앙에 배치|
    |fill|0x77|객체가 컨테이너를 가득 채우도록 배치|

- 가중치(weight)
    - 선형 레이아웃 자식뷰들간에 상대적인 비율 설정 가능
    - 따로 설정하지 않으면 default로 0이 됨!
    - 자식뷰들의 가중치가 각각 1, 2, 3이면, 
        - 남아있는 공간의 1/6, 2/6, 3/6을 각각 할당받음!
    - 자식뷰들의 가중치가 각각 0, 1, 1이면,
        - w=1 인 2개의 텍스트뷰들은 남아있는 공간을 동일하게 차지
        - w=0은 최소한의 크기만 차지하고 나머지 부분을 w=1인 두개의 텍스트 뷰들이 동일하게 나눠서 차지함

### 테이블 레이아웃(TableLayout)

- 수직으로 Linear Layout을 하나 만들고 수평으로 Linear Layout을 하나 더 만드는 것과 동일함!

### 상대적 레이아웃(RelativeLayout)

- 상대적으로 뷰들의 위치와 크기를 결정함
- \<TableLayout> 하위에 \<TableRow>가 여러 개 들어있고
- 각 \<TableRow> 안에 여러 개의 뷰(\<TextView>, \<EditText>)가 들어있는 형태
- 같은 column에 들어가 있는 뷰 중에서 가장 큰 뷰를 기준으로 뷰의 크기가 결정됨

- 속성
    |속성|설명|
    |--|--|
    |layout_above|true면 현재 뷰의 하단을 기준 뷰의 위에 일치시킴|
    |layout_below|현재 뷰의 상단을 기준 뷰의 하단에 위치시킴|
    |layout_centerHorizontal|수평으로 현재 뷰의 중심을 부모와 일치시킴|
    |layout_centerInParent|부모의 중심점에 현재 뷰를 위치시킴|
    |layout_centerVertical|수직으로 현재 뷰의 중심을 부모와 일치시킴|
    |layout_toLeftOf|현재 뷰의 우측단을 기준 뷰의 좌측단에 위치시킴|
    |layout_toRightOf|현재 뷰의 좌측단을 기준 뷰의 우측단에 위치시킴|

## XML 레이아웃과 Java 코드

1. 모든 XML 레이아웃은 자바 코드로 대체될 수 있음
    - UI 경우, 객체를 생성한 뒤 생성된 객체를 화면에 보여주기 위해서 반드시 Root View에 추가시켜 줘야함!
    - XML으로 레이아웃 작성한 경우(activity_main.xml)
        - onCreate()의 `setContentView(R.layout.activity_main);` 메서드를 통해 윈도우 시스템에 자기의 Root ViewGroup을 넘겨주는 것임!
            ```java
            public class MainActivity extends AppCompatActivity {

                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);
                    setContentView(R.layout.activity_main); // Root ViewGroup 넘겨주는 것
                }
            }
            ```
    - Java 코드에서도 **setContentView()**를 통해서 마지막에 최종적으로 Root ViewGroup을 윈도우 시스템에 넘겨줘야 함!
        ```java
        public class MainActivity extends AppCompatActivity {

                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);
                    LinearLayout container = new LinearLayout(this); // ViewGroup 객체 생성
                    container.setOrientation(LinearLayout.VERTICAL);

                    Button b1 = new Button(this); // View 객체 생성
                    b1.setText("첫번째 버튼");
                    container.addView(b1);

                    Button b2 = new Button(this); // View 객체 생성
                    b2.setText("두번째 버튼");
                    container.addView(b2);

                    setContentView(container); // Root ViewGroup 넘겨주는 것
                }
            }
        ```

2. XML로 define한 객체 View들을 java코드로 직접 불러올 수 있음
    - XML에서 정의한 `id`와 java코드에서 `findViewById()`메서드를 통해 가져올 수 있음!
    - 모든 id는 `R.id`라는 참조형 변수로 변환이 됨!
    - 예시
        - activity_main.xml
            - 처음에 레이아웃이 그려질 때 button1의 text는 button1으로 그려짐
            ```xml
            <?xml version="1.0" encoding="utf-8"?>
            <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
                xmlns:app="http://schemas.android.com/apk/res-auto"
                xmlns:tools="http://schemas.android.com/tools"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:orientation="horizontal"
                android:gravity="center_vertical"
                android:paddingLeft="10dp"
                android:paddingRight="10dp"
                tools:context=".MainActivity">

                <Button
                    android:id="@+id/button1"
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="5"
                    android:text="button1"/>

                <Button
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="10"
                    android:text="btn2"/>

                <Button
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="20"
                    android:text="button3"/>


            </LinearLayout>
            ```

        - MainActivity.java
            - 이후에 java 코드가 실행되면서 button1의 text는 "MyButton"으로 변경됨(덮어쓰기)
            ```java
            public class MainActivity extends AppCompatActivity {

                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);
                    setContentView(R.layout.activity_main);

                    Button button = (Button) findViewById(R.id.button1);

                    button.setText("MyButton");
                }
            }
            ```