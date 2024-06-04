#include <iostream>

int triple_ref(int &i) {

  i = i * 3;
  
  return i;

}

int triple(int i) {

  i = i * 3;
  
  return i;

}

int main() {
  
  int num = 1;

  /// No reference on parameter
  std::cout << triple(num) << "\n";
  std::cout << triple(num) << "\n";
  
  /// Reference on parameter
  std::cout << triple_ref(num) << "\n";
  std::cout << triple_ref(num) << "\n";

}
