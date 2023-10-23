import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class LinkedListDemoo {
    public static void main(String[] args) {
        LinkedList<Integer> al = new LinkedList<Integer>();
        ArrayList<Integer> al2 = new ArrayList<Integer>(List.of(1, 2, 3, 3));
        
        al.add(10);
        al.add(0, 5);
        al.addAll(2, al2);
        al.remove(2);
        al.set(0, 89);

        System.out.println(al);

        al.addFirst(200);
        al.addLast(300);

        System.out.println(al);
    }
}
