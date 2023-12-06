import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long N = sc.nextLong();
        int B = sc.nextInt();

        String result = decimalToBase(N, B);
        System.out.println(result);
    }

    private static String decimalToBase(long n, int b) {
        StringBuilder sb = new StringBuilder();

        while (n > 0) {
            long remainder = n % b;
            char digit;
            if (remainder >= 10) {
                digit = (char) ('A' + (remainder - 10));
            } else {
                digit = (char) ('0' + remainder);
            }

            sb.insert(0, digit);
            n /= b;
        }

        return sb.toString();
    }
}