package DesignPatterns.Strategy;

public class SportsVehicle extends Vehicle {
    SportsVehicle() {
        super(new SportsVehicleStrategy());
    }
}
