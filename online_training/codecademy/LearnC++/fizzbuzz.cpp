#include <iostream>

int main() {

  int i;

  for (i = 1; i < 101; i++) {

    if (i % 3 == 0 && i % 5 == 0) {
      std::cout << "FizzBuzz \n";
    } else if (i % 5 == 0) {
      std::cout << "Buzz \n";
    } else if (i % 3 == 0) {
      std::cout << "Fizz \n";
    } else {
      std::cout << i << "\n";
    }
  }

  return 0;
}
