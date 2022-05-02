// while
// List Map -> 복습
// Iterator

fun main() {
    
  // while 문
  var count = 0
  while (count < 100) {
      println(count)
      count++
  }
  
  
  // List Map 복습
  
  val testList1 = mutableListOf("a", "b", "c")
  println(testList1)
  // 원소 하나씩 출력
  for (i in testList1) {
      println(i)
  }
  
  val testMap1 = mutableMapOf<Int, String>()
  testMap1.put(5, "유리1")
  testMap1.put(15, "유리2")
  testMap1.put(25, "유리3")
  testMap1.put(35, "유리4")
  println(testMap1) // {5=유리1, 15=유리2, 25=유리3, 35=유리4}
  // 원소 하나씩 출력
  for (i in testMap1) {
      println(i)
  }
  
  
  // Map에 원소를 추가하는 다른 방식
  val testMap2 = mutableMapOf<Int, String>()
  testMap2[5] = "유리1"
  testMap2[15] = "유리2"
  testMap2[25] = "유리3"
  testMap2[35] = "유리4"
  println(testMap2) // {5=유리1, 15=유리2, 25=유리3, 35=유리4}
  // 원소 하나씩 출력
  for (i in testMap2) {
      println(i)
  }
  
  
  // Iterator
  
  val testList2 = mutableListOf("a", "b", "c")
  
  val testIterator = testList2.listIterator()
  
  println(testIterator) // java.util.ArrayList$ListItr@b81eda8
  
  // .next() : 하나 다음 값으로 점프
  println(testIterator.next()) // a (맨 앞에서 시작)
  println(testIterator.next()) // b
  println(testIterator.hasNext()) // true
  println(testIterator.next()) // c
  println(testIterator.hasNext()) // false
  
  // .previous() : 하나 이전 값으로 점프
  println(testIterator.previous()) // c (맨 뒤에서 시작)
  println(testIterator.previous()) // b
  println(testIterator.previous()) // a
  
  println()
  
  // while문에서의 Iterator 활용
  while(testIterator.hasNext()) {
      println(testIterator.next())
  }
  
}