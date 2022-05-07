// class

// function -> 기능
// class -> 설계 + 기능

fun main() {
    
  println(Test().a) // abc
  println(Test2("abcd").b) // abcd
  Test3().test3Fun() // test3Fun 출력
  
  // 재사용 불가
  val myInfo = MyInfo() // MyInfo 클래스 선언
  println(myInfo.getMyAge())
  println(myInfo.getMyName())
  println(myInfo.getMyLocation())
  
  // 재사용 가능
  val dog1 = Dog("Shih Tzu", 8)
  println(dog1.getMyDogInfo())
  
  val dog2 = Dog("Poodle", 5)
  println(dog2.getMyDogInfo())
  
  // init {} : 객체 생성 시 동작 
  initTest() // 여기에서 뭔가 해주고 싶음
  
  initTest().testInitFun() // 여기에서 뭔가 해주고 싶음
             //	testInitFun

  InitialValue("박보검", 20) // 박보검
                // 20
  
  InitialValue2("박보검") // 박보검
               // 20
  
  InitialValue2("홍길동", 30) // 홍길동
                 // 30
  
}
class InitialValue2(name : String, age : Int = 20) {
  
  init {
      println(name)
      println(age)
  }
}

class InitialValue(name : String, age : Int) {
  
  init {
      println(name)
      println(age)
  }
}

class initTest() {
  
  // 선언할 때 뭔가 해주고 싶은 경우
  init {
      println("여기에서 뭔가 해주고 싶음")
  }
  
  fun testInitFun() {
      println("testInitFun")
  }
}


class Dog(name : String, age : Int) {
  
  val dogName = name
  val dogAge = age
  
  fun getMyDogInfo() : String {
      return "$dogName : $dogAge"
  }
}


class MyInfo() {
  
  fun getMyAge() : Int {
      return 20
  }
  
  fun getMyName() : String {
      return "My Name is OOO"
  }
  fun getMyLocation() : String {
      return "Seoul"
  }
}
class Test3() {
  
  // 메소드
  fun test3Fun() {
      println("test3Fun 출력")
  }
}

class Test2(str : String) {
  val b = str   
}

class Test {
  val a = "abc"
}