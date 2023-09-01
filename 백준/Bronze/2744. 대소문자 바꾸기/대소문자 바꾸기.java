import java.util.Scanner;

public class Main {
    // BOJ 2744번 대소문자 바꾸기
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String problem = sc.nextLine();

        for (int i = 0; i < problem.length(); i++) {
            char a = problem.charAt(i);
            if (90 < problem.charAt(i)) {
                System.out.print((char) (a - 32));
            }
            else {
                System.out.print((char) (a + 32));
            }
        }
    }
}