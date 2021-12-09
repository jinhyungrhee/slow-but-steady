# 멀티미디어

## Android Multimedia Framework (각 layer에서 multimedia 기능 지원)

|Layer|종류|기능|detail|
|--|--|--|--|
|Application|Multimedia Player(Client)|skin,재생,반복/배속조절,찾기/볼륨조절|Home, Contact, Phone, Browser ...|
|Application Framework|Multimedia JNI interface|App과 Core간 커뮤니케이션|ActivityManager, WindowManager, ContentProvider, ViewSystem, PackageManager, TelephonyManager, ResourceManager, LocationManager, NotificationManager|
|Libraries|Multimedia(Server, Engine, Codec)|비디오코덱, 오디오코덱, 다운로드, 로컬플레이|SurfaceManager, MediaFramework, SQLite, OpenGL/ES, FreeType, Webkit, SGL, SSL, libc, Core Lib(Android Runtime), Dalvik VM(Android Runtime)|
|Linux Kernel|Audio/Video HAL&Codec Driver|Audio/Video hardware abstraction layer|Display Driver, Camera Driver, Flash Memory Driver, Binder(IPC) Driver, Keypad Driver, WiFi Driver, Audio Driver, Power Managerment|


- multimedia 데이터는 raw데이터를 그대로 사용하기 때문에 사용되는 데이터 용량이 방대해 압축과 해제(인코딩/디코딩)가 반드시 필요함 => `Codec Engine`
- Codec Engine은 C/C++ 형태로 Library로 구현되어 있음
- Codec Engine에서 제공하는 서비스를 받아서 Applicaion Framework에서 사용함(multimedia 재생 등)
  - Codec Engine과 Application Framework 간에는 `JNI Interface`로 연결되어 있음!
- Linux Kernel 레벨에서 device driver를 사용하여 외부 장치를 이용해 미디어 정보를 입력받거나 출력함

## Application Framework에서 제공하는 객체

- MediaPlayer
  - 멀티미디어 데이터들을 출력(재생)하는 객체
- MediaRecorder 
  - 멀티미디어 데이터를 입력(녹음/녹화)받는 객체
- SurfaceView / videoView
  - 카메라로 들어온 데이터 소스나 video file을 display하기 위한 창(view)

- Audio
  - play (=>MediaPlayer)
  - record (=>MediaRecorder, MIC 사용)
- Video
  - play (=>MediaPlayer)
  - record (=>MediaRecorder, Camera 사용)
- Image
  - capture (=>Camera 사용)
  - display


## Mediaserver(Codec Engine)에서의 처리과정

- StagefrightPlayer에서 오디오 데이터는 AudioSink라는 client 객체로 보냄
- StagefrightPlayer에서 비디오 데이터는 Surface라는 client 객체로 보냄
- Library 레벨에서 오디오를 관리하는 모듈 : AudioFlinger
  - 코덱 엔진을 통해 Audio Device Driver(=ALSA)에게 데이터 만들어서 전송
- Library 레벨에서 비디오를 관리하는 모듈 : SurfaceFlinger
  - 코덱 엔진을 통해 Linux의 FrameBuffer Driver에게 데이터 만들어서 전송

## MediaPlayer State Diagram

- 시작시키는 과정 
  - → reset() → `Idle` → setDaataSource → `Initialized` → prepare() → `Prepared` → start() → `Started`
- 중지
  - 완전히 멈추기(stopped) : 재생 불가
    - → ... → `Started` → stop() → `Stopped`
    - Stopped에서 다시 play하려면 prepare() 통해서 다시 start()해야함! (바로 재생 불가!)
      - → ... → `Stopped` → prepare() → `Prepared` → start() → `Started` 
    - 초기상태로 돌아가기 위해선 release()와 reset()을 통해서 장치 해제 필요 
      - → ... → `Stopped` → release() → `End` → reset() → `Idle` 
  - 일시 정지(paused) : 재생 가능
    - → ... → `Started` → pause() → `Paused` → start() → `Started` 

