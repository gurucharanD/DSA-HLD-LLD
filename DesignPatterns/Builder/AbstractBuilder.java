package DesignPatterns.Builder;

import java.util.List;

abstract class AbstractBuilder {
    protected Restaurant restaurant;
    AbstractBuilder() {
        this.restaurant = new Restaurant();
    }

    abstract void buildName(String name);

    abstract void buildMenu(List<String> items);

    abstract void buildOwner(String name);

    public Restaurant getRestaurant() {
        return this.restaurant;
    }
}
