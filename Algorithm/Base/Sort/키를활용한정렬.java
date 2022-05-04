import java.util.*;

class Fruit implements Comparable<Fruit> {
  
  private String name;
  private int score;

  public Fruit(String name, int score) {
    this.name = name;
    this.score = score;
  }

  public String getName() {
    return this.name;
  }

  public int getScore() {
    return this.score;
  }

  // 정렬 기준은 '점수가 낮은 순서'
  @Override
  public int compareTo(Fruit other) {
    if(this.score < other.score) {
      return -1; // default가 오름차순이므로 '음수'가 나오면 두 원소의 위치 바꾸지 않음
    }
    return 1; // '양수'가 나오면 두 원소의 위치 바꿈
  }
  
}

class Main{
  
  public static void main(String[] args) {

    List<Fruit> fruits = new ArrayList<>();

    fruits.add(new Fruit("바나나", 2));
    fruits.add(new Fruit("사과", 5));
    fruits.add(new Fruit("당근", 3));

    Collections.sort(fruits);

    for (int i = 0; i < fruits.size(); i++) {
      System.out.print("(" + fruits.get(i).getName() + "," + fruits.get(i).getScore() + ") ");
    }    
  }
}

// 출력 결과 : (바나나,2) (당근,3) (사과,5)