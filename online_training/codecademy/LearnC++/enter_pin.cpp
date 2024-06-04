#include <iostream>

int main() {

  int pin = 0;
  int tries = 1;

  std::cout << "BANK OF CODECADEMY\n";

  std::cout << "Enter your PIN: ";
  std::cin >> pin;

  //   tries++;

  while (pin != 1234 && tries < 3) {

    std::cout << "Enter your PIN: ";
    std::cin >> pin;
    tries++;

    if (tries == 3) {
      std::cout << "Too many trys, session terminated \n";
    }
  }

  if (pin == 1234) {

    std::cout << "PIN accepted!\n";
    std::cout << "You now have access.\n";
  }
}