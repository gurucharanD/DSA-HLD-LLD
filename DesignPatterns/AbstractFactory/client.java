
package DesignPatterns.AbstractFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class client {

    public static void main(String[] args) throws IOException {
        // Enter data using BufferReader
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // Reading data using readLine
        String osType = reader.readLine();
        // Printing the read line
        System.out.println(osType);

        Factory factory = AbstractFactory.createFactory(osType);
        TextBox box = factory.createTextBox();
        box.printText();
        Button button = factory.createButton();
        button.press();
    }
}
