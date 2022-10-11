// publisher maintains a list of all the subscribers
// and when a message is recieved notifies the subscribers
// also has methods for subscribe and unsubscribe the subscribers

package DesignPatterns.Observer;

import java.util.ArrayList;
import java.util.List;

public class Publisher {
    List<Subscriber> subscribers = new ArrayList<Subscriber>();

    Publisher() {
    }

    public void subscribe(Subscriber subscriber) {
        this.subscribers.add(subscriber);
        System.out.println("new user" + subscriber + "is subscribed");
    }

    public void unsubscribe(Subscriber subscriber) {
        this.subscribers.remove(subscriber);
    }

    public void notify(String msg) {
        for (int i = 0; i < this.subscribers.size(); i++) {
            Subscriber sub = this.subscribers.get(i);
            sub.update(msg);
        }
    }
}
