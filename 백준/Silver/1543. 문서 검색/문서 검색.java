import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String doc = sc.nextLine();
        String word = sc.nextLine();

        if (doc.contains(word) == false) {
            System.out.println(0);
            System.exit(0);
        } else {
            doc = doc.replace(word,"!");
        }

        int count = 0;

        for (int i = 0; i < doc.length(); i++){
            if (doc.charAt(i) == '!'){
                count++;
            }
        }

        System.out.println(count);
    }
}