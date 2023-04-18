package DesignPatterns.remoteProxy;

interface PaymentManagerInterface {
    public void connect();

    public void pay(String sender, String reciever, double amount);
}