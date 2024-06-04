#include <iostream>

void name_x_times(std::string name, int x) {

  while (x > 0) {
    std::cout << name << "\n";
    x -= 1;
  }
}

int main() {

  std::string name = "Marlo";
  int some_number = 5;

  name_x_times(name, some_number);

  return 0;
}
