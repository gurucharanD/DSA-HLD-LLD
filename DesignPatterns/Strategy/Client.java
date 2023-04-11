package DesignPatterns.Strategy;

public class Client {
    public static void main(String[] args) {
        Vehicle sv = new SportsVehicle();
        sv.drive();

        Vehicle ofv = new OffRoadVehicle();
        ofv.drive();
    }
}
