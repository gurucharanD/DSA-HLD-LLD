import java.util.LinkedHashMap;

public class LinkedHashMapDemo {
    public static void main(String[] args) {
        LinkedHashMap<Integer, String> lhm = new LinkedHashMap<>(5,.75f,true);

        lhm.put(1, "A");
        lhm.put(2, "B");
        lhm.put(4, "D");
        lhm.put(5, "E");
        lhm.put(3, "C");

        lhm.forEach((k, v) -> {
            System.out.println(k+" "+v);
        });

        System.out.println(lhm.get(5));
        System.out.println(lhm.get(3));

        lhm.forEach((k, v) -> {
            System.out.println(k+" "+v);
        });
    }
}
