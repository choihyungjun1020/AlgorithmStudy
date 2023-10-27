import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] currentTime = sc.nextLine().split(":");
        int currentHour = Integer.parseInt(currentTime[0]);
        int currentMin = Integer.parseInt(currentTime[1]);
        int currentSec = Integer.parseInt(currentTime[2]);
        int currentSecAmount = currentHour * 3600 + currentMin * 60 + currentSec;


        String[] dropTime = sc.nextLine().split(":");
        int dropHour = Integer.parseInt(dropTime[0]);
        int dropMin = Integer.parseInt(dropTime[1]);
        int dropSec = Integer.parseInt(dropTime[2]);
        int dropSecAmount = dropHour * 3600 + dropMin * 60 + dropSec;

        int needSecondAmount = dropSecAmount - currentSecAmount;
        if (needSecondAmount <= 0)
            needSecondAmount += 24 * 3600;

        int needHour = needSecondAmount / 3600;
        int needMin = (needSecondAmount % 3600) / 60;
        int needSec = (needSecondAmount % 60);

        System.out.printf("%02d:%02d:%02d", needHour, needMin, needSec);
    }
}
