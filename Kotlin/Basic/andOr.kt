// 논리연산
// AND OR
// 남자이면서 20세 이상 -> AND (둘 다 만족)
// 남자이거나 30세 이상 -> OR (둘 중 하나만 만족)

fun main() {

    
  val a = "남자"
  val b = 10
  
  // AND
  if (a == "남자" && b >= 20) {
      println("AND 만족")
  } else { 
    println("AND 불만족")
  }
  
  // OR
  val c = "여자"
  val d = 30
  if (c == "남자" || d >= 30) {
      println("OR 만족")
  } else {
      println("OR 불만족")
  }
  

  val student = mutableMapOf<Int, String>()
  
  student[99] = "민지"
  student[20] = "철수"
  student[35] = "민수"
  student[48] = "가영"
  student[100] = "하영"
  student[22] = "수진"
  student[45] = "수달"
  student[88] = "캥거루"
  student[91] = "코알라"
  student[87] = "악어"
  student[54] = "코끼리"
  student[42] = "하마"
  student[10] = "크로커다일"
  
  // 학생들 중에 점수가 50점 이상이고(AND) 이름 길이가 3 이상인 학생들만 출력
  for (i in student) {
      if (i.key >= 50 && i.value.length >= 3) {
          println(i.value)
      }
  }
  
}
