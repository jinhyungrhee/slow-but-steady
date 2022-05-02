// 리스트와 filter
// 물음표와 느낌표
// 반복문

fun main() {
    
  // 리스트 생성 방법1
  val testList1 = ArrayList<String>()
  testList1.add("a")
  testList1.add("b")
  testList1.add("c")
  
  println(testList1) // [a, b, c]
  println(testList1[0]) // a
  println(testList1[1]) // b
  println(testList1[2]) // c
  
  // 리스트 생성 방법2
  val testList2 = listOf("a", "b", "c")
  println(testList2) // [a, b, c]
  
  // 리스트 생성 방법3
  val testList3 = mutableListOf<String>("a", "b", "c") // == mutableListOf("a", "b", "c")
  println(testList3) // [a, b, c]
  
  
  val testList4 = listOf("student1", "student2", "student3", "student4", "teacher1", "student5")
  println(testList4) // [student1, student2, student3, student4, teacher1, student5]
  
  // 앞자리가 's'로 시작하는 것들만 가져오기(filter)
  println(testList4.filter {it.startsWith("s")}) // [student1, student2, student3, student4, student5]
  
   val testList5 = listOf("student1", "student2", "student3", "student4", "teacher1", "student5", null)
   println(testList5)
   // println(testList5.filter {it.startsWith("s")}) // null이 포함된 경우 filtering 불가!
   // Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type String? 에러 발생!
   println(testList5.filterNotNull().filter {it.startsWith("s")}) // .filterNotNull() : null이 아닌 것들만 가져옴!
   
   
  
  // 물음표(?)와 느낌표(!)
  var test1 : String = "a"
  var test2 : String = "b"
  
  test1 = test2
   
  println(test1) // b
  
  var test3 : String = "c"
  var test4 : String? = "d"
  
  //test3 = test4 // Type mismatch: inferred type is String? but String was expected 에러 발생
  test3 = test4!! // !! : "null이 아니다" 의미 (에러 발생 X)
  println(test3) // d
  
  
  
  // 반복문
  
  val testList6 = listOf("a", "b", "c", "d", "e", "f")
  for (i in testList6) {
      print(i + " ") // a b c d e f
  }
  
  
  
  // 1부터 10까지 출력
  for (i in 1..10) {
      print(i) // 12345678910
  }
  
  println()
  
  // 2씩 증가
  for (i in 1..10 step 2) {
      print(i) // 13579
  }
  
  println()
  
  for (i in 1..3) {
//         println("i의 값은 : " + i)
      println("i의 값은 : $i")
//         print(" " + i) // 가능
//         print(i + " ") // 불가 (왜?)
  }
  
  // 중첩 반복문
  for (i in 1..3) {
      for (j in 1..3) {
          println("i is $i j is $j")
  }
  }
}