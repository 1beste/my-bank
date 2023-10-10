
import java.util.Scanner;

public class Taxi {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Please enter your travel distance: ");
        int distance = input.nextInt();

        System.out.print("Please write the amount per kilometer: ");
        double amount = input.nextDouble();

        double total = distance * amount;
        int opening = 15;

        System.out.println("Total: " + total + opening);

    }

}
