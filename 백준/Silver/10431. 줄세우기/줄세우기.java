import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] students = new int[20];

        // 출력
        for (int i = 1; i < T + 1; i++) {
            sc.nextInt();
            for (int j = 0; j < students.length; j++) {
                students[j] = sc.nextInt();
            }

            System.out.println(i + " " + count(students));
        }
    }

    static int count(int[] students) {
        int count = 0;
        for (int i = 0; i < students.length; i++) {
            for (int j = 0; j < i; j++) {
                if (students[j] > students[i]) {
                    count++;
                }
            }
        }

        return count;
    }
}