#include "fns.hpp"
#include "fns.cpp"

#include <iostream>

int main() {
  
  std::cout << is_palindrome("noon") << "\n";
  std::cout << tenth_power(4) << "\n";
  std::cout << average(4.0, 7.0) << "\n";

  return 0;
  
}
