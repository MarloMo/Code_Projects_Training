class City {

  // attribute
  int population;

// we'll explain 'public' later
public:
  // method
  void add_resident() {
    population++;
  }
};

////////////////////////////////////////////////////////////

// In city.hpp
class City {
  int population;

public:
  int get_population();
};


// In city.cpp
#include "city.hpp"

int City::get_population() {
  return population;
}
