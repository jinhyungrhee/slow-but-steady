# 그래픽

## 안드로이드에서의 그래픽

- XML 파일로 그래픽이나 애니메이션을 정의함
- 그리는 작업은 안드로이드 시스템이 담당
- `onDraw()` 메서드 안에 `drawXXX()`와 같은 메서드를 호출하여 직접 그림
- 안드로이드 UI/UX는 View를 기반으로 함(View 상속받아서 커스텀 뷰를 정의할 수 있음)
- View 클래스 안에서 어떤 그림을 그릴 때 onDraw()메서드에서 Canvas 객체를 받아서 거기에 원하는 그림을 그림

## Canvas 클래스와 Paint 클래스

- Canvas 클래스는 그림을 그리는 캔버스(화포)에 해당
- Paint 클래스는 색상이나 선의 스타일, 채우기 스타일, 폰트, 안티앨리어싱 여부 등과 같은 그리기 속성을 가지고 있는 클래스임

## 색상

- 색의 3원색인 Red, Green, Blue 성분을 8비트로 표시
  - paint.setColor(0xFF0000);
  - paint.setColor(Color.RED);

## 폰트

- 메서드
  - 주어진 폰트와 스타일에 가장 일치하는 Typeface 객체를 생성함.
  - 주로 이미 존재하는 폰트로부터 새로운 스타일의 폰트를 생성하고자 할 때 호출함.
  - 만약 family가 null이면, 디폴트 폰트 패밀리를 선택함.
  ```
  static Typeface create(Typeface family, int style)
  static Typeface create(String familyName, int style)
  Typeface setTypeface(Typeface typeface) // 폰트를 typeface로 변경

  ex)
  Typeface t;
  t = typeface.create(Typeface.DEFAULT, Typeface.NORMAL);
  paint.setTypeface(t);
  canvas.drawText("DEFAULT 폰트", 10, 400, paint);
  ...
  ```
  - Typeface 객체 : Typeface 클래스 내부의 create()메서드로 생성됨
  - family(폰트이름) : DEFAULT, DEFAULT_BOLD, MONOSPACE, SANS_SERIF, SERIF 등
  - style(폰트스타일) : NORMAL, BOLD, ITALIC, BOLD_ITALIC 등
    
- 외부폰트 사용

  - 폰트 파일(.ttf)을 구하여 프로젝트의 asset 폴더로 복사
  - createFromAsset() 메서드 사용
    ```java
    myFont = Typeface.createFromAsset(getContext().getAssets(), "animeace2_ital.tff");
    paint.setTypeface(myFont);
    ```

## 패스(Path)

- 패스는 복잡한 기하학적인 경로를 표현 가능
- 패스는 직선과 타원, 곡선으로 이루어짐

## 이미지 표시

- ImageView 위젯 객체를 통해 이미지를 그릴 수 있음
- 리소스 폴더에 이미지 파일을 복사함
  - ex) android.png 파일을 프로젝트의 res/drawable 폴더에 복사함
  - ex) 프로그램에서는 R.drawable.android로 참조
- 지원되는 파일 형식은 PNG(선호), JPG(가능), GIF(권장되지 않음)
- 일반적으로 bitmap형태의 데이터 객체로 만들어서 사용
  - 크기를 늘리거나 자르는 등의 조작을 할 수 있음!
  - bitmap은 24bit 혹은  32bit의 픽셀 단위의 정보를 가지고 있는 것! (그 정보들을 가지고 사진을 만듦)
  ```java
  // 리소스를 argument로 넣어서 bitmap 객체 생성
  Bitmap b = BitmapFactory.decodeResource(getResources(), R.drawable.cat);  
  Bitmap mb = Bitmap.createBitmap(b, 0, 0, b.getWidth(), b.getHeight(), m ,false);
  Bitmap sb = Bitmap.createScaledBitmap(b, 200, 200, false);

  canvas.drawBitmap(b, 0, 0 , null);
  canvas.drawBitmap(mb, 0, 0 , null);
  canvas.drawBitmap(sb, 100, 100 , null);
  ```

## 도형 객체

- 사각형이나 원 같은 도형을 객체로 표시함
- Drawable 객체
  - xml로 객체 생성
    - \<Shape> 태그 사용
    - 코드에서 setImageDrawable()메서드로 그려줌
      ```java
      ImageView i = new ImageView(this);
      i.setImageDrawable(R.drawable.oval);
      ```

  - 코드로 객체 생성
    - canvas.drawCircle()
    - canvas.drawArc()
    - canvas.drawRect()

## Transition API 애니메이션

- 종류
  - Fade
    - 페이드-인 및 페이드-아웃과 같은 가장 보편적인 애니메이션 수행
  - Slide
    - 한 방향으로 움직여서 사라짐
  - Explode
    - 폭발하는 것과 같은 효과를 냄
  - Auto Transition 
    - Fade-out, ChangeBounds, Fade-in이 순차적으로 포함된 TranstionSet
    - 첫 번째 뷰가 페이드 아웃된 후에 위치 및 크기가 변경되고 마지막으로 새로운 뷰가 페이드 인으로 나타남
  - ChangeBounds
    - 위치 및 크기를 변경하는 애니메이션
  - TransitionSet
    - 여거 개의 전환들을 묶음

