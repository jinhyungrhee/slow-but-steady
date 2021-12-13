# 안드로이드 개발패턴

- 사용자에게 보여지는 `View`와 View로부터 입력받은 입력 이벤트에 따른 내부의 `Model(=data structure)`의 변화를 분리하여 관리
- MVC, MVP, MVVM에 따라
  - Model에 대한 data structure를 interaction하는 유저 인터페이스를 정의하고 활용하는 방법이 약간씩 다름

## MVC 패턴
- Model
  - 프로그램에서 사용되는 실제 데이터 및 데이터 조작 로직을 처리하는 부분
- View
  - 사용자에게 제공되어 보여지는 UI 부분
- Controller
  - `사용자의 입력`을 받고 처리하는 부분 
- 처리과정
  - Controller로 사용자의 입력이 들어옴 (view에 대한 객체를 controller가 가져옴, controller는 Model에 대한 객체도 가지고 있음)
  - Controller는 Model을 데이터 업데이트 및 로딩
  - Model은 해당 데이터를 보여줄 View를 선택해서 화면에 출력 (Model자체가 View를 바꾸는 것처럼 동작)

## MVP 패턴

- Model
  - 프로그램에서 사용되는 실제 데이터 및 데이터 조작 로직을 처리하는 부분
- View
  - 사용자에게 제공되어 보여지는 UI 부분
  - `사용자의 입력`을 받는 부분
- Presenter
  - View에서 요청한 정보를 Model로부터 가공해서 View로 전달하는 부분
  - View와 Model에 대한 interaction을 다 처리하는 형태
- 처리과정
  - View로 사용자의 입력이 들어옴
  - View는 Presenter에 작업 요청
  - Presenter에서 필요한 데이터를 Model에 요청
  - Model은 Presenter에 필요한 데이터 응답
  - Presenter는 View에 데이터 응답
  - View는 Presenter로부터 받은 데이터로 화면에 출력

## MVVM 패턴

- Model
  - 프로그램에서 사용되는 실제 데이터 및 데이터 조작 로직을 처리하는 부분
- View
  - 사용자에게 제공되어 보여지는 UI 부분
  - `사용자의 입력`을 받는 부분
- ViewModel
  - View를 표현하기 위해 만들어진 View를 위한 Model(Data Binding 인터페이스 사용)

- 처리과정
  - View에 입력이 들어오면 Command 패턴으로 ViewModel에 명령을 내림
  - ViewModel은 필요한 데이터를 Model에 요청
  - Model은 ViewModel에 필요한 데이터를 응답
  - ViewModel은 응답받은 데이터를 가공하여 저장
  - View는 ViewModel과의 Data Binding으로 인해 자동으로 갱신됨

## 예제 : TicTacToe

- MVC 패턴
  - Model (Data Structure 로직)
    - Board
    - Cell
    - player
  - View
  - Controller