// 추상클래스(Abstract class)
// 공통적으로 기능을 구현해줘야 할 때 사용

fun main() {

  //     Bike().engine()
  //     Bike().wheel()
      BMW().wheel()
      BMW().engine()
      Benz().wheel()
      Benz().engine()
      
  }
  
  abstract class Car {
      
      abstract fun wheel()
      
      abstract fun engine()
      
  }
  
  class BMW() : Car() {
      override fun wheel() { // 반드시 정의 필요
          println("BMW 굴러갑니다.")
      }
      override fun engine() { // 반드시 정의 필요
          println("BMW 시동걸립니다.")
      }
  }
  
  class Benz() : Car() {
      override fun wheel() {
          println("Benz 굴러갑니다.")
      }
      override fun engine() {
          println("Benz 시동걸립니다.")
      }
  }
  
  /*
  open class Car {
      open fun wheel() {
          println("굴러갑니다.")
      }
      open fun engine() {
          println("시동이 켜졌습니다.")
      }
  }
  
  class Bike() : Car() {
      
      override fun wheel() {
          println("자전거가 굴러갑니다.")
      }
  }
  */