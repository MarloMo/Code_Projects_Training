#include <iostream>
#include <vector>

int main() {

  std::vector<double> delivery_order;

  delivery_order.push_back(8.99);
  delivery_order.push_back(3.75);
  delivery_order.push_back(0.99);
  delivery_order.push_back(5.99);

  // Calculate the total using a for loop:

  double total = 0.0;

  for (int i = 0; i < delivery_order.size(); i++) {
    total += delivery_order[i];
  }

  /// Using Declarations for Members: You can bring
  /// specific members of a namespace into the current scope. For example:
  using std::cout;

  /// Now you can directly use cout and endl without prefixing them
  /// with std::.
  cout << "the total: \n" << total;

  return 0;
}
