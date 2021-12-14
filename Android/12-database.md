# Database & Firebase

## 데이터 스토리지

- 기본적으로 스토리지는 I/O임
  - I/O의 대상은 FILE, 데이터를 구조적으로 관리하기 위한 DB
- 데이터를 읽고 쓰는 용도와 구조적으로 데이터를 관리하는 용도는 데이터 스토리지에서 관리
- 모바일에서는 **SD카드**라는 스토리지 장치를 사용(내장된 SD카드, NandFlash)
  - 리눅스 운영체제에서 파일 시스템으로 마운트(mount)를 해서 저장 장치로 사용
    - **mount** : 논리적인 파일 시스템 구조가 특정 운영체제에 연결되어서 해당 파일 시스템 구조 안에 있는 폴더나 파일들을 볼 수 있도록 하는 동작
  - 리눅스 파일시스템은 `ext4` 형식의 파일시스템 사용 (안드로이드는 리눅스 파일시스템 그대로 사용)
  - 실제로 패키지를 설치하면 루트 파일시스템 밑에 존재하는 android/user/data/...가 설치가 되는 것
- 파일과 관련된 데이터
  - 저장소가 각종 어플리케이션에 설치되는 어플리케이션 패키지의 패스 안에 저장되는 파일들 => `내부 저장소`
  - 외부 장치와 연결해서 볼 수 있는 영역 => `외부 저장소`
- 데이터베이스
  - DBMS에 의해서 구조적인 데이터로 관리되는 시스템
  - 하나의 파일 형태로 만들어지만, 사용자가 접근할 때에는 Query문법을 통해 DBMS에 의해서 접근함.
    - android에서 사용하는 아주 가벼운 DBMS => `SQLite`
- `내부 저장소`, `외부 저장소`, `데이터베이스`는 안드로이드 모바일 폰 자체에 대해서 로컬로 데이터를 관리하는 방법임!
- 요즘에는 네트워크 프로그래밍을 통해 클라우드 시스템에서 데이터를 관리, 공유해서 사용 => `웹 서버`
  - 자체 구글 클라우드의 NoSQL 기반의 데이터베이스 서비스 제공 => `firebase`
    - NoSQL : 빅데이터 환경이 중요해지면서 기존의 SQL기반 RDBMS에서 벗어나서, 데이터를 조금 더 유연하게 관리할 수 있는 방법
    - 클라우드 시스템을 통해서 여러 모바일을 동기화시킬 수 있도록 데이터 관리

## 데이터를 저장하는 방법

- 로컬 스토리지 : SD 카드 스토리지 기반으로 데이터 관리
  - 공유 프레퍼런스(Shared Preference)
    - 키-값(key-value) 쌍으로 사적이고 기초적인 데이터를 저장
  - 내부 저장소(Internal Storage)
    - 사적인 데이터를 내부 저장소에 저장
  - 외부 저장소(External Storage)
    - 공유 데이터를 공유 외부 저장소에 저장
- 데이터 베이스(SQLite Database)
  - 구조화된 데이터를 사적인 데이터베이스에 저장
- 네트워크 연결(Network Connection)
  - 데이터를 네트워크 서버에 저장

## 공유 프레퍼런스(Shared Preference)

- 안드로이드 프레임워크에서 제공하는 아주 간단한 데이터 저장 객체
- 애플리케이션의 환경 설정
- 기초적인 자료형을 `키-값 쌍`으로 저장하고 복원할 수 있는 방법
- 저장된 데이터는 사용자 애플리케이션이 종료되더라도 저장함
- 공유 프레퍼런스를 얻는 방법(ActivityManager의 Shared Preference를 접근하는 API 메서드)
  - getSharedPreferences(name, mode)
    - SharedPreference 객체 반환
    - name : 이미 존재하면 해당 객체 가져오고, 없으면 지정한 이름으로 특정 객체의 SharedPreference를 만들어서 반환
    - mode : public, private.. 
  - getPreferences(mode)
- 이는 가장 최근에 입력되었던 값을 불러오는 용도로 사용될 수 있음!

## 프레퍼런스 파일에서 값을 읽거나 쓰는 메서드

- 타입별로 읽을 수 있는 함수 메서드
  - getBoolean(String Key, boolean defValue) : defValue는 없으면 반환되도록 하는 기본값
  - getInt(String Key, int defValue)
  - getString(String Key, String defValue)

- Shared Preference의 edit() 메서드
  - Editor 객체를 가져와서 거기에다 putXXX()메서드를 적용함

- Shared Preference에 타입 별로 값을 넣는 메서드
  - putBoolean(String Key, boolean value)
  - putInt(String Key, int value)
  - putString(String Key, String value)

