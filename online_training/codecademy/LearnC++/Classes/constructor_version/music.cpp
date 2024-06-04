#include "song.hpp"
#include <iostream>

int main() {

  /// Instantiation (Object) for the Ep back_to_black:
  Song back_to_black("Back to Black", "Amy Winehouse");

  std::cout << back_to_black.get_title() << "\n";
  std::cout << back_to_black.get_artist();
}
