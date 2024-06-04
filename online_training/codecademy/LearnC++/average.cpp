#include <iostream>

double average(double num1, double num2) { return (num1 + num2) / 2; }

int main() {

  std::cout << average(42., 24.) << "\n";
  std::cout << average(1., 2.) << "\n";

  return 0;
}
