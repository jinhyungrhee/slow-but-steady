# Comparable과 Comparator

- `Comparable`과 `Comparator`는 모두 인터페이스(Interface)임
- 이들을 사용하기 위해서는 인터페이스 내에 선언된 메소드를 **반드시 구현**해주어야 함!
  - `Comparable` : compareTo(T o) 메소드 재정의(Override, 구현) 필요
  - `Comparator` : compare(T o1, T o2) 메소드 재정의(Override, 구현) 필요
- 용도 : **"객체를 비교할 수 있도록 만든다"**
- 예제) Student 클래스
  ```java
  public class Test {
    public static void main(String[] args) {
      Student a = new Student(17, 2);
      Student b = new Student(18, 1);

      // 어떤 것을 비교할 것인가? (나이? 학급?)
      // if (a > b) ?

    }
  }
  class Student {
    int age;          // 나이
    int classNumber;  // 학급

    Student(int age, int classNumber) {
      this.age = age;
      this.classNumber = classNumber;
    }
  }
  ```
  - 객체는 사용자가 기준을 정해주지 않는 이상 어떤 객체가 더 높은 우선순위를 갖는지 판단할 수 없음

## Comparable
- 구현 메소드 : compareTo(T o)
- **자기 자신과 매개변수 객체를 비교함**
- 값을 비교하여 정수값을 반환(리턴타입 : int)
- `lang패키지`에 존재하므로 import 해줄 필요가 없음
- 기본 사용 방법
  ```java
  public class ClassName implements Comparable<Type> {
    /*
    ...
    code
    ...
    */

    // 필수 구현 부분 -> 우리가 객체를 비교할 기준을 정의해주는 부분!
    @Override
    public int compareTo(Type o) {
      /*
      비교 구현
      */
    }
  }
  ```
- 예제) Student 클래스
  ```java
  class Student implements Comparable<Student> {
    int age;          // 나이
    int classNumber;  // 학급

    Student(int age, int classNumber) {
      this.age = age;
      this.classNumber = classNumber;
    }

    // 필수 구현
    @Override
    public int compareTo(Student o) {

      /*
      // 자기 자신의 age가 o의 age보다 크다면 '양수'
      if (this.age > o.age) {
        return 1;
      }
      // 자기 자신의 age와 o의 ager가 같다면 '0'
      else if (this.age == o.age) {
        return 0;
      }
      // 자기 자신의 age가 o의 age보다 작다면 '음수'
      else {
        return -1;
      }
      */

      // 간단하게 두 비교대상의 값의 차이를 반환해도 동일함!
      return this.age - o.age;
    }
  }
  ```
- ❗주의❗
  - 뺄셈 과정에서 자료형의 범위를 넘어버리는 경우가 발생할 수 있음
    - `int자료형`(4바이트 == 32비트): -2,147,483,648(-2^31) ~ 2,147,483,647(2^31 - 1)
    - `Underflow` : -2,147,483,648 - 1 = -2,147,483,649 (주어진 범위의 하한선을 넘어버리는 것)
    - `Overflow` : 2,147,483,647 + 1 = 2,147,483,648 (주어진 범위의 상한선을 넘어버리는 것)
    ```java
    public class Test {
      public static void main(String[] args) {
        int min = Integer.MIN_VALUE; // -2,147,483,648
        int max = Integer.MAX_VALUE; // 2,147,483,647

        System.out.println("min - 1 = " + (min - 1)); // 2147483647 (Underflow)
        System.out.println("max + 1 = " + (max + 1)); // -2147483468 (Overflow)
      }
    }
    ```
  - 따라서 `compareTo()` 메소드를 구현하거나 `compare()` 메소드를 구현할 때, 대소비교에 있어서 overflow와 underflow 발생 여지를 잘 체크해야 함!
  - 특히 primitive 값에 대해서 overflow, underflow 예외를 확인하기 어렵다면 `<, >, ==`으로 대소비교를 해주는 것이 안전함! (`권장되는 방식`)


## Comparator
- 구현 메소드 : compare(T o1, T o2)
- **객체 자체와는 상관없이 독립적인 두 매개변수 객체를 비교함**
- `util패키지`에 존재하므로 import 필요
- ❗주의❗
  - 뺄셈 과정에서 자료형의 범위를 넘어버리는 경우가 발생할 수 있음
