// Any : 아무거나 할 수 있는 느낌. 모든 아이들을 포함하는 조상

// is as 
// is : Type 맞는지 확인
// as : Type 변경 및 체크(Type Casting)

fun main() {
    
  // any
  
  var str1 : String = "abc"
  println(str1)
  str1 = 123 // The integer literal does not conform to the expected type String
  println(str1)
  
  
  var str2 : Any = "abc"
  println(str2)
  str2 = 123
  println(str2) // 123
  
  
  // is
  
  var str3 : Any = 123
  if (str3 is String) {
      println("This is String")
  } else {
      println("This is not String")
  }
  
  
  var str4 : Any = 123L
  when(str4) {
      is Int -> {println("This is int")}
      is String -> {println("This is String")}
      else -> {println("This is else")}
  }
  
  
  // as
  
  var str5 : String = "abc"
  var str6 : String = str5 as String

  println(str6) // 문제X

  var str7 : Int = 1
  var str8 : String = str7 as String // class java.lang.Integer cannot be cast to class java.lang.String

  println(str8) // 문제O

  var str9 : String? = 1 as? String // Type 변경(Casting)이 안 될 경우 null값 할당 
  println(str9) // null

  var str10 : String? = "abc" as? String
  println(str10) // abc
}