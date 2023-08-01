package DesignPatterns.Observer;

class DeliveryDriver implements OrderStatusObserver {
    private String name;

    public DeliveryDriver(String name) {
        this.name = name;
    }

    public void update(String status) {
        System.out.println("Delivery person " + name + " received order status update: " + status);
    }
}
