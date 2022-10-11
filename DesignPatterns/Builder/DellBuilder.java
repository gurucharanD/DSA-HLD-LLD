package DesignPatterns.Builder;

public class DellBuilder extends AbstractBuilder {

    @Override
    void buildName() {
        // TODO Auto-generated method stub
        this.product.setName("Dell");

    }

    @Override
    void buildKeyboard() {
        // TODO Auto-generated method stub
        this.product.setKeyboard("dell keyboard");

    }

    @Override
    void buildMouse() {
        // TODO Auto-generated method stub
        this.product.setMouse("dell mouse");

    }

}
