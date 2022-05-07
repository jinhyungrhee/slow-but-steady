// 인터페이스(Interface)

fun main() {
	
  //     BMW().wheel()
  //     BMW().engine()
  
      BMW().autoDriving()
      BMW().autoParking()
  }
  
  abstract class Car {
      abstract fun wheel()
      
      abstract fun engine()
  }
  
  // interface는 일종의 작은 틀
  interface CarAutoDriving {
      fun autoDriving()
  }
  
  interface CarAutoParking {
      fun autoParking()
  }
  
  class BMW() : Car(), CarAutoDriving, CarAutoParking { // Interface를 끼워넣어서 사용
      
      override fun wheel() {
      println("BMW 굴러감")
      }
      
      override fun engine() {
          println("BMW 엔진 시동")
      }
      
      // 갑작스럽게 옵션이 추가된 경우 -> abstract 클래스 사용
      //fun autoDriving() {
      //    println("BMW 자율 주행")
      //}
      
      // Interface 사용
      override fun autoDriving() {
          println("BMW 자율 주행")
      }
      override fun autoParking() {
          println("BMW 자동 주차")
      }
  }
  
  class Benz() : Car() {
      override fun wheel() {
      println("Bezn 굴러감")
      }
      
      override fun engine() {
          println("Benz 엔진 시동")
      }
      
      // 갑작스럽게 옵션이 추가된 경우
      fun autoParking() {
          println("Benz 자동 주차")
      }
  }
  
  /*
  interface Car {
      
      fun wheel()
      fun engine()
  }
  
  class BMW() : Car {
      
      override fun wheel() {
          println("BMW 휠 돌아감")
      }
      
      override fun engine() {
          println("BMW 엔진 돌아감")
      }
  }
  */