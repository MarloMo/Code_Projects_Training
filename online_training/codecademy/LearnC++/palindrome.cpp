#include <algorithm>
#include <iostream>
#include <string>

bool is_palindrome(std::string text) {

  int n = text.length();

  for (int i = 0; i < n; i++) {
    if (text[i] != text[n - 1 - i]) {
      return false;
    }
  }

  return true;
}

int main() {
  /// print true/false insteal 1/0
  std::cout << std::boolalpha;

  std::cout << is_palindrome("tacocat") << "\n";
  std::cout << is_palindrome("hannah") << "\n";
  std::cout << is_palindrome("mewtwo") << "\n";
  std::cout << is_palindrome("racecar") << "\n";
  std::cout << is_palindrome("aardvark") << "\n";

  return 0;
}
