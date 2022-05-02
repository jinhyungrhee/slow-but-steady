// List
// Map
// Set

fun main() {
    
  // List 자료구조
  
  val testList1 = listOf("a", "b", "c")
  println(testList1)
  println(testList1[0])
  // testList1.add("d") // Unresolved reference: add 에러 발생!
  
  
  // mutableList 사용
  val testList2 = mutableListOf("a", "b", "c")
  testList2.add("d") // add 가능
  println(testList2) // [a, b, c, d]
  testList2.remove("a")
  println(testList2) // [b, c, d]
 
  
  // Map 자료구조
  
  // 5 - 유리, 10 - 철수, 15 - 짱구, 22 - 훈이
  val mutableList1 = mutableListOf<Int>()
  mutableList1.add(5)
  mutableList1.add(10)
  mutableList1.add(15)
  mutableList1.add(22)
  println(mutableList1)
  
  val mutableList2 = mutableListOf<String>()
  mutableList2.add("유리")
  mutableList2.add("철수")
  mutableList2.add("짱구")
  mutableList2.add("훈이")
  println(mutableList2)
  
  // 약간 번거로운 방식
  val findIndex = mutableList1.indexOf(10)
  println(findIndex) // 1
  println(mutableList2[findIndex]) // 철수
  
  // 개선된 방식 : map 사용!
  val testMap1 = mutableMapOf<Int, String>()
  testMap1.put(5, "유리") // key - value
  testMap1.put(10, "철수")
  testMap1.put(15, "짱구")
  testMap1.put(22, "훈이")
  println(testMap1[10]) // 철수
  
  
  // Set 자료구조 - 중복 허용X, 입력 순서 허용O(?)
  
  val testSet1 = mutableSetOf("a", "b", "c")
  println(testSet1)

  testSet1.add("e")
  testSet1.add("d")

  println(testSet1) // [a, b, c, e, d]
  
  testSet1.add("e")
  testSet1.add("e")
  testSet1.add("e")
  testSet1.add("e")
  
  println(testSet1) // [a, b, c, e, d]
  
  testSet1.remove("e")
  println(testSet1) // [a, b, c, d]
  
  
}