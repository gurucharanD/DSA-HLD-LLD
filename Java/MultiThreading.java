class Customer extends Thread {
    String name;
    int balance;
    ATM atm;

    Customer(String name, int balance, ATM atm) {
        this.name = name;
        this.balance = balance;
        this.atm = atm;
    }

    public void useAtm() {
        atm.checkBalance(this.name);
        atm.withdraw(this.name, this.balance);
    }

    public void run() {
        this.useAtm();
    }

}

class ATM {
    synchronized void checkBalance(String name) {
        System.out.println("person " + name + " is checking his balance");
        try {
            Thread.sleep(1000);
        } catch (Exception e) {
        }
        System.out.println(name+" balance checking done");
    }

    synchronized void withdraw(String name, int amount) {
        System.out.println("person " + name + " is withdrawing " + amount);
         try {
            Thread.sleep(1000);
        } catch (Exception e) {
        }
        System.out.println(name+" withdraw done");

    }
}

public class MultiThreading {
    public static void main(String[] args) {
        try {
            ATM atm = new ATM();
            Customer c1 = new Customer("guru", 100, atm);
            Customer c2 = new Customer("charan", 200, atm);
            c1.start();
            c2.start();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
