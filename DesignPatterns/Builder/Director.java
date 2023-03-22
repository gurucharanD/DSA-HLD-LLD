package DesignPatterns.Builder;

import java.util.List;

public class Director {
    private AbstractBuilder restaurantBuilder;

    Director(AbstractBuilder builder) {
        this.restaurantBuilder = builder;
    }

    public Restaurant buildRestaurant(List<String> items, String owner, String name) {
        this.restaurantBuilder.buildMenu(items);
        this.restaurantBuilder.buildName(name);
        this.restaurantBuilder.buildOwner(owner);
        return this.restaurantBuilder.getRestaurant();
    }
}