package DesignPatterns.Builder;

import java.util.List;

public class CloudKitchen extends AbstractBuilder {

    CloudKitchen() {
        super();
    }

    @Override
    void buildName(String name) {
        this.restaurant.setName(name);
    }

    @Override
    void buildMenu(List<String> items) {
       this.restaurant.setMenu(items);
    }

    @Override
    void buildOwner(String name) {
        this.restaurant.setOwner(name);
    }

}
