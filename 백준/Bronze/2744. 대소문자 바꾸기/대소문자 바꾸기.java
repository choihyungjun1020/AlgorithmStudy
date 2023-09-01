import java.util.Scanner;

public class Main {
    // BOJ 2744번 대소문자 바꾸기
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String problem = sc.nextLine();
        String answer = "";

        for (int i = 0; i < problem.length(); i++) {
            if (90 < problem.charAt(i)) {
                char a = (char) (problem.charAt(i)-32);
                answer = answer + a;
                continue;
            }
            else {
                char a = (char) (problem.charAt(i)+32);
                answer = answer + a;
            }
        }

        System.out.println(answer);
    }
}
