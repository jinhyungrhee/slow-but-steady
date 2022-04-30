// 엘비스 연산자(Elvis Operator) -> ?:
// null 처리를 위해 사용
// null : 아무것도 없는 것
// val str = "", val number = 0 (null X)

fun main() {
    
    var testStr1 : String = ""
    println(testStr1)
    
    var testStr2 = null
    println(testStr2)
    
    var testStr3 : String = "abcd"
    //var testStr4 : String = null // null일 수 없는 String
    var testStr5 : String? = null // null 가능한 String 
    
    println(findStringLength1("abcd")) // 4
    println(findStringLength2(null))   // null
    
    println(findStringLength3("efgh")) // 4
    println(findStringLength3(null))   // 0
    
    println(findStringLength4("안녕하세요")) // 5
    println(findStringLength4(null))        // 0
}

fun findStringLength1(str : String) : Int {
    
    return str.length;
}

fun findStringLength2(str : String?) : Int? { // 파라미터, 리턴값 모두 null일 수 있음
    
    return str?.length;  
}

fun findStringLength3(str : String?) : Int { // 조금 더 직관적인 코드
    var resultCount = 0
    if (str != null) { // null이 들어와도 길이 0을 리턴
        resultCount = str.length
    }
    return resultCount
}

// 엘비스 연산자를 사용한 조금 더 간단한 코드
fun findStringLength4(str : String?) : Int {
    return str?.length ?: 0 // null일 경우 0 리턴, 아니면 길이 리턴
}