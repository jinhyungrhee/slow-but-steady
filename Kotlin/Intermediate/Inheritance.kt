// 상속(Inheritance)

fun main() {
    
  //     Job1()
  //     Job2()
    Job3()
    Job4()
  }
  
  open class AllJobs() { // open : 상속 가능
      
      init {
          println("일을 합니다.")
      }
  }
  
  class Job3() : AllJobs() { // 상속받음
      init {
          println("마케팅을 합니다.")
      }
  }
  
  class Job4() : AllJobs() {
      init {
          println("근로를 합니다.")
      }
  }
  
  class Job1() {
      
      init {
          println("일을 합니다.")
          println("코딩을 합니다.")
      }
  }
  
  class Job2() {
      
      init {
          println("일을 합니다.")
          println("디자인을 합니다.")
      }
  }