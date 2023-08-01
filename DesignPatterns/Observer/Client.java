package DesignPatterns.Observer;

public class Client {
    public static void main(String[] args) {
        Order order = new Order();

      DeliveryDriver deliveryPerson = new DeliveryDriver("guru");
      Customer customer = new Customer("charan");

    order.registerObserver(deliveryPerson);
    order.registerObserver(customer);

    order.setStatus("Preparing");
    order.setStatus("Packaging");
    order.setStatus("Out for delivery");
    order.setStatus("Delivered");

    order.removeObserver(deliveryPerson);
    order.setStatus("Cancelled");
}
}