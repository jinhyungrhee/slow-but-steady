# 센서

## 센서 하드웨어
- 자이로, 근접, 가속도, 주변광, 나침반 센서 내장

## 센서 관리자 클래스
- `SensorManager` 클래스는 장치에 내장되어 있는 센서의 리스트를 제공
  - sensor_manager = (SensorManager)getSystemService(SENSOR_SERVICE);

- Sensor getDefaultSensor(int type)
  - 주어진 타입에 대한 디폴트 센서를 얻을 수 있음

## 센서의 타입

|상수|설명|단위|
|--|--|--|
|TYPE_ALL|모든 센서||
|TYPE_ACCELEROMETER|가속도 센서|m/sec2|
|TYPE_GRAVITY|중력 센서|m/sec2|
|TYPE_GYROSCOPE|자이로스코프 센서||
|TYPE_ORIENTAITON|방향 센서|도(degree)|
|TYPE_LIGHT|조도 센서|lux|
|TYPE_LINEAR_ACCELERATION|선형 가속 센서||
|TYPE_MAGNETIC_FIELD|자기장 센서|마이크로테슬라(uT)|
|TYPE_PRESSURE|압력 센서||
|TYPE_PROXIMITY|근접 센서|미터|
|TYPE_ROTATION_VECTOR|회전 벡터 센서||
|TYPE_TEMPERATURE|온도 센서||

- example : 가속도 센서에 대한 정보 얻기
  ```java
  accelerometer = sensor_manager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
  ```

## 센서로부터 값을 받는 방법

- 값을 받고 싶은 센서에 리스터를 등록해 놓으면 애플리케이션에서 값을 전달받을 수 있음
  ```java
  SensorEventListener listener = new SensorEventListener() {
    // 센서 값에 변화가 있는 경우 호출
    public void onSensorChanged(SensorEvent event) { 
      // 여기서 센서 값을 읽음
    }

    // 센서 값의 정확도에 변화가 있는 경우 호출
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }
  }
  ```

- 센서 리스너 등록
  ```java
  mSensorManager.registerListener(this, mOrientation, SensorManager.SENSOR_DELAY_UI);
  ```

## AVD에서의 센서 값 입력
- Extended controls - virtual sensors
  - Z-Rot: z축 회전 (폰을 바라보고 있을 때, 시계방향/반시계방향으로 회전)
  - X-Rot: x축 회전('수평(가로)'을 기준으로 회전)
  - Y-Rot: y축 회전('수직(세로)'을 기준으로 회전)
- 이러한 회전에 따라 Accelerometer, Gyroscope, Magnetometer, Rotation값 변경

## 방향(orientation) 센서
- 현재 장치의 자세를 나타냄
- 3개의 값 제공
  - 방위각(azimuth) : z축
  - 피치(pitch) : x축
  - 롤(roll) : y축
- orientation은 값을 radian으로 표현
- SDK버전이 업데이트되면서 deprecated됨!
  - 직접 가져오기보다는 `ACCELEROMETER`와 `MAGNETIC_FIELD` 두 개를 결합시켜 방향에 대한 값을 가져와야 함!(=> 더 정밀한 값)
    - getRotationMatrix(R, I, mGravity, mGeomagnetic);
    - getOrientation(R, orientation);

## 가속도 센서

- 가속도 센서(accelerometer)는 장치의 **가속도**를 측정(얼마나 빠르게 움직이는지)
- 중력 센서(gravity sensor)라고도 함
- x축 방향의 가속도, y축 방향의 가속도, z축 방향의 가속도가 측정됨

## 주사위 예제

- STT(Speech To Text), TTS(Text To Speech)
  - implements TextToSpeech.OnInitListener
  - 오버라이딩 메서드
  ```java
  @Override
    public void onInit(int i) {
        if(i != TextToSpeech.ERROR) {
            mTts.setLanguage(getResources().getConfiguration().locale); // locale = 영어
        }
    }
  ```