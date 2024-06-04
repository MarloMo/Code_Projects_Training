#include <cmath>
#include <iostream>

std::pair<double, double> quadratic_formula(int a, int b, int c) {

  double discriminant = b * b - 4 * a * c;

  if (discriminant < 0) {
    return std::make_pair(NAN, NAN);
  } else {
    double result_pos = (-b + sqrt(discriminant)) / (2 * a);
    double result_neg = (-b - sqrt(discriminant)) / (2 * a);
    return std::make_pair(result_pos, result_neg);
  }
}

int main() {

  int a, b, c;

  std::cout << "Enter a \n";
  std::cin >> a;
  std::cout << "Enter b \n";
  std::cin >> b;
  std::cout << "Enter c \n";
  std::cin >> c;

  std::pair<double, double> solutions = quadratic_formula(a, b, c);

  std::cout << "Roots = " << solutions.first << " and " << solutions.second;

  return 0;
}
