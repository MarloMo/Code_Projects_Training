#include <iostream>
#include <fstream>

#include "read_file.hpp"

void readFile(const std::string &fileName) {
  std::ifstream file(fileName);
  if (!file.is_open()) {
    throw std::runtime_error("Cannot open file");
  }

  // Read the file content
  std::string line;
  while (std::getline(file, line)) {
    std::cout << line << "\n";
  }
}