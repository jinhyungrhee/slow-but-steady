import java.util.*;

class Main{
  
  public static void main(String[] args) {

    int[] arr = {7, 5};
    
    // 스와프
    int temp = arr[0];
    arr[0] = arr[1];
    arr[1] = temp;

    System.out.println(arr[0] + " " + arr[1]); // 5 7 
  }
}
