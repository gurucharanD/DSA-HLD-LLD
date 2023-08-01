package DesignPatterns.Observer;

public interface OrderStatusSubject {
    void registerObserver(OrderStatusObserver observer);

    void removeObserver(OrderStatusObserver observer);

    void notifyObservers();
}
