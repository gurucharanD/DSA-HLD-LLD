package DesignPatterns.Builder;

import java.util.ArrayList;
import java.util.List;

class Client {

    public static void main(String[] args) {
        CasualDining cd = new CasualDining();
        CloudKitchen ck = new CloudKitchen();

        Director dir1 = new Director(cd);
        Director dir2 = new Director(ck);

        List<String> ckItems = new ArrayList<>();
        ckItems.add("pizza");
        ckItems.add("sandwich");
        ckItems.add("burger");

        List<String> cdItems = new ArrayList<>();
        cdItems.add("biryani");
        cdItems.add("chicken");
        cdItems.add("fish");

        Restaurant prod1 = dir1.buildRestaurant(ckItems, "Guru", "Native cloud kitchen");
        Restaurant prod2 = dir2.buildRestaurant(cdItems, "charan", "Internation casual dining");

        prod1.showSpecs();
        prod2.showSpecs();
    }

}