public class Test {
  public static void main(String[] args) {
    
  }
}

class Student implements Comparable<Student> {

  int age;          // 나이
  int classNumber;  // 학급

  Student(int age, int classNumber) {
    this.age = age;
    this.classNumber = classNumber;
  }

  @Override
  public int compareTo(Student o) {
    return this.age - o.age;
  }
  /*
  @Override
  public int compareTo(Student o) {
    return this.classNumber - o.classNumber;
  }
  */
}

// reference : https://st-lab.tistory.com/243