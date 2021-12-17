# 위치 기반 애플리케이션

- 사용자의 모바일에서의 위치를 인식하고, 위치를 바탕으로 서비스하는 앱
- 예시 : 구글맵 기반 서비스

## 위치 정보를 얻는 방법

- GPS(Global Positioning System)
  - 3개 이상의 위성정보를 이용해서 지구상의 위치(위도/경도)를 표현
  - 위성 정보를 수신할 수 있는 '실외'에서만 사용가능
- 전화 기지국을 이용
  - cellular 망 사용(대략적인 위치 파악)
  - 실내 위치 정보
- WiFi의 AP(Access Point)를 이용
  - 위치정보 기반으로 신호의 세기를 파악해서 (계산적으로) 근거리 위치 파악
  - 실내 위치 정보

## 사용자 위치 파악하기

- 위치 제공자(Location Provider)들을 지원하며 이들은 모두 `위치 관리자(Location Manager)` 시스템 서비스를 통하여 제공
  - `location manager` : location 정보 제공
  - 모바일 스마트폰은 기본적으로 GPS 수신 장치가 내장되어 있음
  - GPS 수신 장치로부터 프레임워크를 통해서 location 정보를 얻어올 수 있음(LocationManager 객체)
    ```java
    LocationManager manager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
    List<String> providers = manager.getAllProviders();
    ```

## 사용자 위치 구하기

- 안드로이드에서 사용자 위치를 얻으려면 콜백 메서드를 등록
  - 해당 LocationManager에다가 listener를 등록시킴
- requestLocationUpdates() 호출
- 새로운 위치가 얻어지면 onLocationChanged(Location location)이 호출됨

## 위치  관리자 콜백 메서드

- LocationManager에 requestLocationUpdates(mlocListener)를 통해서 listener 등록시킴
  - listener도 일종의 interface
- listener 내부의 메서드
  - onStatusChanged() : 새로운 상태 처리
  - onLocationChanged() : 새로운 위치 처리
    - 위치가 변경될 때마다 새로운 위치 정보를 받아올 수 있음

## 사용자 위치 정보를 얻기 위한 두 가지 권한

- android.permission.ACCESS_FINE_LOCATION
- android.permission.ACCESS_COARSE_LOCATION

## 구글 지도 v2

- 구글에서 제공하는 지도 서비스
- 3D지도를 지원
- 벡터 타일을 사용하여 다운로드 속도가 빨라짐
- 10,000 여 곳에서 실내 지도를 지원함
- 마커나 직선, 다각형 등을 지도 위에 그릴 수 있음
- 제스처로 틸트, 회전, 확대 동작을 수행할 수 있음
- 지도 정보는 안드로이드 프레임워크에 들어있는 API 개념이 아니라 각각 서비스 프로바이더들이 제공하는 API를 사용하기 위해서 SDK를 연동시켜서 앱에서 개발해야함
- 앱에다가 구글 맵스를 바로 띄우고 싶으면 `암묵적 인텐트(Intent.ACTION_VIEW)`를 사용하면 됨
  - 구글 맵스 애플리케이션을 실행하는 URI를 인텐트로 보냄
    ```java
    Uri uri = Uri.parse(String.format("geo:%f,%f?z=10", 37.30, 127.2));
    startActivity(new Intent(Intent.ACTION_VIEW, uri));
    ```

## 구글 플레이 서비스

- 구글은 안드로이드의 파편화를 완화시키기 위하여 안드로이드 운영체제의 핵심 기능들을 애플리케이션으로 독립
- 2012년도에 도입 (2008년 - 안드로이드 SDK 출시)
- 구글 맵 서비스를 이용하려면 Google Play Services라는 SDK의 API를 설치해야 함

## 구글 지도 키 얻기

- 클라이언트 컴퓨터 
  - 지도 타일 요청 + key

- 구글 서버
  - 지도 타일 보내줌

## 쉬운 구글 지도 앱 작성 단계

1. GoogleMapsBasic 프로젝트를 생성함
2. "Add an activity to Mobile" 화면에서 Google Maps Activity를 선택함
3. 액티비티 파일 이름과 레이아웃 파일 이름을 입력함
4. API 키를 생성함
5. /res/values/google_maps_api.xml 파일을 더블 클릭함
6. 프로젝트의 google_maps_api.xml 파일로 가서 "YOUR_KEY_HERE" 부분에 복사된 API키를 붙여넣음

## 인증키 생성방법

- SHA-1 인증서 지문 생성
  - Windows 실행창에서 "cmd" 실행
  - cmd 창에서 다음 명령어 실행
    ```
    #cd C:\Program Files\Android\Android Studio\jre\bin\
    #keytool -list -v -keystore
    "%USERPROFILE%\.android\debug.keystore" -alias
    androiddebugkey -storepass android -keypass android
    ```
  - SHA1 값을 복사하여 SHA-1 인증서 지문 란에 붙여넣기
  - 패키지 이름은 생성한 프로젝트의 패키지 이름 기재

## 정리

1. `locationManager`를 통해 권한을 얻어서 자신의 위치 정보를 가져오기
2. Google Map을 연동하고 Map에 선을 긋거나 아이콘을 표시