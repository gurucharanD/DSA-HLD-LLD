package DesignPatterns.singleton;

public class Payment {
    public String id;
    public String sender;
    public String reciever;
    public int amount;

    Payment(String sender, String reciever, int amount) {
        this.amount = amount;
        this.sender = sender;
        this.reciever = reciever;
    }
}
