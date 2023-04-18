package DesignPatterns.remoteProxy;

public class PaymentManagerProxy implements PaymentManagerInterface {

    PaymentManagerInterface rpm;

    PaymentManagerProxy() {
        this.rpm = new RemotePaymentManager();
        this.connect();
    }

    @Override
    public void connect() {
        this.rpm.connect();
    }

    @Override
    public void pay(String sender, String reciever, double amount) {
        this.rpm.pay(sender, reciever, amount);
    }

}
