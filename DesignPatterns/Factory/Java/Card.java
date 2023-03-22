package DesignPatterns.Factory.Java;

public class Card extends Payment {

    @Override
    void pay() {
        System.out.println("this is a card payment");
    }
}
