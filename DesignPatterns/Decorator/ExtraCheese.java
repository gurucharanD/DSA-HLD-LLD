package DesignPatterns.Decorator;

public class ExtraCheese extends PizzaToppings {
    BasePizza bp;

    ExtraCheese(BasePizza bp) {
        this.bp = bp;
    }

    @Override
    public int cost() {
        return this.bp.cost() + 100;
    }
}
