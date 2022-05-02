fun main() {

    // val -> 박스안에 값을 넣고, 값을 넣고 나서 테이프로 밀봉  
      val box1 = "test box1"
      val box2 = "test box2"
      println(box1)
      println(box2)
      
  //     box1 = "changed box1"
      println(box1)
      
      // var -> 박스 안에 값을 넣고, 테이프로 밀봉하지 않음
      var box3 = "test box3"
      println(box3)
      box3 = "changed box3"
      println(box3)
      
      println("123" + 4)
      println(123 + 4)
  }