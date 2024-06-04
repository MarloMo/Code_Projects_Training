#include "song.hpp"
#include <iostream>

int main() {

  /// To create (or instantiate) an object, we can do this:
  Song electric_relaxation;

  electric_relaxation.add_title("Electric Relaxation");

  std::cout << electric_relaxation.get_title();

  /// Will return an error because the attribute artist is not
  ///  public.
  //   electric_relaxation.artist = "A Tribe Called Quest";

  electric_relaxation.add_artist("A Tribe Called Quest");

  std::cout << electric_relaxation.get_artist();
}
