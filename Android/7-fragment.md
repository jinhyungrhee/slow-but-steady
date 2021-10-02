# 고급 위젯 & 프래그먼트

## 어댑터 뷰

- 배열이나 파일, 데이터베이스에 저장된 데이터를 화면에 표시할 때 유용한 뷰
- 여러 데이터들을 Adapter라는 매개체를 통해서 일일이 뷰를 생성하지 않고도 리스트 뷰에다가 디스플레이 해주는 것
  - 공통의 형식(포맷)을 가진 대량의 데이터를 보여주는 일반적인 방식
  - Adapter에다가 데이터를 adaption시켜서 adapter가 가지는 디스플레이 뷰 형식으로 뷰를 만들어줌
  - 추상 클래스인 Adapter도 상속을 하여 많은 종류의 adapter가 존재함
    - BaseAdapter(기본)
    - ArrayAdapter(배열을 쉽게 넣을 수 있도록)
  - Adapter의 **getView()** 메서드
    - 화면의 position에 대한 정보를 구성해서 보여줌
    - position에 해당하는 항목을 긁어다가, 그 항목에 대한 화면을 구성해서 `Inflation`(팽창) 시켜줌 
- 종류 : **리스트뷰(ListView)**, 갤러리(Gallery), 스피너(Spinner), 그리드 뷰(GridView)

## 리스트뷰

- 항목들을 수직으로(또는 수평으로) 보여주는 어댑터 뷰로서 상하로 스크롤이 가능함
- adapter를 먼저 만들고 adapter를 리스트뷰에 붙여서(attach) 사용
- 사용자가 자신이 가진 데이터들을 커스터마이징하여 원하는 형식에 맞게 여러 데이터를 보여줄 수 있음

- 리스트뷰의 표준 레이아웃
  |레이아웃 ID|설명|
  |--|--|
  |simple_list_item_1|하나의 텍스트 뷰 사용|
  |simple_list_itme_2|두 개의 텍스트 뷰 사용|
  |simple_list_item_checked|항목당 체크 표시|
  |simple_list_item_single_choice|한 개의 항목만 선택|
  |simple_list_item_multiple_choice|여러 개의 항목 선택 가능|

- 사용 방법
  - xml에 \<ListView> (= 컨테이너 뷰) 생성. 그 아래 \<item>뷰로 채움.
  - 리스트뷰만 가지도록 하는 ListActivity 상속받아서 사용
    - ListActivity는 메인 root 뷰에 기본적으로 리스트뷰를 하나 가지고 있음
  - 리스트 뷰의 한 아이템에 텍스트를 넣고 싶으면 adapter를 만들 때 ArrayAdapter로 생성
    - 제네릭 뷰 \<String> 사용 : String에 대한 array를 만들어서 adapter를 만듦
      ```java
      String[] values = {"Apple", "Apricot", "Avocado", ... ,"Watermelon"};

      ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, values);
      // 리스트뷰에 adapter를 set하는 메서드
      setListAdapter(adapter);
      ```
  - 리스트 뷰에서 사용자가 특정한 항목을 선택하면 이벤트가 발생하고, 이벤트가 발생하면 `onListenClick()`메서드가 호출됨

### 예제 : 커스텀 뷰

- 리스트뷰 안에 각 아이템에 '이미지 뷰'하나와 '텍스트 뷰' 네 개로 구성됨
  - 이 아이템 하나를 xml로 정의하고 리스트뷰에다가 이 아이템에 대한 adapter를 만들어서 넣어주면 됨

## Recycler View

- 불필요한 뷰 생성이나 리소스를 많이 소모하는 `findViewById()` 조회를 수행하지 않아서 성능이 개선됨
  - 리스트뷰의 getView()메서드는 화면에서 해당 position이 나타날 때마다 finViewById()메서드를 호출함
  - 그때마다 view에 해당되는 레이아웃을 inflation 시켜서 그리는 작업들을 매번 수행함
  - 비효율적인 메모리 활용. 스크롤시 끊김 발생 가능.
- 최소한의 View 만으로도 큰 데이터를 효율적으로 스크롤링 해줌
- 기본적인 애니메이션을 제공해 사용자의 입출력 요청, 데이터 갱신이 빈번할 때 사용 가능
  - `view holder`라는 것을 만들어서 거기에 데이터를 미리 만들어서 넣어놓고 그것을 디스플레이하는 방식이기 때문
