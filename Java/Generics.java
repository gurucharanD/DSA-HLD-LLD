
@SuppressWarnings("unchecked")
class Data<T> {
    
    T Data[] = (T[]) new Object[10];
    int length = 0;

    public void append(T val) {
        this.Data[length++] = val;
    }

    public void display() {
        for (int i = 0; i < this.length; i++) {
            System.out.println(this.Data[i]);
        }
    }
}

public class Generics {
    static <T> void show(T[] list){
        for (T t : list) {
            System.out.println(t);
        }
    }
    public static void main(String[] args) {
        show(new String[] { "abc", "def", "ghi" });
        show(new Integer[]{ 1, 2, 3, 4, 5 });
    }
}

