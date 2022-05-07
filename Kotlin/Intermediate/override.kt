/**
상속(Inheritance)과 오버라이딩(Overriding)
 */

fun main() {
    
  //    Parents().disease()
    Child().doing() // 부모클래스의 메소드 그대로 사용
    Child().disease() // 부모클래스의 메소드 그대로 사용
  }
  
  open class Parents() {
      
  //     init {
  //         println("이 것은 부모입니다.")
  //     }
      fun doing() {
          println("자식을 돌봅니다.")
      }
      
       open fun disease() { // open : 자식 클래스에서 재정의하여 사용하기 위해
          println("비염이 있습니다.")
      }
  }
  
  class Child() : Parents() {
      
  //     init {
  //         println("이 것은 자식입니다.")
  //     }
  
      override fun disease() {
          //super.disease() // 재정의하지 않고 그대로 사용
          println("겁이 많습니다")
      }
  }