import java.util.*;

class Student implements Comparable<Student> {
  
  private String name;
  private int score;

  public Student(String name, int score) {
    this.name = name;
    this.score = score;
  }

  public String getName() {
    return this.name;
  }
  public int getScore() {
    return this.score;
  }

  // 기준 : 점수가 낮은 순서
  @Override
  public int compareTo(Student other) {
    if(this.score < other.score) {
      return -1;
    }
    return 1;
  }
}

class Main{
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    List<Student> students = new ArrayList<>();

    for (int i = 0; i < n; i++) {
      String name = sc.next();
      int score = sc.nextInt();
      students.add(new Student(name, score));
    }

    // 지정된 기준으로 정렬
    Collections.sort(students);

    for (int i = 0; i < students.size(); i++) {
      System.out.print(students.get(i).getName() + " ");
    }
  }
}
