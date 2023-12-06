import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] cnt = new int[10001];
        for (int i = 0; i < n; i++) {
            int N = Integer.parseInt(br.readLine());
            cnt[N]++;
        }

        for (int i = 1; i <= 10000; i++) {
            while (cnt[i]-- > 0) {
                bw.write(i + "\n");
            }
        }
        bw.flush();
    }
}