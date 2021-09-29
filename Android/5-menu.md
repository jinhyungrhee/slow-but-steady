# 메뉴 & 대화상자

## 안드로이드의 사용자 인터페이스

- 네비게이션바
- 액션바
- 다중 패널 레이아웃
- 제스처

- 기본적인 코딩 과정
  - 프로젝트 구성 -> XML과 액티비티의 레이아웃과 뷰들을 통해서 UI구성
  - 코드의 반 이상 UI/UX 차지
    - UI/UX 라이브러리나 위젯들을 어떻게 잘 활용하는지가 중요!

## 메뉴의 종류

- 옵션 메뉴
  - 사용자가 MENU 키를 누를 때 나타나는 메뉴 (스피너 또는 콤보박스의 개념)

- 컨텍스트 메뉴
  - 사용자가 화면을 일정 시간 이상으로 길게 누르면 나타나는 메뉴

- 팝업 메뉴
  - 버튼 밑에 팝업으로 뜨는 메뉴

## 메뉴 생성 방법

- XML로 메뉴 생성
  - \<menu> 태그 아래 \<item> 태그로 구성
  - BasicActivity로 프로젝트를 생성하면 res/menu 디렉토리에 menu_main.xml 파일이 존재함
    ```xml
    <menu xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        tools:context="com.example.basictest.MainActivity">
        <item
            android:id="@+id/action_settings"
            android:orderInCategory="100"
            android:title="@string/action_settings"
            app:showAsAction="never" />
    </menu>
    ```
  - 이렇게 생성한 파일을 MainActivity.java에서 onCreateOptionsMenu()에서 inflate시키는 것!
    ```java
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }
    ```
    - inflate(팽창) 
      - 기본 뷰 위에다가 또 다른 뷰를 얹는 것!
      - 메뉴 리소스를 **팽창(inflate)**하면 실제 메뉴가 생성됨!

  - 메뉴 클릭 시 이벤트 처리하는 메서드 : onOptionsItemSelected()
      - 예시
        ```java
            @Override
        public boolean onOptionsItemSelected(@NonNull MenuItem item) {
            System.out.println("아이템 : "+item.getTitle());
            return super.onOptionsItemSelected(item);
        }
        ```

- 코드로 메뉴 생성
  - MainActivity.java
    ```java
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.mymenu, menu);
        MenuItem item = menu.add(0, 1, 0, "배"); // 기본 xml로 만든 것에 "배" 메뉴 하나 더 추가한 것
        return super.onCreateOptionsMenu(menu);
    }
    ```


## 컨텍스트 메뉴

- UI의 어떤 항목과 관련된 동작

### 플로팅 컨텍스트 메뉴
  - 사용자가 항목 위에서 오래 누르기(long click)를 하면 메뉴가 대화 상자처럼 떠서 표시됨
  - PC에서 마우스 오른쪽 클릭을 했을 때 나오는 메뉴와 개념적으로 유사
  - 사용방법
    - onCreate() 메서드에서 registerForContextMenu()를 사용해서 컨텍스트 메뉴로 등록함
      - 특정 뷰를 해당 액티비티에 컨텍스트 메뉴로 넣을 수 있음
    - 컨텍스트 메뉴에 대해서 long click이 발생했을 경우에 나오는 메뉴를 만들어주기 위해 onCreateContextMenu() 메서드를 오버라이딩하여 메뉴를 넣어줌
    - 해당 아이템이 선택될 때 마다 onContextItemSelected() 메서드를 사용하여 어떤 메뉴가 클릭되었는지 확인 후 처리 가능

### 컨텍스트 액션 모드
    - 현재 선택된 항목에 대하여 수행할 수 있는 액션들을 제공하는 컨텍스트 액션바가 화면의 상단에 표시됨
    - 여러 항목을 선택하여 특정한 액션을 한꺼번에 적용 가능

## 팝업 메뉴

- **뷰에 부착된** 모달 메뉴(modal menu)
- API 레벨 11부터 제공
- 팝업 메뉴의 용도
  - 오버플로우 스타일 메뉴 제공
  - 서브 메뉴의 역할
  - 드롭다운 메뉴
- 사용방법
  - PopupMenu 객체를 사용하여 해당 뷰에 부착된 모달 메뉴 생성 가능
  - 넣을 메뉴를 xml로 만들어서 inflate시킴
  - 어떤 것이 select되었을 경우에 그 아이템에 대한 정보를 가져와서 특정 코드를 적용할 때 : popup.setOnMenuItemClickListener() 사용
    - activity_main.xml
      ```xml
      ...
      <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="버튼"
        android:onClick="onClick"  // onClick시 팝업이 발생함
        android:id="@+id/button" />
      ...
      ```
    - mainActivity.java
      ```java
      //...
      public void onClick(View view) {
          PopupMenu popup = new PopupMenu(this, view); // 팝업 객체 생성
          popup.getMenuInflater().inflate(R.menu.mymenu, popup.getMenu()); // 메뉴에 어떤 형식으로 넣을지 지정하여 inflate

          popup.show(); // popup 메뉴를 불러주는 popup.show() 호출 필요!
      }
      ```
    - mymenu.xml
      ```xml
      <?xml version="1.0" encoding="utf-8"?>
      <menu xmlns:android="http://schemas.android.com/apk/res/android">
          <item
              android:id="@+id/apple"
              android:icon="@drawable/ic_launcher_background"
              android:title="사과"
              />
          <item
              android:id="@+id/grape"
              android:icon="@drawable/ic_launcher_background"
              android:title="포도"
              />
          <item
              android:id="@+id/banana"
              android:icon="@drawable/ic_launcher_background"
              android:title="바나나"
              />
      </menu>
      ```

## 대화상자(Dialog)
  - 사용자에게 메시지를 출력하고 사용자로부터 입력을 받아들이는 아주 보편적인 사용자 인터페이스
  - AlertDialog(경고), ProgressDialog(진행중/로딩), DatePickerDialog(날짜선택), TimePickedDialog(시간선택) 등

### AlertDialog
  - 세가지 항목으로 구성
    - 제목
    - 콘텐츠 영역 : 메시지나 리스트, 커스텀 레이아웃 표시 (기본은 텍스트 컨텐츠)
    - 액션 버튼 : 3개 이내의 버튼

  - 사용방법
    - AlertDialogBuilder 이용해 객체 생성