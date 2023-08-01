package DesignPatterns.TemplateMethod;

abstract class OrderProcessor {
    public void processOrder() {
        System.out.println("_______________");
        this.cookItems();
        this.packItems();
        this.deliverItems();
        System.out.println("_______________");
    }

    abstract void cookItems();

    abstract void packItems();

    abstract void deliverItems();

}
