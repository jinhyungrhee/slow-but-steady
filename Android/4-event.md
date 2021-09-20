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

## 이벤트 처리 메서드 재정의

- 이벤트 처리와 관련된 여러 가지 메서스들이 미리 정의되어 있고 그것들을 자기 뷰에 적용하기 위해서 재정의(오버라이딩)해서 사용
- 재정의할 수 있는 콜백 메서드
    - onKeyDown(int, KeyEvent)
    - onKeyUP(int, KeyEvent)
    - onTrackballEvent(MotionEvent)
    - onTouchEvent(MotionEvent)
        - 해당 뷰에 터치가 발생했을 경우, 터치 이벤트가 만들어져서 콜백으로 전달됨
        - 재정의를 해놓았다면 해당 메서드가 실행되어서 원하는 작업을 수행함
    - onFocusChanged(boolean, int, Rect)
- invalidate()
    - 해당 뷰/컴포넌트에 대해 invalidate를 시켜주면 콜백으로 미리 정의해놓은 그리기 함수(onDraw(Canvas canvas){...})등을 호출할 수 있음
- 예시
    ```java
    public class MainActivity extends AppCompatActivity {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            // 객체를 직접 만들어서 Root View에다가 넣어주는 코드
            MyView myView = new MyView(this);
            setContentView(myView);
        }
    }
    // 클래스 정의(객체는 실제 코드에서 따로 생성 필요)
    class MyView extends View {

        int key;
        String str;
        int x,y;

        // 기본 view는 기본 생성자 하나만 있어도 됨
        public MyView(Context context) {
            super(context);
            setBackgroundColor(Color.YELLOW);
        }

        // 우클릭 - generate - override methods
        @Override
        public boolean onTouchEvent(MotionEvent event) {
            x = (int)event.getX();
            y = (int)event.getY();
            invalidate(); // onDraw() 메서드가 콜백으로 불림
            return super.onTouchEvent(event);
        }

        // 우클릭 - generate - override methods
        @Override
        protected void onDraw(Canvas canvas) {
            // 그림 그리는 graphics 작업 수행
            super.onDraw(canvas);
            Paint paint = new Paint();
            paint.setTextSize(50);
            // canvas(뷰 바탕화면)에 여러 가지 도형 넣어줄 수 있음
            canvas.drawCircle(x,y,30,paint);
            canvas.drawText("(" + x + "," + y + ") Touch Occurred", x, y, paint);
        }
    }
    ``` 
    - **일반적으로 하나의 java파일 안에는 public class는 하나만 존재할 수 있음!**

## 볼륨 컨트롤러 예제

- 특정 위젯 뷰를 상속받은 커스텀 뷰를 만듦
    - 이미지 뷰에서 touch 이벤트가 발생했을 경우에 onTouch()가 호출되고
    - onTouch()가 호출된 위치에 따라서 이미지를 회전시킴
    - volume을 돌렸을 경우에 얼마나 늘어났고 줄어들었는지를 ratingBar를 이용하여 표시함
        - 이를 듣기 위한 listener : `KnobListener` (인터페이스로 정의 필요!)

1. eventtest 패키지 아래 새로운 VolumeControlView 클래스 생성
    ```java
    // view에 touch 이벤트를 넣을 수 있도록 OnTouchListener 인터페이스를 implement함
    // ImageView 에러 - ImageView는 widget 아래 있는 것이고 기본적으로 모든 activity들은 AppCompatActivity를 상속받음
    // ImageView도 AppCompatActivity를 확장해서 상속받아야함 (두가지 방법 중 아무거나)
    @SuppressLint("AppCompatCustomView")
    public class VolumeControlView extends ImageView implements View.OnTouchListener {

        private double angle = 0.0;
        private KnobListener listener;
        float x,y;
        float mx, my;

        // KnobListener 인터페이스 정의
        public interface KnobListener {
            // abstract 메서드도 정의
            public void onChanged(double angle);
        }

        // listener를 등록할 변수
        public void setKnobListener(KnobListener lis){
            listener = lis;
        }

        // ImageView의 경우에는 context만 있는 생성자와 attribute를 받는 생성자 두 개를 만들어야 함
        public VolumeControlView(Context context) {
            super(context);
            this.setImageResource(R.drawable.knob);
            this.setOnTouchListener(this);
        }

        public VolumeControlView(Context context, @Nullable AttributeSet attrs) {
            super(context, attrs);
            this.setImageResource(R.drawable.knob);
            this.setOnTouchListener(this);
        }
        private double getAngle(float x, float y) {
            mx = x - (getWidth() / 2.0f);
            my = (getHeight() / 2.0f) - y;

            double degree = Math.atan2(mx, my) * 100.0 / Math.PI;
            return degree;
        }

        // OnTouchListener 인터페이스 안에 있는 abstract 메서드 구현 필요
        @Override
        public boolean onTouch(View view, MotionEvent motionEvent) {
            x = motionEvent.getX();
            y = motionEvent.getY();
            angle = getAngle(x, y);
            invalidate();
            listener.onChanged(angle);
            return false;
        }

        @Override
        protected void onDraw(Canvas canvas) {
            canvas.rotate((float) angle, getWidth()/2, getHeight()/2);
            super.onDraw(canvas);
        }
    }
    ```

