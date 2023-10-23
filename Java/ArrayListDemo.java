import java.util.*;

public class ArrayListDemo {
    public static void main(String[] args) {
        ArrayList<Integer> al = new ArrayList<Integer>();
        ArrayList<Integer> al2 = new ArrayList<Integer>(List.of(1, 2, 3,3));

        al.add(10);
        al.add(0, 5);
        al.addAll(2, al2);
        System.out.println(al);
        System.out.println(al.contains(50));
        System.out.println(al.indexOf(3));
        System.out.println(al.lastIndexOf(3));
        al.remove(2);
        System.out.println(al);
        al.set(0, 89);
        System.out.println(al);

        for (int i = 0; i < al.size(); i++) {
            System.out.println("index " + i + " " + al.get(i));
        }
        for (var i : al) {
            System.out.print(i);
        }
        al.forEach((x) -> {
            System.out.print(x);
        });

        Iterator<Integer> it = al.iterator();

        while (it.hasNext()) {
            System.out.print(it.next());
        }
    }
}
