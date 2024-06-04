#include <iostream>
#include <string>

int getCount(std::string &inputStr) {
  int count = 0;
  for (int i = 0; i < inputStr.length(); i++) {
    if (inputStr[i] == 'a' || inputStr[i] == 'e' || inputStr[i] == 'i' ||
        inputStr[i] == 'o' || inputStr[i] == 'u') {
      count++;
    }
  }
  return count;
}

int main() {

  std::string str;
  str = "abracadabra";

  std::cout << "The number of vowels in the string is: " << getCount(str)
            << std::endl;

  return 0;
}