- 특정 버튼(fadeButton)을 누르면 **TransitionManager**를 통해서 Transition을 하나 정의한 뒤 해당 뷰 객체에다가 Transition을 적용시킴
  - `TransitionManager.beginDelayedTransition(layout, new Fade());`

## 드로어블 애니메이션

- 영화 필름처럼 여러 개의 이미지가 순서대로 재생되어 생성되는 전통적인 애니메이션 방식
  - 여러 개의 이미지를 하나의 애니메이션으로 정의 후 시간 단위(10ms)로 이미지를 교차시켜줌
- 애니메이션을 구성하는 프레임들을 나열하는 XML 파일(rocket.xml)을 생성
   - \<animation-list> 안에 \<item>태그로 이미지와 duration(ms) 설정
- 코드에서 `AnimationDrawable` 객체 생성하여 사용
  ```java
  AnimationDrawable rocketAnimation;

  public void onCreate(Bundle savedInstanceState) {
    //...
    ImageView rocketImage = (ImageView) findViewById(R.id.rocket_image);
    // 애니메이션 리소스를 이미지 뷰의 배경으로 설정
    rocketImage.setBackgroundResource(R.drawable.rocket);
    // 애니메이션 객체를 얻음
    rocketAnimation = (AnimationDrawable) rocketImage.getBackground();
  }

  public boolean onTouchEvent(MotionEvent event) {
    if (event.getAction() == MotionEvent.ACTION_DOWN) {
      // 화면이 터치되면 애니메이션을 시작함
      rocketAnimation.start();
      return true;
    }
    return super.onTouchEvent(event);
  }
  ```

## 서피스 뷰

- 개념
  - 서피스뷰는 사용자 인터페이스와는 별도로 애플리케이션에게 그림을 그릴 수 있는 화면을 제공

- 등장 배경
  - 앱이 시작되면 기본적으로 UI를 보여주는 액티비티가 하나 시작됨(이것이 가장 많은 리소스 차지)
  - 처음 UI를 그리는 액티비티(메인 스레드)가 전체를 다 그리도록 하면, 그림이 많고 복잡할 수록 소요시간이 길어짐
  - 메인스레드는 그림만 그리다가 user interaction이나 networking을 못할 가능성이 높아짐 (application 응답률 저하, ANR(Application Not Responding)에러 띄우고 종료)
  - 그러므로 별도의 스레드를 둬서 거기에서 그림을 다 그린 뒤, 그림이 그려진 캔버스만 메인스레드에서 보여주도록 함!

- 구성
  - 메인 스레드 : UI를 보여주는 스레드(오직 메인스레드에서만 UI를 보여줘야 함)
  - 별도의 스레드 : 서피스 뷰를 통해 메인 스레드와 별도로 그림을 그릴 수 있는 인터페이스 제공

- 서피스 뷰 구현 방식
    1. 서피스 뷰를 상속받고
    2. SurfaceHolder.Callback을 implements하는 객체를 하나 define(정의)함
    3. defined된 객체를 Activity에서 뷰를 생성해서 Root나 하부에 넣어주는 방식
    4. 생성된 서피스 뷰 안에서는 각종 그래픽을 그리는 작업들을 별도의 스레드를 만들어서 실행

- 구조
  - SurfaceView 클래스를 상속한 뷰를 생성함
    - SurfaceView를 생성하면 SurfaceHolder를 하나 반환받게 됨
    - SurfaceHolder에 3개의 메서드가 인터페이스로 정의되어 있음
      - 서피스가 생성되면 surfaceCreated()가 호출됨
      - 서피스가 변환되면 변환된 추가 작업을 하도록 surfaceChanged() 메서드가 호출됨
      - 서피스가 없어지면, 없어진 리소스를 처리하기 위한 surfaceDestroyed() 메서드가 호출됨
    ```java
    class MyView extends SurfaceView implements SurfaceHolder.Callback {
      public void surfaceCreated(SurfaceHolder holder) {
              // 서피스가 준비되었으므로 스레드를 시작함
      }
      public void surfaceDestroyed(SurfaceHolder holder) {
              // 서피스가 준비되었으므로 스레드를 종료함
      }
      public void surfaceChanged(SurfaceHolder holder, int format,
                                        int width, int height) {
              // 서피스가 변경됨
      }
    }
    ```
  - 스레드를 정의함
    - 스레드를 상속받아서 클래스를 define함
    - 스레드를 시작시키면 run()메서드가 돌아가면서, 기존 스레드와는 별도의 유저레벨의 스레드를 하나 만들어서 실행시킴(메인스레드와 별도)
    - 아까 생성한 서피스의 서피스홀더(holder)를 전달받아서, 전달받은 holder의 캔버스를 받아와서 캔버스에 그림을 그림
    ```java
    class MyThread extends Thread {
      SurfaceHolder holder;
      ...
      public void run()
      {
        canvas = holder.lockCanvas();
        // 캔버스에 그림을 그림
        ...
        holder.unlockCanvasAndPost(canvas);
      }
    }
    ```
  
