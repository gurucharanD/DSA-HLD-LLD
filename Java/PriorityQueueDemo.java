// priority queue is implemented using heap
// heap is implemented using Binary tree
// we can't have null values in priority queue
// we can change the priority using a comparator

import java.util.*;

class MyComparator implements Comparator<Integer> {
    public int compare(Integer o1, Integer o2) {
        if (o1 < o2) {
            return 1;
        }
        if (o1 > o2) {
            return -1;
        }
        return 0;
    }
}
public class PriorityQueueDemo {
    public static void main(String[] args) {
        PriorityQueue<Integer> maxpq = new PriorityQueue<>(new MyComparator());
        maxpq.add(1);
        maxpq.add(2);
        maxpq.add(3);
        maxpq.add(4);
        maxpq.add(5);

        System.out.println(maxpq.peek());
        maxpq.poll();
        System.out.println(maxpq.peek());

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(1);
        pq.add(2);
        pq.add(3);
        pq.add(4);
        pq.add(5);

        System.out.println(pq.peek());
        pq.poll();
        System.out.println(pq.peek());
    }
}
