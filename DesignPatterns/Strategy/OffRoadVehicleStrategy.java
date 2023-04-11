package DesignPatterns.Strategy;

public class OffRoadVehicleStrategy implements DrivingStrategy {

    OffRoadVehicleStrategy() {

    }

    @Override
    public void drive() {
        System.out.println("this is a off road vehicle strategy");
    }

}
