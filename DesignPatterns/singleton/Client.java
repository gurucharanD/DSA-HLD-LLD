package DesignPatterns.singleton;

public class Client {

    public static void method1() {
        PaymentManager payment = PaymentManager.getInstance();
        payment.process("john", "mike", 1000);
    }

    public static void method2() {
        PaymentManager payment = PaymentManager.getInstance();
        payment.process("guru", "charan", 100);
        payment.listPayments();

    }

    public static void main(String[] args) {
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                method1();
            }
        });
        t1.run();

        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                method2();
            }
        });
        t2.run();
    }
}
