// 중첩 클래스(Nested Class) -> 객체지향 / 캡슐화
// 내부 클래스(Inner Class) -> recyclerView

fun main() {
  val test1 = Test1.Test1NestedClass()
  test1.testFun1()
  
  val test2 = Test2().Test2InnerClass()
  test2.testFun2()
}

// 중첩 클래스
class Test1 {
  
  val tempText1 = "tempText1" // 접근 불가
  class Test1NestedClass {
      
      fun testFun1() {
          println("TestFun1")
          println(tempText1) // Unresolved reference: tempText1
      }
  }
}

// 내부 클래스
class Test2 {
  
  val tempText2 = "tempText2" // 접근 가능
  
  inner class Test2InnerClass {
  fun testFun2() {
          println("TestFun2")
          println(tempText2)
      }
  }
}