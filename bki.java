
import java.util.Scanner;

public class bki {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Weight: ");
        int kilo = scanner.nextInt();

        System.out.print("Height: ");
        double boy = scanner.nextDouble();

        double sonuç = kilo / (boy * boy);

        System.out.println("Result: " + sonuç);

    }
}
