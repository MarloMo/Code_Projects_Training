#include <fstream>
#include <iostream>
#include <stdexcept>

#include "read_file.cpp"
#include "read_file.hpp"

/// ERROR!!! FIX THIS PROGRAM!!!

int main() {

  try {
    readFile("example.txt");
  } catch (const std::exception &e) {
    std::cerr << "Error: " << e.what() << "\n";
  }

  return 0;
}