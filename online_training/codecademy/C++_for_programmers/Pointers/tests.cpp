#include <iostream>

/*
A pointer in C++ is a variable that stores a memory address as its value.

Pointers are similar to references in the sense that when the pointer’s value
changes, the value of the original variable will also change in the same way
*/

int main() {

  std::string day = "Monday";

  std::string *ptr = &day;

  *ptr = "Friday";

  /// Reference
  std::cout << "ptr = " << ptr << "\n";
  /// Dereference
  std::cout << "*ptr = " << *ptr << "\n";
  std::cout << "day = " << day << "\n";

  /*
  It is dangerous to leave a pointer variable uninitialized. If you are unsure
  where to point, assign that variable to nullptr, which is a keyword that
  provides a typesafe pointer value representing an empty pointer.
  */

  int *null_ptr = nullptr;

  /// Reference
  std::cout << "null_ptr = " << null_ptr << "\n";
  /// Dereference ---> segmentation fault
  // std::cout << "*null_ptr = " << *null_ptr << "\n";

  return 0;
}