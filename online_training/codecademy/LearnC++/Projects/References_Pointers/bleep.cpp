#include <iostream>

#include "functions.hpp"

int main() {

  std::string word = "broccolli";
  std::string text =
      "I sometimes eat broccoli. The interesting thing about broccoli is that "
      "there are four interesting things about broccoli. Number One. Nobody "
      "knows "
      "how to spell it. Number Two. No matter how long you boil it, it's "
      "always "
      "cold by the time it reaches your plate. Number Three. It's green. "
      "#broccoli";

  for (int i = 0; i < text.size(); i++) {
    for (int j = 0; j < word.size(); j++) {

      std::cout << text[i+j];

    }
  }
  

  return 0;
}
