#include <iostream>
#include <vector>

std::vector<int> first_three_multiples(int num) {

  return {num, 2 * num, 3 * num};
}

int main() {

  for (int elements : first_three_multiples(7)) {
    std::cout << elements << "\n";
  }

  return 0;
}