import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();
        int index = 0;
        int count = 0;
        int molecule = 0;
        int fraction = 0;

        while (count < num) {
            index += 1;
            count += index;
        }
        count -= index;

        if (index % 2 == 0) {
            molecule = num - count;
            fraction = index - molecule + 1;
        }
        else {
            molecule = index - (num - count) + 1;
            fraction = num - count;
        }

        System.out.println(molecule + "/" + fraction);
    }
}