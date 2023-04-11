package DesignPatterns.Decorator;

public class Mushrooms extends PizzaToppings {
    BasePizza bp;

    Mushrooms(BasePizza bp) {
        this.bp = bp;
    }

    @Override
    public int cost() {
        return this.bp.cost() + 200;
    }
}
