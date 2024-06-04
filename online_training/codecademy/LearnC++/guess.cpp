#include <iostream>

int main() {

  int guess;
  int tries = 1;

  std::cout << "Guess a number from 1-10 \n";
  std::cin >> guess;

  while (guess != 8 && tries < 3) {

    std::cout << "Guess again a number from 1-8 \n";
    std::cin >> guess;

    tries++;

    if (tries == 3) {
      std::cout << "You lose! \n";
    }
  }

  if (guess == 8) {
    std::cout << "You got it! \n";
  }

  return 0;
}