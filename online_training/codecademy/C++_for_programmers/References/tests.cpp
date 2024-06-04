#include <iostream>

int reference_test(int &param1) {

  /*
  Remove the & to see how the variable num behaves.
  */

  param1 = 2;

  return param1;
}

int main() {

  int exam_score = 85;

  int &score = exam_score;

  score = 3;

  std::cout << score << "\n";

	/// Codecademy example ///
  int x = 1, y = 2;

  int &ex = x;

  /// This should output an unwanted result
  /// nothing happens (STILL WORKS FINE).
  int &eex = ex;

	eex = 152;

  std::cout << "x = " << x << "\n";
  std::cout << "y = " << y << "\n";
  std::cout << "ex = " << ex << "\n";
	std::cout << "memory address for ex = " << &ex << "\n";
	std::cout << "eex = " << eex << "\n";

  /// function tests ///

  int num = 6;

  std::cout << "num = " << num << "\n";
  std::cout << "function call result = " << reference_test(num) << "\n";
  std::cout << "num = " << num << "\n";

  return 0;
}