package DesignPatterns.Strategy;

public class SportsVehicleStrategy implements DrivingStrategy {

    public SportsVehicleStrategy() {
    }

    @Override
    public void drive() {
        System.out.println("this is a sports vehicle strategy");
    }

}
