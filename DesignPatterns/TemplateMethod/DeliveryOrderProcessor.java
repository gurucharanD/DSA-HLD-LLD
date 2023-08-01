package DesignPatterns.TemplateMethod;

public class DeliveryOrderProcessor extends OrderProcessor {

    @Override
    void cookItems() {
        System.out.println("cooking items for delivery order");

    }

    @Override
    void packItems() {
        System.out.println("packing items for deliverys order");
    }

    @Override
    void deliverItems() {
        System.out.println("looking for a delivery driver nearby");
        System.out.println("delivery driver on the way");
        System.out.println("order pickedup");
        System.out.println("order delivered");

    }

}
