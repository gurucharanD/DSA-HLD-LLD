package DesignPatterns.Observer;

class Customer implements OrderStatusObserver {
    private String name;

    public Customer(String name) {
        this.name = name;
    }

    public void update(String status) {
        System.out.println("Customer " + name + " received order status update: " + status);
        // Code to update the customer about the order status
    }
}
