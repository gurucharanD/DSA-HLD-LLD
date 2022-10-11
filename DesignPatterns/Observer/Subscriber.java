package DesignPatterns.Observer;

abstract public class Subscriber {

    Subscriber() {

    }

    abstract void update(String msg);

}

class User1 extends Subscriber {
    private int id;
    // private String msg;

    User1(int id) {
        super();
        this.id = id;
    }

    public void update(String msg) {
        System.out.println(this.id + "  recieved new msg " + msg);
        // this.msg = msg;
    }
}

class User2 extends Subscriber {
    private int id;
    // private String msg;

    User2(int id) {
        super();
        this.id = id;
    }

    public void update(String msg) {
        System.out.println(this.id + "  recieved new msg " + msg);
        // this.msg = msg;
    }
}

class User3 extends Subscriber {
    private int id;
    // private String msg;

    User3(int id) {
        super();
        this.id = id;
    }

    public void update(String msg) {
        System.out.println(this.id + "  recieved new msg " + msg);
        // this.msg = msg;
    }
}