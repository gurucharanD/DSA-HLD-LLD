class MyData {
    int value;
    boolean flag = true;

    synchronized public void set(int v) {
        while (flag != true) {
            try {
                wait();
            } catch (Exception e) {
            }
        }
        value = v;
        flag = false;
        notify();
    }

    synchronized public int get() {
        int x = 0;
        while (flag != false) {
            try {
                wait();
            } catch (Exception e) {
            }
        }
        x = value;
        flag = true;
        notify();
        return x;
    }
}

class Producer extends Thread {
    MyData md;

    Producer(MyData md) {
        this.md = md;
    }

    public void run() {
        int count = 1;
        while (true) {
            this.md.set(count);
            System.out.println("Producer " + count);
            count += 1;
        }
    }
}

class Consumer extends Thread {
    MyData md;

    Consumer(MyData md) {
        this.md = md;
    }

    public void run() {
        int value;
        while (true) {
            value = this.md.get();
            System.out.println("consumer " + value);
        }
    }
}

public class ProducerConsumer {
    public static void main(String[] args) {
        MyData md = new MyData();
        Producer p = new Producer(md);
        Consumer c = new Consumer(md);
        p.start();
        c.start();
    }
}
