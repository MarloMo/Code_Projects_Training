#include <iostream>

std::string needs_water(int days, bool is_succulent) {

  std::string result;

  if (is_succulent == false and days > 3) {
    result = "Time to water the plant. \n";
  } else if (is_succulent == true and days < 12) {
    result = "Don't water the plant! \n";
  } else if (is_succulent == true and days > 13) {
    result = "Go ahead and give the plant a little water. \n";
  } else {
    result = "Don't water the plant! \n";
  }

  return result;
}

int main() {

  std::cout << needs_water(10, false) << "\n";

  return 0;
}