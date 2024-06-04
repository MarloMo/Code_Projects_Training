#include <iostream>

int main() {
  int n;
  std::cout << "insert number:";
  std::cin >> n;

  for (int i = n; i > 0; i--) {
    std::cout << i << "\n";
    if (i % 5 == 0) {
      std::cout << "Beep"
                << "\n";
    }
  }

  return 0;
}