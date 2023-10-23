@FunctionalInterface
interface MyData {
    void display(String str);
}

public class Lambda {

    public void reverse(String str){
        StringBuffer sb = new StringBuffer(str);
        sb.reverse();
        System.out.println(sb);
    }

    public static void main(String[] args) {
        Lambda l = new Lambda();
        MyData ml = l::reverse;
        ml.display("guru");
    }
}
