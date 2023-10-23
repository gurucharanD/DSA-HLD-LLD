
// Deque Allows us to insert and delete from both ends
import java.util.*;

public class ArrayDequeDemo {
    public static void main(String[] args) {
        ArrayDeque<Integer> adq = new ArrayDeque<>();

        // insert at the end
        adq.offerLast(10);
        adq.offerLast(20);
        adq.offerLast(30);
        adq.offerLast(40);
        adq.forEach((x) -> {
            System.out.print(x);
        });
        System.out.println("");
        // insert at the front
        adq.offerFirst(1);
        adq.offerFirst(2);
        adq.forEach((x) -> {
            System.out.print(x);
        });
        System.out.println("");
        System.out.println(adq.poll());
        System.out.println(adq.pollFirst());
    }
}
