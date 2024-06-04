#include <iostream>
#include <string>

class Accumlator {
public:
  static std::string accum(std::string s) {
    std::string result;
    for (int i = 0; i < s.length(); i++) {
      result += toupper(s[i]);
      for (int j = 0; j < i; j++) {
        result += s[i];
      }
      result += "-";
    }
    return result.substr(0, result.length() - 1);
  }
};

int main() {

  std::string s = "abcdef";

  std::cout << Accumlator::accum(s) << std::endl;

  return 0;
}
