// list 가공하기

fun main() {
    
  val testList1 = mutableListOf<Int>()
  testList1.add(1)
  testList1.add(2)
  testList1.add(3)
  testList1.add(4)
  testList1.add(10)
  testList1.add(10)
  testList1.add(11)
  testList1.add(11)
  
  println(testList1) // [1, 2, 3, 4, 10, 10, 11, 11]
  println(testList1.distinct()) // 중복 제거 : [1, 2, 3, 4, 10, 11]
  println(testList1.maxOrNull()) // 가장 큰 값 : 11
  println(testList1.minOrNull()) // 가장 작은 값 : 1
  println(testList1.average()) // 6.5
  
  // .filter {} : 필터링
  
  var testList2 = listOf("john", "jay", "minsu", "minji", "bokchi")
  
  var result1 = testList2.filter {
      it.startsWith("j")
  }
  
  println(result1) // [john, jay]
  
  
  val testList3 = listOf(1, 2, 3, 4, 5)
  
  val result2 = testList3.filter {
      it % 2 == 0
  }
  
  println(result2) // [2, 4]
  
  
  // .groupby {} : true와 false로 그룹화
  
  val testList4 = listOf("a", "aa", "aaa", "aaaa")
  
  val result3 = testList4.groupBy {
      it.length > 2
  }
  
  println(result3) // {false=[a, aa], true=[aaa, aaaa]}
  println(result3[true]) // true값만 추출 : [aaa, aaaa]
}