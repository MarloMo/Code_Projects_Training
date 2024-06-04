#include <iostream>
#include <vector>

int main() {

  std::vector<int> vec = {2, 4, 3, 6, 1, 9};

  int sum = 0;
  int product = 1;

  for (int i = 0; i < vec.size(); i++) {

    if (vec[i] % 2 == 0) {
      sum += vec[i];
    } else {
      product *= vec[i];
    }
  }

  using std::cout;

  cout << "Sum of even numbers is " << sum << "\n";
  cout << "Product of odd numbers is " << product << "\n";

  return 0;
}
