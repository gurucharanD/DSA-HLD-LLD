package DesignPatterns.singleton;
import java.util.ArrayList;
import java.util.List;

class PaymentManager {
    private static PaymentManager instance = null;

    public List<Payment> payments = new ArrayList<Payment>();

    private PaymentManager() {
    }

    static PaymentManager getInstance() {
        if (instance == null) {
            // synchronized block
            // to allow only one thread to access
            // the instance creation at any point of time
            synchronized (PaymentManager.class) {
                if (instance == null) {
                    instance = new PaymentManager();
                }
            }
        }
        return instance;
    }

    public void process(String sender, String reciever, int amount) {
        this.payments.add(new Payment(sender, reciever, amount));
        System.out.println("paying $" + amount + " to " + reciever + " from " + sender);
    }

    public List<Payment> listPayments() {
        for (Payment payment : this.payments) {
            System.out.println(payment.toString());
        }
        return this.payments;
    }
}
