import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] h = new int[9];
        for (int i = 0; i < 9; i++) {
            h[i] = scanner.nextInt();
        }

        Arrays.sort(h);

        int sum = Arrays.stream(h).sum();
        boolean find = false;
        for (int i = 0; i < 9; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (sum - h[i] - h[j] == 100) {
                    find = true;
                    h[i] = h[j] = -1;
                    break;
                }
            }
            if (find) {
                break;
            }
        }


        for (int i = 0; i < 9; i++) {
            if (h[i] > 0) {
                System.out.println(h[i]);
            }
        }
    }
}