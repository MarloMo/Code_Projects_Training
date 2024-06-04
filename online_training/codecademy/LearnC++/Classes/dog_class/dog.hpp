#include <iostream>
#include <string>

/// declarations / header file

class Dog {
private:
  std::string name;
  int age;
  std::string breed;

public:
  Dog(std::string new_name, int new_age, std::string new_breed);

  std::string get_name();
  int get_age();
  std::string get_breed();
};
