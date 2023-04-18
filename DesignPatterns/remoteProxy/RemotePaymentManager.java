package DesignPatterns.remoteProxy;

public class RemotePaymentManager implements PaymentManagerInterface {

    @Override
    public void connect() {
        System.out.println("connecting to remote payment manager service");
        System.out.println("_____________________");
    }

    @Override
    public void pay(String sender, String reciever, double amount) {
        System.out.println("processing payment from " + sender + " to " + reciever + "$" + amount);
        System.out.println("_____________________");
    }
    
}
