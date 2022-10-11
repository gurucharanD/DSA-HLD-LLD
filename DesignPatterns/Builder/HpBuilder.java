package DesignPatterns.Builder;

public class HpBuilder extends AbstractBuilder {

    HpBuilder() {
        super();
    }

    @Override
    void buildName() {
        // TODO Auto-generated method stub
        this.product.setName("HP");

    }

    @Override
    void buildKeyboard() {
        // TODO Auto-generated method stub
        this.product.setKeyboard("hp - keyboard");

    }

    @Override
    void buildMouse() {
        // TODO Auto-generated method stub
        this.product.setMouse("hpmouse");

    }

}
