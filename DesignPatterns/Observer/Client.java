package DesignPatterns.Observer;

public class Client {
    public static void main(String[] args) {
        Publisher pub = new Publisher();

        Subscriber user1 = new User1(1);
        Subscriber user2 = new User1(2);
        Subscriber user3 = new User1(3);

        pub.subscribe(user1);
        pub.subscribe(user2);
        pub.subscribe(user3);

        pub.notify("this is message 1");

        pub.unsubscribe(user2);
        pub.notify("this is message 2");

    }
}
