import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        char[][] map = new char[n][m];

        for (int i = 0; i < n; i++) {
            map[i] = sc.next().toCharArray();
        }

        // 1. 행과 열에 경비원이 있는지 확인
        boolean[] rowExist = new boolean[n];
        boolean[] colExist = new boolean[m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 'X') {
                    rowExist[i] = true;
                    colExist[j] = true;
                }
            }
        }

        // 2. 보호받지 못하는 행 / 열의 개수
        int rowNeedCount = n;
        int colNeedCount = m;

        for (int i = 0; i < n; i++) {
            if (rowExist[i]) rowNeedCount--;
        }
        for (int i = 0; i < m; i++) {
            if (colExist[i]) colNeedCount--;
        }

        // 3. 둘 중에 큰 값을 출력
        System.out.println(Math.max(rowNeedCount, colNeedCount));
    }
}