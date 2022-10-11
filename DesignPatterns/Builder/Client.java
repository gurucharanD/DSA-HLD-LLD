package DesignPatterns.Builder;

class Client {

    public static void main(String[] args) {
        DellBuilder dbd = new DellBuilder();
        HpBuilder hpbd = new HpBuilder();

        Director dir1 = new Director(dbd);
        Director dir2 = new Director(hpbd);

        Product prod1 = dir1.buildProduct();
        Product prod2 = dir2.buildProduct();

        prod1.showSpecs();
        prod2.showSpecs();
    }

}