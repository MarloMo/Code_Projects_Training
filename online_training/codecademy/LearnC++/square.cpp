#include <iostream>

int main() {

  int number = 0;

  while (number < 10) {
    std::cout << number << "    " << number * number << "\n";

    number++;
  }

  return 0;
}
