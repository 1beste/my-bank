
import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Please enter 2 numbers: ");
        double num1 = input.nextDouble();
        double num2 = input.nextDouble();

        System.out.println("Select your operation: ");
        System.out.println("1. Addition");
        System.out.println("2. Substraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        
        int calculation = input.nextInt();

        switch (calculation) {
            case 1:
                System.out.println("Sum of the numbers are: " + (num1 + num2));
                break; 
            case 2:
                System.out.println("Subtraction of the numbers are: " + (num1 - num2));
                break;
            case 3:
                System.out.println("Product of the numbers are: " + (num1 * num2));
                break;
            case 4:
                System.out.println("Division of the numbers are: " + (double) (num1 / num2));
                break;
            default:
                System.out.println("Invalid Calculation.");
                break;

        }

    }
}
