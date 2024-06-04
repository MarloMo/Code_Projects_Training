#include <iostream>

/// A void function, also known as a subroutine, has no return value, making it
/// ideally suited for situations where you just want to print stuff to the
/// terminal.
void oscar_wilde_quote() {

  std::cout << "The highest, as the lowest, for of criticism is a mode of "
               "autobiography. \n";
}

int main() {

  oscar_wilde_quote();

  return 0;
}
