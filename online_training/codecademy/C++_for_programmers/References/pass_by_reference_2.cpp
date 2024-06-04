#include <iostream>

int triple(int &i) {

  /*
  Remove the & to see how the variable num behaves.
  */

  i = i * 3;

  return i;
}

int main() {

  int num = 1;

  std::cout << num << "\n";
  std::cout << triple(num) << "\n";
  std::cout << num << "\n";
  std::cout << triple(num) << "\n";
}