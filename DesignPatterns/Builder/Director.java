package DesignPatterns.Builder;

public class Director {
    private AbstractBuilder desktopBuilder;

    Director(AbstractBuilder builder) {
        this.desktopBuilder = builder;
    }

    public Product buildProduct() {
        this.desktopBuilder.buildName();
        this.desktopBuilder.buildKeyboard();
        this.desktopBuilder.buildMouse();
        return this.desktopBuilder.getProduct();
    }
}