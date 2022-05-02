// 조건문
// if else
// when

fun main() {
    
  val studentScore1 = 100
  
  if (studentScore1 > 150) {
      println("150이상")
  } else {
      println("150이상이 아님")
  }
  
  
  val studentScore2 = 50
  if (studentScore2 > 50) {
      println("50 초과")
  }
  if (studentScore2 >= 50) {
      println("50 이상")
  }
  
  
  
  val studentScore3 = 65
  if (studentScore3 < 70) {
      println("70미만")
  }
  if (studentScore3 <= 70) {
      println("70이하")
  }
  
  
  val studentScore4 = 10
  if (studentScore4 > 100) {
      println("100보다 큼")
  } else if (studentScore4 > 50) {
      println("50보다 큼")
  } else if (studentScore4 > 30) {
      println("30보다 큼")
  } else {
      println("30보다 작음")
  }
  
  // when -> switch문 처럼 사용!
  
  val score = 70
  when(score) {
      100 -> {
          println("100")
      }
      90 -> {
          println("90")
      }
      80 -> {
          println("80")
      }
      else -> {
          println("no")
  }
  }
}