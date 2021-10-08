# 리소스 & 보안

## 기본적인 프로젝트 구성

- manifest
- java
- resource
  - 안드로이드 스튜디오에서 자동적으로 클래스 파일이나 리소스 파일로 생성되는 형태의 데이터 => (generated)

## 리소스
- 이미지, 문자열, 레이아웃, 동영상 파일등을 의미
- 리소스는 특별하게 이름 지어진 리소스 디렉토리에 모여있어야 함!
- 하나의 애플리케이션이 다양한 정보들을 반영해서 디스플레이하도록 관리
- res 디렉토리 : 리소스들이 들어있는 폴더 (최상위)
  - drawable 디렉토리 : 이미지 리소스
  - layout 디렉토리 : 사용자 인터페이스 레이아웃을 정의하는 XML 파일
  - mipmap 디렉토리 : 각기 다른 런처 아이콘 밀도에 대한 드로어블 파일
  - values 디렉토리 : 문자열, 정수 및 색깔과 같은 단순 값이 들어있는 XML 파일

- 리소스의 종류
  |디렉토리|리소스 타입|
  |--|--|
  |anim/|트윈 애니메이션을 정의하는 XML 파일|
  |color/|컬러의 상태 리스트를 정의하는 XML 파일|
  |drawable/|비트맵 파일(.png, .9.png, .jpg, .gif)이나 다음과 같은 리소스 타입으로 컴파일되는 XML파일|
  |layout/|사용자 인터페이스 레이아웃을 정의하는 XML파일|
  |menu/|애플리케이션 메뉴를 정의하는 XML 파일|
  |raw/|시스템에 의하여 압축되지 않는 원본 파일|
  |values/|단순한 값을 정의하는 XML 파일, 문자열, 정수, 색상 등이 여기에 해당됨|
  |xml/|실행 시간에 Resources.getXML()을 호출하여 읽을 수 있는 XML 파일. XML 구성(configuration) 파일은 여기에 저장됨|

## 기본 리소스와 대체 리소스

- 기본 리소스(default resource)
  - 장치 구성과 상관없이 기본적으로 사용되는 리소스
  - 기본 리소스만 있는 경우, 똑같은 레이아웃이 사용됨!

- 대체 리소스(alternative resource)
  - 특정한 장치 구성을 위하여 설계된 리소스
  - 특정 대상이나 장치에 부합하는 리소스를 가져다가 쓰도록 만들기 위한 것
    - ex) layout-large
  - 기본 리소스와 대체 리소스가 함께 있는 경우, 장치와 크기에 따라 서로 다른 레이아웃이 사용됨!
  - 제공 방법
    - 기본 디렉토리 이름에 **특정한 장치 구성의 이름을 붙인 디렉토리**에 리소스들이 저장됨
      - 기본 리소스 디렉토리 : res/drawable/
      - 대체 리소스 디렉토리 : res/drawable-hdpi/
        - hpdi : 고해상도(high-density)화면을 의미. 이들 디렉토리에 있는 이미지의 크기는 고해상도 화면의 밀도에 맞추어져 있음 (하지만 이미지 파일 이름은 기본 리소스나 대체 리소스나 모두 동일해야 함!)

