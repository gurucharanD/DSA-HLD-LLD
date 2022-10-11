package DesignPatterns.Builder;

abstract class AbstractBuilder {
    protected Product product;

    // whenever a new builder is created,
    // a new product is created along with it
    // hence we create a product object everytime
    // the builder object is created
    // the object is marked protected as it
    // should be accessible to its child classes

    AbstractBuilder() {
        this.product = new Product();
    }

    abstract void buildName();
    // {
    // this.product.buildName(name);
    // }

    abstract void buildKeyboard();
    // {
    // this.product.buildKeyboard(keyboard);
    // }

    abstract void buildMouse();

    public Product getProduct() {
        return this.product;
    }
    // {
    // this.product.buildMouse(mouse);
    // }

}
