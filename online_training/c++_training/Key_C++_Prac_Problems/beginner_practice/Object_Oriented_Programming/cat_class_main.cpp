#include <iostream>

#include "cat_class.hpp"

int main() {

  Cat House_Cat(20, "Neo", "Grey");

  std::cout << House_Cat.get_age() << "\n";
  House_Cat.get_call();

  return 0;
}