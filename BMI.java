
import java.util.Scanner;

public class BMI {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Weight: ");
        int w = input.nextInt();

        System.out.print("Height: ");
        double h = input.nextDouble();

        double result = w / (h * h);

        System.out.println("Result: " + result);

    }
}
