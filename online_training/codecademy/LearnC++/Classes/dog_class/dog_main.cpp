#include <iostream>

#include "dog.hpp"

int main() {

  Dog yorkie("Mia", 11, "Yorkie");

  std::cout << "My dogs name is " << yorkie.get_name() << ". \n";
  std::cout << "She is a " << yorkie.get_breed() << ". \n";
  std::cout << "She is " << yorkie.get_age() << " years old \n";

  return 0;
}
