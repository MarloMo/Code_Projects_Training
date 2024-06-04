#include <cmath>
#include <iostream>

long int findNextSquare(long int sq) {
  return sqrt(sq) * sqrt(sq) == sq ? sq + 2 * sqrt(sq) + 1 : -1;
}

int main() {
  std::cout << findNextSquare(4) << std::endl;
  return 0;
}