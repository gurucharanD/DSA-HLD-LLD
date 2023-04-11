package DesignPatterns.Strategy;

public class OffRoadVehicle extends Vehicle {
    OffRoadVehicle() {
        super(new OffRoadVehicleStrategy());
    }
}
