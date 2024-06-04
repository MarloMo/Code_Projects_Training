#include <iostream>

void swap_num(int &i, int &j) {

  int temp = i;
  i = j;
  j = temp;
}

void no_ref_swap_num(int i, int j) {

  int temp = i;
  i = j;
  j = temp;
}

int main() {

  int a = 100;
  int b = 200;
  int c = 100;
  int d = 200;

  swap_num(a, b);

  std::cout << "A is " << a << "\n";
  std::cout << "B is " << b << "\n";

  no_ref_swap_num(c, d);

  std::cout << "A is " << c << "\n";
  std::cout << "B is " << d << "\n";
}
