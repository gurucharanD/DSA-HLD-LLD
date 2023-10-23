import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class TreeMapDemo {
    public static void main(String[] args) {
        TreeMap<Integer, String> tm = new TreeMap<>(Map.of(0, "a", 1, "b", 3, "c"));
        tm.put(4, "d");
        tm.put(5, "e");
        System.out.println(tm);
        System.out.println(tm.get(0));


        HashMap<Integer, String> hm = new HashMap<>(Map.of(0, "a", 1, "b", 3, "c"));
        hm.put(4, "d");
        hm.put(5, "e");
        System.out.println(hm);
        System.out.println(hm.get(0));
    }
}
