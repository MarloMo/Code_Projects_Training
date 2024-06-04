#include <iostream>

int tempc(int tempf) {
  int result = (tempf - 32) / 1.8;

  return result;
}

int main() {

  int tempf;

  std::cout << "What is the temperature in degrees F? \n";
  std::cin >> tempf;

  std::cout << "The temp is " << tempc(tempf) << " Degrees Celsius. \n";

  return 0;
}