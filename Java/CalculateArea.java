import java.lang.*;
import java.util.*;

public class CalculateArea {
    public static void main(String[] args) {
        // int[] arr = { 3, 4, 5, 6, 23, 545, 656, 56, 34, 6, 6, 565, 43534, 3 };
        int[] arr = { 1,2,3,4,5,6,7,8,9 };
        // int[] arr = { 9,8,7,6,5,4,3,2,1 };

        int max1 = Integer.MIN_VALUE;
        int max2 = Integer.MIN_VALUE;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > max1) {
                max2 = max1;
                max1 = arr[i];
            } else if (arr[i] > max2) {
                max2 = arr[i];
            }
        }
        System.out.println(max1);
        System.out.println(max2);

        StringTokenizer st = new StringTokenizer("sree,guru,charan",",", true);
        StringTokenizer st1 = new StringTokenizer("sree,guru,charan",",", false);

        while (st.hasMoreTokens()) {
            System.out.println(st.nextToken());
        }
        while (st1.hasMoreTokens()) {
            System.out.println(st1.nextToken());
        }
    }

}
