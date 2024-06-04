#include <iostream>
#include <vector>

int positive_sum(std::vector<int> arr) {
  int result = 0;

  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] > 0) {
      result += arr[i];
    }
  }

  return result;
}

int main() {

  std::vector<int> v = {1, 2, -1, 3};

  std::cout << "sum = " << positive_sum(v) << "\n";

  return 0;
}
