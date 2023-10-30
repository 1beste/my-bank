
import java.util.Scanner;

public class ATM {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        String ops = "1- Your Balance:\n" + "2- Withdraw Money:\n" + "3- Deposit Money:\n" + "4- Quit.\n";
        System.out.println(ops);

        int balance = 1000;

        while (true) {

            System.out.print("Select an operation: ");
            int chosen = input.nextInt();

            if (chosen == 4) {
                System.out.println("Quitting.");
                break;
            } else if (chosen == 1) {
                System.out.println("Your balance is:" + balance);

            } else if (chosen == 2) {
                System.out.print("Type the amount you want to withdraw: ");
                int withdrawn = input.nextInt();
                if (balance - withdrawn < 0) {
                    System.out.println("Insufficient funds. Your balance is: " + balance);
                } else {
                    balance -= withdrawn;
                    System.out.println("Your new balance is: " + balance);
                }

            } else if (chosen == 3) {
                System.out.print("Type the amount you want to deposit: ");
                int deposited = input.nextInt();
                balance += deposited;
                System.out.println("Your new balance is: " + balance);
            } else {
                System.out.println("Invalid operation.");
                break;
            }
        }

    }
}