## 리소스 수식자
- 대체 리소스 적용 시 우선순위 有(해당 테이블 순서)
  - 'MCC/MNC'가 우선순위 가장 높음
  - '키보드 여부'가 우선순위 가장 낮음

  |수식자|값(예시)|설명|
  |--|--|--|
  |MCC, MNC|mcc310, mcc310-mnc044|Mobile Country Code(MCC), Mobile Network Code(MNC). mcc310은 U.S의미 mcc310-mnc004는 U.S의 버라이존 의미|
  |언어구분|en, en-rUS|언어 뒤에 2글자로 된 ISO 639-1 언어코드를 붙임|
  |스크린 크기|small, normal, large, xlarge|small:QVGA 스크린, normal:전통적인 중밀도 HVGA 스크린, large:중밀도 VGA 스크린(아이패드)|
  |스크린 종횡비|long, notlong|long:세로로 긴 스크린, notlong:가로로 긴 스크린|
  |스크린 방향|port, land|port:가로(portrait)방향, land:세로(landscape)방향|
  |UI모드|car, desk, television|car:자동차에서 표시, desk:책상 위에서 표시, television:텔레비전에서 표시|
  |밤모드|night, notnight|night:밤모드, notnight:낮모드|
  |스크린 픽셀 밀도(dpi)|ldpi, mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi|ldpi(저밀도 스크린; 약 120dpi), mdpi(중밀도 스크린; 약 160dpi), hdpi(고밀도 스크린; 약 240dpi), xhdpi(고밀도 스크린; 약 320dpi), xxhdpi(고밀도 스크린; 약 480dpi), xxxhdp(고밀도 스크린; 약 640dpi)|
  |키보드 여부|keysexposed, keyshidden, keyssoft|keysexposed(장치가 하드웨어 키보드를 가지고 있고 노출되어 있음), keyshidden(장치가 하드웨어 키보드를 가지고 있으나 감추어져 있음), keyssoft(장치가 소프트웨어 키보드를 가지고 있음)|

  - OHA(Open Handset Alliance)
    - 안드로이드 관련된 표준을 정하는 단체
  - '스크린 크기'는 단순한 크기일 뿐 해상도와는 관련 없음!
    - 해상도(graphics에서 지정한 pixel값) : VGA < HD(1920*1080) < FHD(1920*1080)  < QHD(2K) < UHD(4K) < 8K
  - '스크린 픽셀 밀도(dpi)'는 주로 image에 많이 사용
    - 동일한 해상도에도 밀도(dpi)를 다르게 지정 가능! (=> 스크린 크기와 해상도는 다름!)
    - 퀄리티 좋은 앱을 만들려면, 각 해상도 별로 이미지를 다르게 지정함
    - 최근 휴대폰은 xxhdpi 혹은 xxxhdpi 사용

## 리소스 탐색 과정

- 리소스
  - 이런 앱들이 각종 스마트폰 장치에 패키지로 설치될 수 있음
  ```
  drawable/                    (X : 우선순위 가장 높은 en 없는 것부터 삭제)
  drawable-en/                 (X : 두번째 우선순위인 port가 없는 것 삭제)
  drawable-en-port/            (O)
  drawable-en-notouch-12key/   (X : 두번째 우선순위인 port가 없는 것 삭제)
  drawable-port-ldpi/          (X : 우선순위 가장 높은 en 없는 것부터 삭제)
  drawable-port-notouch-12key/ (X : 우선순위 가장 높은 en 없는 것부터 삭제)
  ```

- 장치구성
  - 어떠한 장치가 이러한 특징을 가지고 있다면, 위의 여러 대체 리소소 중에 어떤 것을 불러와서 사용할까? 
  ```
  Locale = en-GB                    // 우선순위 1
  Screen orientation = port         // 2
  Screen pixel density = hdpi       // 3
  TouchScreen type = notouch        // 4 
  Primary text input method = 12key // 5
  ```

## 리소스 참조

- 리소스는 태그나 속성 값으로 선언해서 넣음 (코딩X)
- 리소스들은 `R클래스`라는 **자동 생성되는 객체**에 의해서 코드에서 접근 가능해짐!
  - 현재 프로젝트 코드에서 R.java를 볼 수 없음(예전에는 노출되었음)
  - R.java에서 리소스 디렉토리에 있는 각 디렉토리(drawable, layout, mipmap, values)와 값들을 parsing해서 리소스 id를 생성해냄!
  - 그러면 그 id가 메모리에 존재하게 됨!
  - 메모리에 존재하는 id를 통해서 리소스에 접근할 수 있는 것!

## 지역화

- 문자열이나 통화, 이미지 같은 여러 가지 리소스들을 사용자가 있는 지역에 따라 변경하는 것
- 하나의 앱으로 여러 국가에 출시할 때 언어를 각 국가의 locale에 맞도록 지정하는 것 필요!
- 예시
  - drawable-en-mdpi/image.png
  - drawable-ko-mdpi/image.png
  - values-en/strings.xml
  - values-ko/strings.xml