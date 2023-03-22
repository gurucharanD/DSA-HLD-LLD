package DesignPatterns.Factory.Java;

public class Paypal extends Payment {

    @Override
    void pay() {
        System.out.println("this is a paypal payment");
    }

}
