package DesignPatterns.AbstractFactory;

public class AbstractFactory {

    public static Factory createFactory(String osType) {
        if (osType == "mac") {
            System.out.println("IN mac");
            return new MacFactory();
        } else if (osType == "win") {
            System.out.println("IN win");

            return new WinFactory();
        } else {
            System.out.println("IN else");

            return new WinFactory();
        }
    }

}