- Shared Preference의 commit() 메서드
  - 값을 넣은 뒤에 동기화하는 메서드

  ## 내부/외부 저장소

  - Java File I/O method를 그대로 사용할 수 있음
  - 내부 저장소와 외부 저장소는 서로 다른 경로에 저장됨
    - 내부 : /data/user/0/com.example.storagetest/files
    - 외부 : /storage/emulated/0
      - 해당 디렉토리 아래에는 DCIM, Documents, Download, Movies, Music, Pictures 등이 존재함
    - 현재 시스템의 FILE 시스템 구조 확인하기(linux ext4 파일 시스템을 루트로 사용)
      - View 탭 - Tool Windows - Device File Explorer
  - 내부 저장소
    - 하나의 앱에서 내부 저장소에 저장하면 자신의 패키지 안에 별도의 폴더를 생성해서 그곳에 파일 저장
    - 내부 저장소는 파일 이름만 주고 특정한 경로를 지정하지 않음
    - `openFileInput()` 메서드를 통해 file을 open하면 바로 FileInputStream 객체를 통해 바로 input stream을 다운받을 수 있음
    - 파일을 쓸 때는 `openFileOutput()` 메서드 사용
  - 외부 저장소
    - ex) 사진을 찍으면 외부저장소의 DCIM 디렉토리에 사진이 저장됨
    - 해당 데이터를 공유할 수 있도록 공유 외부 저장소에 저장하는 것

## FILE I/O

- Java는 어떤 데이타를 file에 읽고 쓰기 위해 특정 `FILE 객체`를 생성해야 함. 
- FILE에 데이터를 쓸 때는 OutputStream 객체 사용 (`FileOutputStream`/`ObjOutputStream`/`BufferedOutputStream` 등)
- FILE로부터 데이터를 읽을 때는 InputStream 객체 사용 (`FileInputStream`/`ObjInputStream`/`BufferedInputStream` 등)


## 내부 공간에 파일 만들기

- 애플리케이션은 장치의 내부 저장 공간에 파일을 저장할 수 있음
  - ex) /data/user/0/com.example.storagetest/files
- 내부 저장 공간에 저장되는 파일은 해당 어플리케이션만 접근이 가능함
- 사용자가 애플리케이션을 제거하면 이들 파일들도 제거됨
- 앱을 삭제하면 패키지 전체가 삭제되므로 그때 내부저장소에 저장된 파일들도 모두 삭제가 됨

## 내부 공간과 외부 공간 비교

|내부 공간|외부 공간|
|--|--|
|항상 사용 가능|항상 사용 가능하지 않음. 사용자가 SD카드를 제거하면 사용 불가|
|이곳에 저장되는 파일은 해당되는 앱만 사용 가능|누구나 읽을 수 있음|
|사용자가 앱을 제거하면 시스템에 의해 앱이 사용했던 공간이 삭제됨|사용자가 앱을 제거할 때 공용 디렉토리에 저장된 파일은 삭제되지 않음. 다만 getExternalFilesDir()가 반환하는 디렉토리에 파일을 저장한 경우만 시스템이 삭제함|

## 외부 미디어 장착 여부 검사

- mount가 되어 있으면 외부 장치가 파일 시스템 형태로 장착되어 있는 것임! : `state.equals(Environment.MEDIA_MOUNTED)`

```java
String state = Environment.getExternalStorageState();
if(state.equals(Environment.MEDIA_MOUNTED)) {
  // 미디어에 읽고 쓸 수 있음
} else if(state.equals(Environment.MEDIA_MOUNTED_READ_ONLY)) {
  // 미디어를 읽을 수 있음
} else {
  // 읽거나 쓸 수 없음
}
```

## 외부 저장소 접근 권한 필요

```xml
<manifset ...>
  <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
  <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"  />
  ...
</manifest>
```
---------------------------------------------------------------------------------

## 안드로이드에서의 데이터베이스(구현 측면)

- 방식
  - 서버에서 관리(Network 사용)
    - MySQL, MSSQL을 사용하여 Table 구성하여 구조적으로 데이터 관리(RDBMS) / MongoDB, NoSQL 활용
  - 모바일에서 관리(phone 자체의 database)
    - 간단한 DBMS(SQLite) 탑재

- SQLite
  - IOS Safari, Android Native Library 등에서도 사용
- Android Hierarchy 구조
  - Android Framework 아래에 C/C++ Library가 존재함. C/C++ Library에는 web kit, web engine, OpenGL 등이 Native Library로 구현되어 있음. 거기에 **SQLite**도 Native Library로 구현되어 있음!
  - Android Framework에서 Native Library에 접근할 수 있는 API 객체들을 만들어줘서 유저레벨에서 JAVA코드로 이곳에 접근할 수 있음!
