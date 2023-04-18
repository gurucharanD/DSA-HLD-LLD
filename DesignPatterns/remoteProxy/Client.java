package DesignPatterns.remoteProxy;

public class Client {
    public static void main(String[] args) {
        PaymentManagerInterface pm = new PaymentManagerProxy();
        pm.pay("guru", "charan", 200);
        pm.pay("vijay", "kiran", 300);
    }
}
