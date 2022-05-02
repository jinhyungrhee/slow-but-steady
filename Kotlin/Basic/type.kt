// 자료형 -> 숫자(int, long, double, float), 문자(string), boolean(true, false)
// 형변환
// null type

fun main() {
    
  val test1 = "1234"
  val test2 = 1234
  
  println(test1 + 1) // 12341
  println(test2 + 1) // 1235
  
  // 데이터 타입 출력
  println(test1::class.java.simpleName) // String
  println(test2::class.java.simpleName) // int
  
  val test3 = 1234.1234
  println(test3::class.java.simpleName) // double
  
  
  val test4 : Int = 1234
  println(test4)
  
  // 타입을 잘못 지정한 경우
  val test5 : Int = "1234"
  println(test5) // Type mismatch 에러 발생

  val test6 : Int = 1234123412341234 // The value is out of range (int가 커버할 수 있는 숫자 범위 넘어감)
  val test7 : Long = 1234123412341234
  println(test6)
  println(test7)
  
  val test8 : Float = 1234.1234f
  println(test8)
  
  // 데이터 타입 변경
  val test9 : Int = 1234
  val test10 = test9.toString()
  println(test10::class.java.simpleName)
  
  val test11 : String = "1234"
  val test12 = Integer.parseInt(test11)
  println(test12::class.java.simpleName) // int
  println(test12 + 1234) // 2468
 
  
  // null -> kotlin에서 null인지 아닌지 체크하는 것 엄격함!
  
  val test13 = "" // 빈 문자열
  val test14 = null // 아예 없는 값
  
  println(test13) // 
  println(test14) // null
  
  // "null일수도 있고 아닐 수도 있다" 선언 (?)
  //val test15 : String = null // Null can not be a value of a non-null type String 에러 발생
  val test16 : String? = null
  println(test16) // null
  val test17 : String? = "abcd"
  println(test17) // "abcd"
  
}