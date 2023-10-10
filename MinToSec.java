package week2;

import java.util.Scanner;

public class MinToSec {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Number: ");
        int seconds = input.nextInt();

        System.out.println(seconds + " second is " + (seconds / 60) + " minutes and " + (seconds % 60) + " seconds");

    }

}
