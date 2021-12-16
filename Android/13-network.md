#  네트워크

## 안드로이드에서의 네트워크
- 3G,4G
- 와이파이 - Ethernet 기반 (`TYPE_WIFI`)
- 블루투스 (용도 한정, 근거리 통신망)
- NFC (용도 한정, 근거리 통신망)

- smartphone (All IP ver6)
  - IP망 : 컴퓨터 네트워크
  - 통신망 : 유선 -> 이동통신 (4G, 5G, LTE) - chip 기반(`TYPE_MOBILE`)

## 네트워킹 상태 조회

- ConnectivityManager클래스는 네트워크 연결 상태를 감시하고 만약 네트워크 연결 상태가 변경되면 다른 애플리케이션에게 방송한다.
  - ConnectivityManage : 네트워크 연결을 관리하는 매니저  
  `ConnectivityManager manager = (ConectivityManager)getSystemService(Context.CONNECTIVITY_SERVICE);`
  - getSystemService() : 각 매니저 가져오는 메서드
  - getActiveNetworkInfo() : 현재 네트워크 정보 가져옴

- permission 권한 필요
  - `android.permission.ACCESS_NETWORK_STATE"` : 네트워크 상태 가져오기


## 웹에서 파일 다운로드

- HTTP 프로토콜를 이용하여 네트워크에서 파일을 다운로드할 때는 `HttpURLConnection` 사용
  - openInputStream, openOutputStream 사용
- 메인 스레드에서 직접 파일을 다운로드하면 `NetworkOnMainThreadException` 발생
  - 네트워크는 response를 보장할 수 없음
  - AsynTask나 별도의 Thread를 생성해 진행해야함!
- 예제 코드
  - onPostExecute() : Main Thread의 UI 접근 가능
  - AndroidManifest.xml
    - "android.permission.INTERNET" : 인터넷 접근 권한
    - "android.permission.ACCESS_NETWORK_STATE" : 네트워크 상태 가져오기
    - `<application android:usesCleartextTraffic = "true" ...>` : 보안&트래픽 관련 attr 추가해야 네트워크로부터 데이터 다운 가능! 


## 중간 정리

- HTTP Protocol을 통해 android mobile program에서 웹 service programming을 할 수 있다.

## 모바일 애플리케이션의 종류

- 안드로이드 SDK를 사용하여 개발하고 `APK 형식`으로 사용자 장치에 설치되는 클라이언트 쪽 어플리케이션
- `웹앱(Web App)`으로 웹 표준을 사용하여 개발하고 사용자는 웹 브라우저를 통해 액세스하는 방법이다. 사용자 장치에 설치할 필요X

## 웹 앱의 종류

- 종류
  - 웹 페이지 -> 안드로이드 브라우저
  - 웹 페이지 -> `WebView`로 작성된 안드로이드 앱 - 안드로이드 시스템에서 web을 display하는 engine
- 장점
  - 네이티브 앱은 수정사항이 생기면 계속 update해줘야함 -> 웹 앱은 그럴 필요 없음
  - 동일한 플랫폼에서 여러가지 장치들에 동일하게 제공 가능

## WebView 위젯

- 안드로이드에서 웹 서버로부터 웹 페이지를 읽어서 웹 브라우저처럼 화면에 표시하는 것이 가능할까?
  - `WebView` 위젯을 사용하면 가능
- WebView 위젯은 `WebKit`이라는 엔진을 사용하여 HTML 문서를 해석해서 화면에 그려줌!

## XML 처리

- 인터넷을 통하여 전달되는 데이터는 주로 XML형식(open API에서 데이터 받아오는 경우-JSON/XML)
  - Document object 사용
  - 과정
    - xML문서 -> XML파서 -> DOM(Document Object Model) 트리

## XML 파서
- **DOM 파서**
- SAX 파서
- PullParser 파서

## DOM
- DOM(Document Object Model)은 W3C의 표준으로, XML문서에 접근하고 처리하는 표준적인 방법을 정의
- XML 문서를 트리 구조로 표현한 것
- DOM은 문서 요소의 객체(object), 특징(property), 메서드(interface)를 정의