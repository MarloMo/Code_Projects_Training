#include <iostream>

int main() {

  /// Remainder of bus seats available quiz
  int bus_seats = 50;
  int num_peeps_station = 126;

  num_peeps_station %= bus_seats;
  num_peeps_station = bus_seats - num_peeps_station;
  std::cout << "Seats left over from the last peeps left at the station: "
            << num_peeps_station << "\n";

  return 0;
}