- 기본 사용 방법
  ```java
  import java.util.Comparator;
  public class ClassName implements Comparator<Type> {
    /*
    ...
    code
    ...
    */

    // 필수 구현 부분 -> 우리가 객체를 비교할 기준을 정의해주는 부분!
    @Override
    public int compare(Type o1, Type o2) {
      /*
      비교 구현
      */
    }
  }
  ```
- 예제) Student 클래스
  ```java
  import java.util.Comparator;
  public class ClassName implements Comparator<Student> {
    int age;         // 나이
    int classNumber; // 학급

    Student(int age, int classNumber) {
      this.age = age;
      this.classNumber = classNumber;
    }

    @Override
    public int compare(Student o1, Student o2) {
      /*
      // o1의 학급이 o2의 학급보다 크다면 양수
      if(o1.classNumber > o2.classNumber) {
        return 1;
      } 
      // o1의 학급이 o2의 학급과 같다면 0
      else if(o1.classNumber == o2.classNumber) {
        return 0;
      }
      // o1의 학급이 o2의 학급보다 작다면 음수
      else {
        return -1;
      }
      */

      // 위 코드를 조금 더 간단히 나타내면
      return o1.classNumber - o2.classNumber;
    }
  }
  ```
- ⭐Comparator 기능만 사용하기(`익명 객체` 사용)⭐
  - `Comparator 인터페이스`가 구현(상속)할 대상이 됨 → **Comparator 인터페이스를 구현하는 익명 객체 생성**
    ```java
    import java.util.Comparator;

    public class Test {
      public static void main(String[] args) {
        
        // 익명 객체 구현방법1 : main 함수 안에 지역변수처럼 non-static으로 생성
        Comparator<Stduent> comp1 = new Comparator<Student>() {
          @Override
          public int compare(Student o1, Student o2) {
            return o1.classNumber - o2.classNumber;
          }
        };
      }

      // 익명 객체 구현방법2 : main 함수 밖에 정적(static) 타입으로 선언
      /*
      public static Comparator<Student> comp2 = new Comparator<Student>() {
        @Override
        public int compare(Student o1, Student o2) {
          return o1.classNumber - o2.classNumber;
        }
      }
      */
    }

    // 외부에서 익명 객체로 Comparator가 생성되기 때문에, Student 클래스 내부에서 Comparator을 구현(재정의)할 필요가 없어짐!
    class Student {

      int age;
      int classNumber;

      Student(int age, int classNumber) {
        this.age = age;
        this.classNumber = classNumber;
      }
    }
    ```
  - 익명 개체를 통해 여러가지 비교 기준 정의 가능 (장점)
    ```java
    import java.util.Comparator;

    public class Test {
      public static void main(String[] args) {

        Student a = new Student(17, 2);
        Student b = new Student(18, 1);
        Student c = new Student(15, 3);

        // '학급' 기준 익명 객체 통해 b와 c객체 비교
        int classBig = compClass.compare(b, c);
        if (classBig > 0) {
          System.out.println("b객체가 c객체보다 큽니다.");
        }
        else if(classBig == 0){
          System.out.println("b객체와 c객체의 크기가 같습니다.");
        }
        else {
          System.out.println("b객체가 c객체보다 작습니다.");
        }

        // '나이' 기준 익명 객체 통해 b와 c객체 비교
        int ageBig = compAge.compare(b, c);
        if (ageBig > 0) {
          System.out.println("b객체가 c객체보다 큽니다.");
        }
        else if(ageBig == 0){
          System.out.println("b객체와 c객체의 크기가 같습니다.");
        }
        else {
          System.out.println("b객체가 c객체보다 작습니다.");
        }
      }
      
      // '학급' 대소 비교 익명 객체
      public static Comparator<Student> compClass = new Comparator<Student>() {
        @Override
        public int compare(Student o1, Student o2) {
          return o1.classNumber - o2.classNumber;
        }
      };
      // '나이' 대소 비교 익명 객체
      public staic Comparator<Student> compAge = new Comparator<Student>() {
        @Override
        public int compare(Student o1, Student o2) {
          return o1.age - o2.age; 
        }
      };
    }

    class Student {
      int age;
      int classNumber;

      Student(int age, int classNumber) {
        this.age = age;
        this.classNumber = classNumber;
      }
    }
    ```

## Reference

- Stranger's lab 블로그 - [Comparable과 Comparator의 이해](https://st-lab.tistory.com/243)