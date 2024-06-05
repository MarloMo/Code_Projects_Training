#include <iostream>

class Cat {

private:
  int age;
  std::string name;
  std::string color;

public:
  Cat(int new_age, std::string new_name, std::string new_color);

  int get_age();
  std::string get_color();
  std::string get_name();
  void get_call();
};