2. XML 레이아웃 정의
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        tools:context=".MainActivity">

        <!--커스텀 컴포넌트 생성-->
        <com.example.eventtest.VolumeControlView
            android:id="@+id/volume"
            android:layout_width="300px"
            android:layout_height="300px" />

        <RatingBar
            android:id="@+id/rating"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:stepSize="1.0" />


    </LinearLayout>
    ```

3. MainActivity.java에서 VolumeControlView와 ratingBar 연결
    ```java
    public class MainActivity extends AppCompatActivity {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            // xml에 정의된 레이아웃 그려줌
            setContentView(R.layout.activity_main);
            
            // MainActivity에서 rating bar를 달아서 넣어줘야함
            RatingBar bar = (RatingBar) findViewById(R.id.rating);
            VolumeControlView view = (VolumeControlView) findViewById(R.id.volume);
            view.setKnobListener(new VolumeControlView.KnobListener() {
                @Override
                public void onChanged(double angle) {
                    // 전달받은 angle에 따라서 rating bar에 값을 넣어줌
                    float rating = bar.getRating();
                    if (angle > 0 && rating < 7.0) {
                        bar.setRating(rating + 1.0f); // rating bar 하나 증가
                    } else if (rating > 0.0) {
                        bar.setRating(rating - 1.0f);
                    }
                }
            });
        }
    }
    ```

## 터치 이벤트

- 일반적으로 커스텀 뷰를 정의하고 onTouchEvent()를 재정의해서 사용
- 터치 이벤트의 종류
    |액션|설명|
    |--|--|
    |ACTION_DOWN|누르는 동작이 시작됨|
    |ACTION_UP|누르고 있따가 뗄때 발생함|
    |ACTION_MOVE|누르는 도중에 움직임|
    |ACTION_CANCEL|터치 동작이 취소됨|
    |ACTION_OUTSIDE|터치가 현재의 위젯을 벗어남|

- 예제
    - MainActivity.java
        ```java
        public class MainActivity extends AppCompatActivity {

            @Override
            protected void onCreate(Bundle savedInstanceState) {
                super.onCreate(savedInstanceState);
                // myView 넣어주기
                MyView myView = new MyView(this);
                setContentView(myView);
            }
        }
        // 클래스 정의(객체는 실제 코드에서 따로 생성 필요)
        class MyView extends View {

            int key;
            String str;
            float x,y;
            
            // 그림판 그리기 예제
            private Paint paint = new Paint();
            private Path path = new Path();

            // 기본 view는 기본 생성자 하나만 있어도 됨
            public MyView(Context context) {
                super(context);
                setBackgroundColor(Color.YELLOW);
                // 페인트 속성 지정
                paint.setAntiAlias(true);
                paint.setStrokeWidth(10f);
                paint.setColor(Color.BLUE);
                paint.setStyle(Paint.Style.STROKE);
                paint.setStrokeJoin(Paint.Join.ROUND);
            }

            // 우클릭 - generate - override methods
            @Override
            public boolean onTouchEvent(MotionEvent event) {
                x = event.getX();
                y = event.getY();
                // 터치 이벤트의 타입을 확인하고 처리가능
                // 터치가 발생할 때마다 case를 만들어줌
                if(event.getAction() == MotionEvent.ACTION_DOWN) {
                    // DOWN이 발생하면 path를 시작함
                    path.moveTo(x,y);
                }
                if(event.getAction() == MotionEvent.ACTION_MOVE) {
                    // MOVE가 발생하면 라인을 이어줌
                    path.lineTo(x,y);
                }
                if(event.getAction() == MotionEvent.ACTION_UP) {

                }
                // 터치 이벤트를 모두 입력받고 나중에 그에 해당하는 값을 그려줌(콜백)
                // onDraw() 메서드가 콜백으로 불림
                invalidate();

                // onTouchEvent에서 자기가 그렸던 것을 온전히 적용하기 위해서는 true를 리턴해야 함!
                return true;
            }

            // 우클릭 - generate - override methods
            @Override
            protected void onDraw(Canvas canvas) {
                // 그림 그리는 graphics 작업 수행
                super.onDraw(canvas);
                canvas.drawPath(path, paint);
            }
        }
        ```

## 멀티 터치
- 여러 개의 손가락을 이용하여 화면을 터치하는 것
- 이미지를 확대/축소할 때 많이 사용됨
- 터치 이벤트
    - 터치가 발생할 때마다 현재 몇 번째 터치인지, 몇 개의 터치가 들어오는지 index 값을 통해 알아낼 수 있음
    - `ACTION_DOWN`
        - 화면을 터치하는 첫 번째 포인터에 대하여 발생함
        - 제스처 인식이 시작됨
        - 첫 번째 터치는 항상 MotionEvent에서 인덱스 0번에 저장됨
    - `ACTION_POINTER_DOWN`
        - 첫 번째 포인터 이외의 포인터에 대하여 발생됨 (두 번째, 세 번째...)
        - 포인터 데이터는 getActionIndex()이 반환하는 인덱스에 저장됨
    - `ACTION_MOVE`
        - 화면을 누르면서 이동할 때 발생
    - `ACTION_POINTER_UP`
        - 마지막 포인터가 아닌 다른 포인터가 화면에서 없어지면 발생됨
    - `ACTION_UP`
        - 화면을 떠나는 마지막 포인터에 대해서 발생됨

- 예제
    - MultiTouchView 클래스 생성