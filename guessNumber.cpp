#include <iostream>
#include <ctime>


using std::cout;

int main() {

    cout << "****** NUMBER GUESSING GAME ******\n";

    srand(time(0));
    int num = 1+ (rand() % 100);
    int guess;
    int tries = 0;

    do{
        cout << "Guess the number: ";
        std::cin >> guess;

        if(guess > num){
            cout << "Lower!\n\n";
            tries++;
        }
        else if(guess < num){
            cout << "Higher!\n\n";
            tries++;
        } else{
            cout << "You guessed the number! You are tried " << tries << " times.\n";
        }


    }while(guess != num);

    cout << "******************************\n";

    return 0;
}