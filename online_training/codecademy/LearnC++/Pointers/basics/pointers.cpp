#include <iostream>

int main() {

  int power = 9000;

  /// Create pointer

  int *ptr = &power;

  /// Print ptr
  std::cout << "&power = " << &power << "\n";
  std::cout << "ptr = " << ptr << "\n";

  /// dereference: will show the actual value stored in memory.
  std::cout << "ptr = : " << *ptr << "\n";
}
