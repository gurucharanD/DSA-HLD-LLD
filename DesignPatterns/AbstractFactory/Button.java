package DesignPatterns.AbstractFactory;

interface Button {
    public void press();
}

class MacButton implements Button {
    public void press() {
        System.out.println("pressed mac button");
    }
}

class WinButton implements Button {
    public void press() {
        System.out.println("pressed win button");
    }
}