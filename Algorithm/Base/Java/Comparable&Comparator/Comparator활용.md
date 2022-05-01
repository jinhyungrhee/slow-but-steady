# Comparator 활용

## Comparator란?

- 구현 메소드 : compare(T o1, T o2)
- **객체 자체와는 상관없이 독립적인 두 매개변수 객체를 비교함**
- `util패키지`에 존재하므로 import 필요
- ❗주의❗
  - 뺄셈 과정에서 자료형의 범위를 넘어버리는 경우가 발생할 수 있음

## Comparator의 문제점

- Comparator를 통해 compare 메소드를 사용하려면 결국 compare 메소드를 활용하기 위한 객체가 필요함

- 예시1 : 메소드를 호출하기 위한 대상이 a이든, b이든, c이든 상관이 없음 (일관성이 떨어짐)
  ```java
  public class Test {
    public static void main(String[] args) {
      
      Student a = new Student(17, 2);
      Student b = new Student(18, 1);
      Student c = new Student(15, 3);

      int isBig = a.compare(a, b);

      int isBig2 = a.compare(b, c);

      int isBig3 = b.compare(a, c);
    }
  }

  // Student class 생략
  ```
- 예시2 : 비교만을 위한 Student 객체 하나 더 생성 (Student 클래스의 age와 classNumber 변수는 쓸모가 없음에도 생성됨)
  ```java
  public class Test {
    public static void main(String[] args) {

      Student a = new Student(17, 2);
      Student b = new Student(18, 1);
      Student c = new Student(15, 3); 
      // 비교만을 위한 객체 생성
      Student comp = new Student(0, 0);

      int isBig = comp.compare(a, b);

      int isBig2 = comp.compare(b, c);

      int isBig3 = comp.compare(a, c);

    }
  }
  // Student class 생략
  ```

➡ 즉, 우리가 원하는 것은 **Comparator 비교 기능만 따로 두고 싶은 것**임!

## Comparator 비교 기능만 따로 두기 : 익명 객체(클래스) 활용

- 익명 객체
  - 이름이 정의되지 않은 객체
  - 특정 구현 부분만 따로 사용하거나, 부분적으로 기능을 일시적으로 바꿔야 할 경우 사용 가능

- `객체를 구현한다는 것`의 의미
  - 변수를 선언하고, 메소드를 정의하며 하나의 클래스(객체)로 만드는 것 (일반적인 클래스 구현 방식)
  - Interface 클래스를 implements하여 interface의 메소드를 재정의하는 것
  - class를 상속(extends)하여 부모의 메소드, 필드를 사용 또는 재정의하는 것

- 예시
  ```java
  public class Anonymous {
    public static void main(String[] args) {

      // 익명 객체1 -> "Rectangle을 상속받은 하나의 새로운 class" (*새로운 class인데 이름이 정의되지 않음*)
      Rectangle a = new Rectangle() {
        
        @Override
        int get() {
          return width;
        }
      };

      System.out.println(a.get());
      System.out.println(anonymous1.get());
      System.out.println(anonymous2.get());
    }

    // 익명 객체2 -> "Rectangle을 상속받은 하나의 새로운 class" (*새로운 class인데 이름이 정의되지 않음*)
    static Rectangle anonymous2 = new Rectangle() {

      int depth = 30;

      @Override
      int get() {
        return width * height * depth;
      }
    };
  }

  class Rectangle {
    int width = 10;
    int height = 20;

    int get() {
      return height;
    }
  }
  ```
- 비교
  - 코드1 : Rectangle 클래스를 상속받아 ChildRectangle이라는 이름으로 정의된 자식 클래스
    ```java
    public class Anonymous {
      public static void main(String[] args) {

        Rectangle a = new Rectangle();
        ChildRectangle child = new ChildRectangle();

        System.out.println(a.get());     // 20
        System.our.println(child.get()); // 10 * 20 * 40
      }
    }

    class ChildRectangle extends Rectangle {

      int depth = 40; // 새로운 필드(변수) 생성

      @Override
      int get() {
        return width * height * depth; // get 메소드 재정의
      }
    }

    class Rectangle {
      int width = 10;
      int height = 20;

      int get() {
        return height;
      }
    }
    ```
  - 코드2 : 익명 객체를 사용한 코드
    ```java
    public class Anonymous {
      public static void main(String[] args) {

        Rectangle a = new Rectangle();
        // 익명 객체를 사용하여 새로운 클래스(익명 클래스) 생성
        Rectangle anonymous = new Rectangle() {
          int depth = 40;

          @Override
          int get() {
            return width * height * depth;
          }
        }

        System.out.println(a.get());     // 20
        System.our.println(child.get()); // 10 * 20 * 40
      }
    }

    class Rectangle {
      int width = 10;
      int height = 20;

      int get() {
        return height;
      }
    }
    ```
    - 이름이 정의되지 않기 때문에, 특정 타입이 존재하는 것이 아님 → 반드시 익명 객체의 경우 `상속할 대상`이 있어야 함!
    - '상속'은 class의 extends 뿐만 아니라 interface의 implements도 포함
  - 코드 3 : 인터페이스를 구현한 익명 객체 사용
    ```java
    public class Anonymous {
      public static void main(String[] args) {

        Rectangle a = new Rectangle();

        // 인터페이스를 구현한 익명 객체
        Shape anonymous = new Shape() {
          int depth = 40;

          @Override
          public int get() {
            return width * height * depth;
          }
        };

        //System.out.println(a.get()); // Shape 인터페이스를 구현한 Rectangle (구체 클래스)
        System.out.println(anonymous.get()); // Shape 인터페이스를 구현한 익명 객체(클래스)
     
      }
    }

    /*
    // Shape 인터페이스를 구현한 Rectangle 클래스
    class Rectangle implements Shape {
      int depth = 40;

      @Override
      public int get() {
        return width * height * depth;
      }
    }
    */

    interface Shape {
      int width = 10;
      int height = 20;

      int get();
    }
    ```

## Reference

- Stranger's lab 블로그 - [Comparable과 Comparator의 이해](https://st-lab.tistory.com/243)