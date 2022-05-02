// 구구단 출력

fun main() {
    
  for (i in 2..9) {
      for (j in 1..9) {
          val result = i * j
          println("$i * $j : $result")
      }
  }
}