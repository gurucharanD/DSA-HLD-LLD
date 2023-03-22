// this is a Restaurant class, it defines
// the properties that a Restaurant should have
// all the properties are private and they should be
// set and get through setters and getters

package DesignPatterns.Builder;

import java.util.*;

public class Restaurant {
    private String name;
    private List<String> menu = new ArrayList<String>();
    private String owner;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public void setMenu(List<String> menu) {
        this.menu = menu;
    }

    public List<String> getMenu() {
        return this.menu;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public String getOwner() {
        return this.owner;
    }

    public void showSpecs() {
        System.out.println("_____");
        System.out.println("Restaurant name: " + this.name);
        System.out.println("Owner Name:" + this.owner);
        System.out.println("Menu: " + this.menu);
        System.out.println("_____");
    }

}