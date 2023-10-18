
import java.util.Scanner;

public class Bmi2 {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Please enter your weight: ");
        double weight = input.nextDouble();

        System.out.println("Please enter your height(m): ");
        double height = input.nextDouble();

        double result = weight / (height * height);

        if (result < 18.5) {
            System.out.println("Your result is: " + result + " and you're underweight.");
        } else if (result > 18.5 && result < 24.9) {
            System.out.println("Your result is: " + result + " and your weight is ideal.");

        } else if (result > 24.9 && result < 29.9) {
            System.out.println("Your result is: " + result + " and you're overweight.");

        } else {
            System.out.println("Your result is: " + result + " and you're obez.");
        }

    }
}
