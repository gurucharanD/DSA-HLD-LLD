package DesignPatterns.Decorator;

public class Client {
    public static void main(String[] args) {
        BasePizza bp = new Mushrooms(new ExtraCheese(new Farmhouse()));
        System.out.println(bp.cost());
    }
}
