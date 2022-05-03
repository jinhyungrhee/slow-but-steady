// 간단한 계산기 문제

fun main() {
	
  sumTwo(1, 4)
  sumThree(1, 2, 3)
  minus(5, 2)
  division(10, 3) // 3
  remainder(10, 3) // 1
}

fun sumTwo(num1 : Int, num2 : Int) {
  println(num1 + num2)
}

fun sumThree(num1 : Int, num2 : Int, num3 : Int) {
  println(num1 + num2 + num3)
}

fun minus(num1 : Int, num2 : Int) {
  println(num1 - num2)
}

fun division(num1 : Int, num2 : Int) {
if (num2 != 0) {
      println(num1 / num2)
  }
}

fun remainder(num1 : Int, num2 : Int) {
  if(num2 != 0) {
      println(num1 % num2)
  }
}