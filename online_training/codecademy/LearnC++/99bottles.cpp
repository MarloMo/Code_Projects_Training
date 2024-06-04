#include <iostream>

int main() {

  int i;

  for (i = 99; i > 0; i--) {

    std::cout << i << " bottles of beer on the wall. \n";
    std::cout << "Take one down and pass it around \n";
    std::cout << i - 1 << " bottles of beer on the wall \n";
    std::cout << "\n";
  }

  return 0;
}
