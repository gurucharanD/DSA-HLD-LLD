package DesignPatterns.singleton;

public class Client {

    public static void method1() {
        Logger logger = Logger.getLoggerInstance();
        logger.print("hello");
        logger.print("hows it going");
    }

    public static void method2() {
        Logger logger = Logger.getLoggerInstance();
        logger.print("hello");
        logger.print("hows it going");
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
                method1();
            }
        });
        t2.run();
    }
}
