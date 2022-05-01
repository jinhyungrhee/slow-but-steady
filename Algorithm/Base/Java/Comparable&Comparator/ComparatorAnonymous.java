import java.util.Comparator;

public class Test {
  public static void main(String[] args) {

    Student a = new Student(17, 2);
    Student b = new Student(18, 1);
    Student c = new Student(15, 3);

    // comp 익명 객체를 사용해 b와 c객체 비교
    int isBig = comp.compare(b, c);

    if(isBig > 0) {
      System.out.println("b객체가 c객체보다 큽니다.");
    }
    else if(isBig == 0) {
      System.out.println("두 객체의 크기가 같습니다.");
    }
    else {
      System.out.println("b객체가 c객체보다 작습니다.");
    }
  }

  // 방법2 : main 함수 밖에 정적(static) 타입으로 선언
  public static Comparator<Student> comp = new Comparator<Student>() {
    @Override
    public int compare(Student o1, Student o2) {
      return o1.classNumber - o2.classNumber;
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

// reference : https://st-lab.tistory.com/243