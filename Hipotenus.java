
import java.util.Scanner;

public class Hipotenus {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Side1: ");
        int side1 = input.nextInt();

        System.out.print("Side2: ");
        int side2 = input.nextInt();

        double hipotenus = Math.sqrt((side1 * side1) + (side2 * side2));
        System.out.println("Hipotenus: " + hipotenus);

    }
}