- Content Provider
  - 안드로이드 시스템에 있는 각종 데이터(연락처, 전화기록, 전화번호, 비디오, 오디오, 웹브라우저)들을 모두 SQLite 데이터베이스 테이블로 관리가 됨. 유저가 이를 쉽게 사용할 수 있도록 각종 데이터를 데이터베이스화 시키고 그러한 데이터들을 제공하는 컴포넌트임!
- www.sqlite.org
- SQLite는 안드로이드와 아이폰을 비롯한 많은 모바일 장치에서 사용되는 데이터베이스
- SQL을 거의 완전하게 지원
- embedded 시스템에서 가볍게 사용될 수 있도록 만들어진 DBMS
- 내부 데이터를 관리하는 트리는 B+ Tree 사용
- 하나의 데이터베이스 테이블 당 하나의 데이터베이스 파일을 만들어서, 파일 당 데이터베이스 테이블을 관리하도록 함!

## 데이터베이스

- 행(row) 또는 레코드(record)
- 컬럼(column)
  - 하나의 데이터 레코드를 구성하는 데이터 컨텐츠 내용 

## SQL

- 데이터 정의 명령어(Data Definition Language) : 테이블 관련 명령어
  - CREATE
  - ALTER
  - DROP
  - USE
- 데이터 조작 명령어(Data Manipulation Language) : 데이터를 가져오거나 업데이트하는 명령어
  - SELECT
  - INSERT
  - DELETE
  - UPDATE

## 결과 집합(Result Sets)과 커서(Cursors)

- 안드로이드 시스템에서 Query를 했을 때 그 결과로 반납되는 객체 => `커서(Cursor)`
  - moveToFirst(), moveToNext(), MoveToLeft()등의 메서드를 통해 조작 가능!

## 안드로이드에서 데이터베이스 사용하는 2가지 방법

- SQLiteOpenHelper(Abstract Class)를 사용하는 방법
  - SQLiteOpenHelper 객체를 상속받아서 class를 정의(DBHelper 클래스)
  - onCreate() : 데이터베이스 안에 테이블과 초기 데이터를 생성함. 버전을 argument로 넣어줌
  - onUpgrade() : 데이터베이스를 업그레이드 함. 버전을 argument로 넣어줌

- openOrCreateDatabase() 메서드로 데이터베이스 객체를 직접 생성하는 방법

## 데이터베이스와 어댑터

- SimpleCursorAdapter 객체는 데이터베이스와 화면을 연결함
- 데이터베이스에서 데이터를 읽어서 정해진 레이아웃으로 화면에 표시함
- 데이터베이스에 있는 레코드를 가져와서 레코드의 항목들을 하나하나씩 어댑터뷰에 접목시킴

-------------------------------------------------------------------------------------------------

## Firebase

- Backend as a Service(BaaS)를 제품으로 제공하는 회사였으며 2014년 10월에 Google에 인수됨
- 모든 서비스들은 개발툴에서 손쉽게 코딩할 수 있도록 Adroid와 iOS, 웹/앱 전용 SDK를 제공
- 기반 데이터 포맷은 `JSON`이며, 웹이나 모바일 앱에서 제한없이 사용가능
- Android를 포함하여 iOS와 Web용 클라이언트 SDK가 있으며, Firebase 콘솔에서 설정용 `google-services.json` 파일을 다운로드 받아 Android Studio 프로젝트에 적용하는 방식으로 Firebase와 Android 앱간 연동을 위한 설정이 완료됨
- 각 앱마다 firebase 프로젝트에 연결되어서 사용하는 것
- 특징
  - Firebase는 분석, 데이터베이스, 메시징, 오류 보고 등의 기능을 제공하므로 개발자는 개발 속도를 높이면서 사용자에게 집중할 수 있음
   - Firebase는 Google 인프라 위에서 자동으로 확장되므로 대규모 앱도 문제 없음
   - Firebase 제품은 개별적으로도 뛰어나지만 데이터와 통계를 서로 공유하여 더 큰 효과를 발휘할 수 있음
- 주요 기능
  - Firebase ML (머신러닝)
  - Authentication (사용자 인증)
  - Cloud Storage
  - Realtime Database (실시간 앱 데이터 저장 및 동기화) 등

## Firebase 설정

- Tools - Firebase - Realtime Database

## Firebase 적용 (Realtime Database)

- DatabaseReference 가져오기
  - private DatabaseReference mDatabase;
  - mDatabase = FirebaseDatabase.getInstance().getReference(); 
    - Firebase의 Realtime Database의 Root 데이터베이스 레퍼런스를 가져오게 됨
- 데이터 읽기 및 쓰기
  - 기본 쓰기 작업은 setValue() 코드를 사용하여 지정된 참조에 데이터를 저장하고 해당경로의 기존 데이터를 모두 바꿈
  - 사용 가능한 JSON 유형
    - String  
    - Long
    - Double
    - Boolean
    - Map\<String, Object>
    - List\<Object>