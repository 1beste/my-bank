
import java.util.Scanner;

public class Switchin {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("First Number: ");
        int first;
        first = input.nextInt();

        System.out.print("Second Number: ");
        int second;
        second = input.nextInt();

        System.out.println("Before the changes your first and "
                + "second number is: " + first + " and " + second);

        int temporary = first;
        first = second;
        second = temporary;

        System.out.println("After the changes your first and "
                + "second number is: " + first + " and " + second);

    }
}
