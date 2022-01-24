public class printSubsets {
    static void printSubsets(char[] arr, int n) {
        for (int i = 0; i < (1 << n); i++) { // (1 << 4) == 16
            System.out.print("{");
            // 각각의 원소가 있는지 확인해서 해당 문자값을 출력
            for (int j = 0; j < n; j++) {
                // j만큼 1을 왼쪽으로 shift + AND연산
                if((i & 1 << j) != 0) {
                    System.out.print(arr[j] + " ");
                }
            }
            System.out.print("}");
        }
    }


    public static void main(String[] args) {
        char[] data = {'A', 'B', 'C', 'D'};
        printSubsets(data, 4);
    }

}
