// 람다(lambda)
// 람다식과 익명 함수는 함수 리터럴임
// 함수 리터럴은 선언되지 않았지만 즉시 표현식으로 전달되는 함수임

fun main() {
  println(a())
  println(b())
  println(sum(1, 2))
  println(sumNumber(3, 4))
  println(sumTypeNumber(3, 4))
  println(sumTypeNumberNull(3, 4))
  println(sumString("1", "2"))
  println(sumStringTwo("1", "2"))
  println(sumStringTypeTwo("1", "2"))
}

fun a() : String {
  return "text"
}
// 함수 a의 조금 더 간단한 형태
fun b() = "text"

fun sum(a : Int, b : Int) : Int {
return a + b
}
// 람다식 사용 (함수를 변수에 선언 가능)
val sumNumber = {a : Int, b : Int -> a + b}
val sumTypeNumber : (Int, Int) -> Int = {a, b -> a + b} // 동일(Type만 따로 빼주기)
val sumTypeNumberNull : (Int, Int) -> Int? = {_, _ -> null} // null 리턴 가능(?)

fun sumString(a : String, b : String) : String {
  return "string1 : $a string2 : $b"
}
// 람다식 사용
val sumStringTwo = {a : String, b : String -> "string1 : $a string2 : $b"}
val sumStringTypeTwo : (String, String) -> String = {a, b -> "string1 : $a string2 : $b"}