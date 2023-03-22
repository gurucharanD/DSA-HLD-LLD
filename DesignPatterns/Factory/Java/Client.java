package DesignPatterns.Factory.Java;

import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        System.out.println("select payment type: card or paypal");
        Scanner sc = new Scanner(System.in);
        String type = sc.nextLine();
        Factory.getPaymentMethod(type);
        sc.close();
    }
}
