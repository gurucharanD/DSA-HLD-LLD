package DesignPatterns.Strategy;

public class Vehicle {

    DrivingStrategy ds;

    Vehicle(DrivingStrategy ds) {
        this.ds = ds;
    }

    public void drive() {
        this.ds.drive();
    }
}
