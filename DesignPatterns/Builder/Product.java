// this is a Desktop product class, it defines
// the properties that a desktop should have
// all the properties are private and they should be
// set and get through setters and getters

package DesignPatterns.Builder;

public class Product {
    private String name;
    private String keyboard;
    private String mouse;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public void setKeyboard(String keyboard) {
        this.keyboard = keyboard;
    }

    public String getKeyboard() {
        return this.keyboard;
    }

    public void setMouse(String mouse) {
        this.mouse = mouse;
    }

    public String getMouse() {
        return this.mouse;
    }

    public void showSpecs() {
        System.out.println(this.name);
        System.out.println(this.keyboard);
        System.out.println(this.mouse);
    }
    
}