## Multimedia의 encoding/decoding 작업

- raw데이터가 들어오면 데이터를 압축해서 특정 데이터의 형식에 맞게 변형시키는 것 : `Encoding`
- encoding으로 특정 format의 file이 생성되면 Library를 통해 device driver로 데이가 나가도록 하는 것 : `Decoding` 

## 안드로이드 지원 파일 형식

- 오디오
  - MP3 : .mp3 
  - AMR-NB(3GPP) : .3gp
- 이미지
  - JPEG
  - GIF
  - PNG
  - BMP
- 비디오
  - MPEG-4 SP

## 오디오 재생 및 녹음

- 오디오 재생
  - MediaPlayer 클래스 사용
- 오디오 녹음
  - MediaRecorder 클래스 사용

## MediaPlayer 클래스

- 안드로이드 액티비티에서 setDataSource()와 prepare(), start()를 호출하여 MediaPlayer 객체 사용

## 이미지 캡쳐
- 2가지 방법
  - 인텐트 사용(안드로이드 이미지 캡쳐 앱)
  - Camera 클래스 사용

## 비디오 재생
- MediaPlayer 클래스는 오디오 재생 뿐만 아니라 비디오 재생도 담당
- VideoView 클래스는 MediaPlayer 객체의 생성과 초기화를 담당

## 비디오 녹화 및 재생

- MediaRecorder 클래스 : 비디오 녹화 담당
- MediaPlyer 클래스 : 녹화된 비디오 재생 담당
- Surface View : 캠코더의 화면을 표시


## MediaPlayer 클래스

|메서드|설명|
|--|--|
|setVideoSource()|녹화에 사용되는 비디오 소스(=카메라) 선택. 즉 Camera나 Default중에서 선택. 만약 이 메서드가 호출되지 않으면 출력 파일은 비디오 트랙을 포함하지 않음|
|setOutputFormat()|녹화 때 생성되는 출력 파일의 형식(mp4등)을 설정(지정하지 않으면 default). setAudioSource()/setVideoSource() 메서드 이후에 호출해야 함. 그러나 prepare() 메서드 전에 반드시 호출되어야 함|
|setVideoEncode()|녹화 때 사용되는 비디오 인코더를 설정(지정하지 않으면 default). 만약 이 메서드가 호출되지 않으면 출력 파일은 비디오 트랙을 포함하지 않음. 이 메서드는 setOutputFormat() 후에 그러나 prepare() 전에 호출되어야 함|
|setOutputFile()|이 메서드는 출력 파일의 경로를 설정함. 이 메서드는 setOutputFormat() 후에, 그러나 prepare() 전에 호출되어야 함|
|setPreviewDisplay()|녹화되는 비디오의 프리뷰를 보이기 위한 서피스를 설정. 이 메서드는 원하는 프리뷰 디스플레이를 설정하기 위하여 prepare() 전에 호출되어야 함|
|prepare()|비디오를 캡쳐하고 인코딩하기 위하여 레코더를 준비함. 이 메서드는 원하는 오디오나 비디오 소스나 인코더, 파일 형식 등을 설정한 후에 호출되어야 함. 그러나 start() 전에는 반드시 호출되어야 함|
|start()|비디오를 캡쳐하고 인코딩하여서 파일에 저장함. setOutputFile()로 지정된 파일에 저장함. prepare() 후에 이 메서드를 호출함.|

## 코드 작성 시 주의할점

- cameraPreview나 surfaceView에 대한 설정을 잘 해주지 않으면 (mediaPlayer나 mediaRecorder의 객체들의 상태 천이를 통해 이루어지기 때문에, 상태 천이나 surfaceView/cameraPreview 의 상태를 적절히 설정해주지 않으면) 녹화나 재생이 잘 이루어지지 않음 
- 상태 천이에 따른 view의 관계를 잘 설정해줘야 함!