import java.util.*;

class Main{

  public static int sequentialSearch(int n, String target, String[] array){
    for (int i = 0; i < n; i++) {
      if (array[i].equals(target)) {
        return i + 1;
      }
    }
    return -1;
  }
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    System.out.println("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.");
    int n = sc.nextInt();
    String target = sc.next();
    System.out.println("앞서 적은 원소 개수만큼 문자여를 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다."); 
    String[] array = new String[n];
    for (int i = 0; i < n; i++) {
      array[i] = sc.next();
    }

    System.out.println(sequentialSearch(n, target, array));
    
    }
}