- 모든 리스트뷰는 recycler view로 호환 가능! (구현하는 방식도 비슷)
  - 리스트뷰
    - 리스트뷰 안에 여러 아이템들을 넣는 방식
    - baseAdapter나 arrayAdapter를 사용하여 리스트뷰 adapter를 만듦
  - 리사이클러뷰
    - 리사이클러뷰 위젯을 xml에다가 추가
      `<androidx.recyclerveiw.widget.RecyclerView ... />`
    - RecyclerView.Adapter사 사용하여 리사이클러뷰 adapter를 만듦(ViewHolder를 제네릭으로 전달)
    - 데이터를 유지시켜 줄 holder를 내부 클래스로 가짐
    - 리스트뷰의 getView()와 유사하게, holder를 생성하는 메서드(`onCreateViewHolder()`)와 holder를 바인딩하는 메서드(`onBindViewHolder()`)를 오버라이딩


## 그리드 뷰

- 2차원의 그리드에 항목들을 표시하는 뷰 그룹
- 그리드 뷰는 전체화면을 다 채우도록 레이아웃이 설정되어 있음
- 그리드 뷰의 속성은 이름만 가지고도 의미를 파악할 수 있음
- BaseAdapter를 상속한 ImageAdapter 사용 (ex, 갤러리)
  - getView()에서 해당 position에 오면, position에 대한 레이아웃을 그려줌 (?)

## 스피너

- 항목을 선택하기 위한 드롭 다운 리스트
  - spinner를 가져오고 spinner 객체에 setAdapter를 하면 동일하게 데이터를 spinner에 넣어서 사용 가능

## 프로그레스 바

- 작업의 진행 정도를 표시하는 위젯
- progressBar와 progressDialog를 보여줄 수 있음
  - progressDialog 객체를 만들고 그 안에 메시지를 넣을 수 있고(setMessage("")), 진행상황 값을 설정(setProgress(0~100))할 수 있음
    - 별도의 thread를 돌려서 거기에서 setProgress의 값을 변경시킴

## 시크바(Seek Bar)

- 프로그레스 바의 확장판
- 사용자가 드래그할 수 있는 썸(thumb)이 추가
- 유저의 interaction을 받아서 유저가 원하는 position에 갖다 놓을 수 있음
  - 그 값을 읽어들여서 원하는 값에 해당하는 file의 position을 이동시키고 거기서부터 display

## 프래그먼트(Fragment)

- 태블릿과 스마트폰에서 화면 다르게 하기 (화면분할)
- 액티비티 안에 여러 개의 프래그먼트를 넣을 수 있음
- 프래그먼트는 자체 뷰를 그릴 수 있는 콜백 메서드(`onCreateView()`)를 가지고 있음
  - 여기에다가 자기가 원하는 화면을 inflation시켜서 프래그먼트 화면을 구성함
  - layout화면을 별도로 구성해서 위에다가 덮어씌우는 것(팽창:inflate)
- 기본적으로 android에서는 layout 디렉토리의 이름에 따라서 화면 별로 다르게 적용되도록(리소스를 만들어내도록) 설계되어 있음
  - 스마트폰 화면은 default(layout 디렉토리)
    - default는 layout이라는 디렉토리에 있는 코드들을 가져다가 사용
  - 큰 화면 기기는 layout_large 디렉토리
    - 여기에 있는 xml 파일들을 가지고 레이아웃 구성함
    - (layout-large 디렉토리를 생성해도 안에 아무것도 없으면 프로젝트 창에 뜨지 않음!)

## PIP 모드
- 이미지는 still이므로 한번 이미지를 이미지뷰에 bitmap으로 draw하면, 그걸 그려서 graphics pipeline을 통해서 linux를 통해서 frame buffer에다가 이미지를 그리면 그것이 static 형태로 데이터가 고정되기 때문에 buffer가 데이터 변경 없이 그대로 display할 수 있음
  - graphics pipeline : 궁극적으로 android에 display하는 소프트웨어와 하드웨어의 연결 통로
    - pipeline에는 동적으로 스크롤되는 화면에서도 동영상이 display 되도록하는 위젯이나 프레임워크 컴포넌트들이 존재 (Ex, PIP)

- PIP(Picture In Picture)
  - 작은 창을 만들어서 그곳에다가 display
  - 버튼을 누르면 화면 자체를 FrameLayout에다가  집어넣는 것
  - SDK 26버전 이상부터 지원 (SDK 버전을 체크하는 코드 필요)


  ### 제네릭 타입
  
  - 데이터 타입들이 딱 한 개로 정해지는 것이 아님
  - 대부분의 클래스나 인터페이스들이 define할 때는 제네릭 타입으로 define하고 사용할 때는 자신이 원하는 형식의 데이터를 넣어서 사용