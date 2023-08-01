package DesignPatterns.Observer;

import java.util.ArrayList;
import java.util.List;

class Order implements OrderStatusSubject {
    private List<OrderStatusObserver> observers = new ArrayList<>();
    private String status;

    public void setStatus(String status) {
        this.status = status;
        notifyObservers();
    }

    public void registerObserver(OrderStatusObserver observer) {
        observers.add(observer);
    }

    public void removeObserver(OrderStatusObserver observer) {
        observers.remove(observer);
    }

    public void notifyObservers() {
        for (OrderStatusObserver observer : observers) {
            observer.update(status);
        }
    }
}
