package DesignPatterns.TemplateMethod;

public class PickupOrderProcessor extends OrderProcessor {

    @Override
    void cookItems() {
        System.out.println("cooking items for pickup order");
    }

    @Override
    void packItems() {
        System.out.println("packing items for pickup order");
    }

    @Override
    void deliverItems() {
        System.out.println("order packed");
        System.out.println("order waiting at the restaurant for pickup by the user");
    }
}
