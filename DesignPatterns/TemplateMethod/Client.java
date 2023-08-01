package DesignPatterns.TemplateMethod;

class Client {
    public static void main(String[] args) {
        OrderProcessor pickup = new PickupOrderProcessor();
        OrderProcessor delivery = new DeliveryOrderProcessor();

        pickup.processOrder();
        delivery.processOrder();
    }
}