public class factorial {

    public static void main(String[] args) {
        int result;

        result = factorial(3);
        System.out.println(result);

    }

    static int factorial(int n) {
        // Base case
        if (n == 0) {
            return 1;
        }
        // Recursive case
        return n * factorial(n-1);
    }
}
