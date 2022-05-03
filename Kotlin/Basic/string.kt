// 문자열 가공
// 유저가 입력한 데이터를 가공하거나
// 서버에서 가져온 데이터를 알맞게 가공해서 씀

fun main() {
    
	
  // .split() : parameter를 기준으로 분할한 뒤 '리스트' 생성
  
  val testString = "동해물과 백두산이 마르고 닳도록"
  val newTestString = testString.split(" ") // 리스트 생성
  println(newTestString) // [동해물과, 백두산이, 마르고, 닳도록]
  println(newTestString[1]) // 백두산이
  
  
  val testString2 = "동해물과 백두산이 마르고 닳도록"
  println(testString2[1]) // 해
  println(testString2[1].toString() + testString2[2].toString()) // 해물
  
  // 간단하게 일부분만 가져오기
  val splitString = testString2.substring(1, 3)
  println(splitString) // 해물
  
  // 전체 다 가져오기
  val splitString2 = testString2.substring(0, testString2.length)
  println(splitString2) // 동해물과 백두산이 마르고 닳도록
  
  
  // 일부분 바꾸기
  
  val testString3 = "동해물과 백두산이 마르고 닳도록"
  
  val replaceValue = testString3.replace("백두산", "한라산")
  println(replaceValue) // 동해물과 한라산이 마르고 닳도록
  
  
  val testList = ArrayList<String>()
  testList.add("abc1@naver.com")
  testList.add("abc2@google.com")
  testList.add("abc3@daum.com")
  testList.add("abc4@kakao.com")
  testList.add("abc5@naver.com")
  testList.add("abc6@kakao.com")
  testList.add("abc7@naver.com")
  testList.add("naver@google.com")
  
  // 네이버 이메일 주소의 개수 찾기 (2가지 방법)
  // 1) naver라는 텍스트가 포함되어 있는지 찾기 -> contains()
  // 2) @ 뒤에 naver라고 텍스트가 있고 그 다음에 .이 이어진 이메일이 몇개인지 찾기 -> split() : '@', '.'기준으로 쪼갬
  
  for (i in testList) {
      if(i.contains("@naver.")) {
          println(i)
      }
  }
  
  println()
  
  val emailList = ArrayList<String>()
  for (i in testList) {
      // println(i.split("@")[1].split(".")[0])
      emailList.add(i.split("@")[1].split(".")[0])
  }
  
  println(emailList) // [naver, google, daum, kakao, naver, kakao, naver, google]
  
  var count = 0
  for (i in emailList) {
      if (i == "naver") {
          count++
      }
  }
  
  println(count)
}