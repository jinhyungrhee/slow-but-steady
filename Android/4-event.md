# 이벤트 처리

- UI에 터치와 같은 이벤트가 발생했을 때 처리하는 기법

## 입력 위젯(뷰)

- `사용자` <-- `입력위젯` -->  `앱`

- 버튼, 텍스트 필드, 시크 바, 체크 박스, 줌 버튼, 토글 버튼

- 종류

    |위젯|설명|관련 클래스|
    |--|--|--|
    |Button|어떤 동작을 수행하기 위해 사용자가 누를 수 있고 클릭할 수 있는 푸시 버튼|Button|
    |Text field|편집이 가능한 텍스트 필드, 자동 완성 기능을 제공하려면 AutoCompleteTextView를 사용|EditText, AutoCompleteTextView|
    

## 버튼

- 텍스트 버튼
    - \<Button> 뷰 사용
    - `android:text="@string/button_text"`

- 이미지 버튼   
    - \<ImageButton> 뷰 사용
    - `android:src="@drawable/button_icon"`

- 텍스트와 이미지를 동시에 갖는 버튼
    - \<Button> 뷰 사용
        ```java
        android:text="@string/button_text"
        android:drawableLeft="@drawable/button_icon"`
        ```
    - 객체지향의 특징!
        - 부모클래스를 상속받아서 다양화/다변화시킬 수 있음

- 버튼의 이벤트 처리

    - **onClick** 속성 사용
        - XML에 해당 버튼에 클릭 이벤트가 발생했을 경우 실제 코드의 함수를 바로 호출할 수 있도록 함수의 이름을 기재할 수 있는 속성
            - `android:onClick="sendMessage"`
            - sendMessage() 함수는 반드시 MainActivity에 java 코드로 구현되어 있어야 함!
        - onClick 함수의 argument로 view가 넘어옴 
            - onClick 이벤트가 발생한 뷰 객체 자체가 넘어옴(Button은 view의 자식클래스)
            - view라는 객체에 참조가 되어서 넘어옴(polymorphism)
                - polymorphism : 부모 클래스에 참조한 변수는 자식 클래스의 객체를 참조할 수 있음

## 폴링과 이벤트 구동 방식

- 이벤트 구동(Event-Driven) 방식
    - UI에 event를 처리할 수 있는 Listener를 만들어서 지속적으로 들을 수 있도록 해당 객체에 붙여놓음 : 폴링(polling)
    - event가 발생하면 그 event를 처리하는 handler(listener)를 통해서 처리함

## 안드로이드에서 이벤트 처리 방법

- XML 파일에 이벤트 처리 메서드를 등록하는 방법
    - onClick 속성 사용
        - 속성 값에 handler함수명 입력
    - 가장 쉽고 권장되는 방법

- 이벤트 처리 객체를 생성하여 컴포넌트에 등록
    - 일반적인 방법
    ```java
    Class MyClass{
        class Listener implements OnClickListener { // 인터페이스를 구현한 클래스 정의
            public void onClick(View v){ // 사용자가 클릭하면 호출됨
                ...
            }
        }
        ...
        Listener lis = new Listener(); // 이벤트 리스너 객체 생성
        button.setOnClickListener(lis); // 버튼에 이벤트 리스너 객체 등록
        ...
    }
    ```
- 뷰 클래스의 이벤트 처리 메서드를 재정의
    - 커스텀 뷰를 작성하는 경우 (ex 게임)

## 리스너 객체 생성하는 방법

- 리스너 클래스를 내부 클래스로 정의하는 방법
- **리스너 클래스를 무명 클래스로 정의하는 방법** (가장 많이 사용)
    ```java
    ...
    public class MainActivity extends AppCompatActivity {
        @Override
        public void onCreate(Bundle saveInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            Button button = (Button) findViewById(R.id.button);
            // button에 등록하는 함수의 argument로 
            // (정의되지 않은 이름의) anonymous 객체를 생성해서 넣어줌
            button.setOnClickListener(new OnClickListener(){  
                public void onClick(View v) {
                    Toast.makeText(getApplicationContext()),
            "버튼이 눌러졌습니다", Toast.LENGTH_SHORT).show();        
                }
            });
        }
    }
    ```
- 리스너 인터페이스를 액티비티 클래스에 구현하는 방법

## 리스너의 종료

- 각 view마다 다양한 종류의 listener가 존재

|리스너|콜백 메서드|설명|
|--|--|--|
|View.OnClickListener|onClick()|사용자가 어떤 항목을 터치하거나 내비게이션 키나 트랙볼로 항목으로 이동한 후에 엔터키를 눌러서 선택하면 호출됨|
|View.OnLongClickListener|onLongClick()|사용자가 항목을 터치하여서 일정 시간 동안 그대로 누르고 있으면 발생함|
|View.OnFocusChangeListener|onFocusChange()|사용자가 하나의 항목에서 다른 항목으로 포커스를 이동할 때 호출됨|
|View.OnKeyListener|onKey()|포커스를 가지고 있는 항목 위에서 키를 눌렀다가 놓았을 때 호출됨|
|View.OnTouchListener|onTouch()|사용자가 터치 이벤트로 간주되는 동작을 한 경우에 호출됨|

## 텍스트 필드

- 텍스트 필드(text field)를 사용하면 사용자가 앱에 텍스트를 타이핑하여 입력할 수 있음

- 단일 라인, 멀티 라인 모두 입력 가능

- 키보드 종류 지정 가능
    - `android:inputType="textEmailAddress"` : 영어 자판

- EditText와 TextField의 차이
    - EditText
        - 일반적으로 한 라인 정도를 받을 때 사용
    - TextField
        - 일반적으로 큰 영역을 지정할 때 사용


## 에디트 텍스트(Edit Text)의 이벤트 처리

- 버튼을 누르면 Edit Text에 있는 값을 읽어오는 것 가능
    ```java
    public class MainActivity extends AppCompatActivity {
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            final EditText eText;
            Button btn;
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            eText = (EditText) findViewById(R.id.edittext);
            btn = (Button) findViewById(R.id.button);
            btn.setOnClickListener(new View.OnClickListener() {
                public void onClick(View v) {                   // 버튼을 누르면
                    String str = eText.getText().toString();    // Edit Text에 있는 값을 읽어옴
                    Toast.makeText(getBaseContext().str.Toast.LENGTH_LONG).show();
                }
            });
        }
    }
    ```
- view에 있는 text 값을 읽어오는 함수 : `getText()`
- view에 text를 설정하는 함수 : `setText()`


## 체크박스

- 독립적으로 동작하는 하나의 박스
    - 독립적인 항목에 대한 체크 또는 해제
- 체크를 했는지 하지 않았는지 확인하는 위젯(GUI 컴포넌트)
- 버튼과 유사
    - onClick 이벤트 발생
- 버튼과 차이점
    - isChecked() 메서드를 통해 현재 체크박스가 체크되어있는지 판별 가능 (boolean타입 리턴)
        ```java
        public void onCheckboxClicked(View view) {
            boolean checked = (CheckBox) view).isChecked(); // true, false 리턴
        }

        switch(view.getId()) {
            case R.id.checkbox_meat:
                if (checked)
                    Toast.makeText(getApplicationContext(), "고기 선택",
                            Toast.LENGTH_SHORT).show();
                else
                    Toast.makeText(getApplicationContext(), "고기 선택 해제",
                            Toast.LENGTH_SHORT).show();
                break;
            case R.id.checkbox_cheese:
                if (checked)
                    Toast.makeText(getApplicationContext(), "치즈 선택",
                            Toast.LENGTH_SHORT).show();
                else
                    Toast.makeText(getApplicationContext(), "치즈 선택 해제",
                            Toast.LENGTH_SHORT).show();
                break;
        }
        ```

## 라디오 버튼

- 여러 개의 항목을 묶어서 그 중 하나만을 선택할 수 있도록 하는 위젯(GUI 컴포넌트)
- onClick 이벤트 발생
- 구조
    ```java
    <LinearLayout ...>
        <RadioGroup
        android:layout_width=""
        android:layout_height=""
        android:orientation="vertical"
        >
            <RadioButton
                android:id="@+id/radio_red"
                android:layout_width=""
                android:layout_height=""
                android:onClick="onRadioButtonClicked"
                android:text="Red" />
            <RadioButton
                android:id="@+id/radio_blue"
                android:layout_width=""
                android:layout_height=""
                android:onClick="onRadioButtonClicked"
                android:text="Blue" />
        </RadioGroup>
    </LinearLayout>
    ```
- 라디오 버튼의 이벤트 처리
    - isChecked() 메서드 사용하여 어떤 것이 눌러졌는지 판별
    ```java
    public void onRadioButtonClicked(View view) {
        boolean checked = ((RadioButton) view).isChecked();

        switch(view.getId()) {
            case R.id.radio_red:
                if (checked)
                    Toast.makeText(getApplicationContext(),
                    ((RadioButton) view).getText(),
                    Toast.LENGTH_SHORT).show();
                break;
            case R.id_radio_blue:
                if (checked)
                    Toast.makeText(getApplicationContext(),
                    ((RadioButton) view).getText(),
                    Toast.LENGTH_SHORT).show();
                break;
        }
    }
    ```

## 토클 버튼

- 버튼 하나를 눌렀을 때 눌러진 상태 유지 혹은 복구
- isChecked() 메서드 사용
- default로 ON/OFF 들어감

## 레이팅바

- XML로 라디오 버튼을 정의함
    ```java
    <RatingBar
        android:id="@+id/ratingBar"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@+id/buttonOK"
        android:numStars="5"
        />
    ```
- `setOnRatingBarChangeListener()` 리스너 함수 사용
    - ratingBar에 변화가 생길 때 마다 몇 개가 눌렸는지 확인 가능
    ```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        bar = (RatingBar) findViewById(R.id.ratingBar);
        // ratingbar 리스너 등록
        bar.setOnRatingBarChangeListener(new RatingBar.OnRatingBarChangeListener() {
            @Override
            public void onRatingChanged(RatingBar ratingBar, float v, boolean b) {
                // ratingbar가 변화할 때마다 해당 객체를 argument로 받고 몇개가 눌렸는지 에 대한 정보 받을 수 있음!
                Toast.makeText(getApplicationContext(),
                        "rating: " + v, Toast.LENGTH_LONG).show();
            }
        });
    }
    ```
    - Toast : 아주 짧은 시간동안 팝업창으로 띄움
        - 값들을 쉽게 확인할 수 있도록 함

## 커스텀 컴포넌트

- 개발자가 직접 View 클래스를 상속받아서 필요한 위젯을 개발 가능