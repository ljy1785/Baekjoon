import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] start = new int[n];
        int[] end = new int[n];
        for (int i = 0; i<n; i++){
            start[i] = sc.nextInt();
            end[i] = sc.nextInt();
        }

        int OFFSET = 100;
        int[] count = new int[2005];
        for(int i = 0; i<n; i++){
            int a = start[i] + OFFSET;
            int b = end[i] + OFFSET;

            for(int j = a; j<=b; j++){
                count[j]++;
            }
        }

        int maxVal = 0;
        for(int i = 0; i<count.length; i++){
            if(count[i] > maxVal){
                maxVal = count[i];
            }
        }
        System.out.println(maxVal);
    }
}