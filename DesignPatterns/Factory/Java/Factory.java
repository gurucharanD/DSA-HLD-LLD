package DesignPatterns.Factory.Java;

public class Factory {
    static void getPaymentMethod(String type) {
        if (type.equals("card")) {
            new Card().pay();
        } else {
            new Paypal().pay();
        }
    }
}
