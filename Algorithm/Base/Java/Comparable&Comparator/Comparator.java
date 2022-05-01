import java.util.Comparator;

public class Test {

  public static void main(String[] args) {

    Student a = new Student(17, 2); 
    Student b = new Student(18, 1);
    Student c = new Student(15, 3);

    // a객체와는 상관없이 b와 c객체를 비교
    int isBig = a.compare(b, c);
    System.out.println(a.getAge());
  }
}

class Student implements Comparator<Student> {
  int age;         // 나이
  int classNumber; // 학급

  Student(String age, int classNumber) {
    this.age = age;
    this.classNumber = classNumber;
  }

  @Override
  public int compare(Student o1, Student o2) {
    return o1.classNumber - o2.classNumber;
  }
  // getter setter
  public void getAge() {
    return this.age;
  } 
}

// reference : https://st-lab.tistory.com/243