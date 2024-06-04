#include <cstdlib>
#include <iostream>

int main() {

  srand(time(NULL));
  int bot = std::rand() % 3 + 1;

  int user;
  std::cout << "Choose option: \n";
  std::cout << "1) Rock \n 2) Paper \n 3) Scissors \n";
  std::cin >> user;

  // std::cout << bot;

  if (user == 1) {
    if (bot == 1) {
      std::cout << "bot = Rock \n Draw, try again \n";
    } else if (bot == 2) {
      std::cout << "bot = Paper \n You lose\n";
    } else if (bot == 3) {
      std::cout << "bot = Scissors \n You win \n";
    }
  } else if (user == 2) {
    if (bot == 1) {
      std::cout << "bot = Rock \n You win \n";
    } else if (bot == 2) {
      std::cout << "bot = Paper \n Draw, try again \n";
    } else if (bot == 3) {
      std::cout << "bot = Scissors \n You lose \n";
    }
  } else if (user == 3) {
    if (bot == 1) {
      std::cout << "bot = Rock \n You lose \n";
    } else if (bot == 2) {
      std::cout << "bot = Paper \n You win \n";
    } else if (bot == 3) {
      std::cout << "bot = Scissors \n Draw, Try again \n";
    }
  }

  return 0;
}