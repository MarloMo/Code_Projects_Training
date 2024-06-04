#include <iostream>
using namespace std;

int main() {
  int purchaseAmount = 0;
  double totalPrice;

  // your code goes here

  for (int i = 0; i < 3; i++) {
    cin >> totalPrice;
    totalPrice *= 0.15;
    cout << "the relevant discount is: $" << totalPrice << "\n";
  }

  return 0;
}