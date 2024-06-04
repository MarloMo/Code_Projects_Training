#include <iostream>
#include <vector>

int main() {

  std::string phrase;

  std::cout
      << "Enter a phrase to that will be converted into whale language: \n";

  std::getline(std::cin, phrase);

  for (int i = 0; i < phrase.size(); i++) {

    if (phrase[i] == 'a') {
      std::cout << phrase[i];
    } else if (phrase[i] == 'e') {
      std::cout << phrase[i] << phrase[i];
    } else if (phrase[i] == 'i') {
      std::cout << phrase[i];
    } else if (phrase[i] == 'o') {
      std::cout << phrase[i];
    } else if (phrase[i] == 'u') {
      std::cout << phrase[i] << phrase[i];
    }
  }

  return 0;
}
