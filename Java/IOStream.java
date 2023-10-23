import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class IOStream {
    public static void main(String[] args) {
        try {

            FileOutputStream fos = new FileOutputStream("./java/text.txt", false);
            Scanner sc = new Scanner(System.in);
            System.out.println();
            System.out.println("enter some text");
            String str = sc.nextLine();
            fos.write(str.getBytes());
            fos.close();
            sc.close();

            FileInputStream fis = new FileInputStream("./java/text.txt");
            byte data[] = new byte[fis.available()];
            fis.read(data);
            String output = new String(data);
            System.out.println(output);
            fis.close();
    
        } catch (FileNotFoundException e) {
            System.out.println(e);
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}
