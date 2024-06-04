#include <cmath>
#include <iostream>

long int findNextSquare(long int sq) {
  long int result;
  result = sqrt(sq);

  if (result * result == sq) {
    return sq + 2 * sqrt(sq) + 1;
  } else
    return -1;
}

int main() {
  std::cout << findNextSquare(14) << "\n";
  return 0;
}
