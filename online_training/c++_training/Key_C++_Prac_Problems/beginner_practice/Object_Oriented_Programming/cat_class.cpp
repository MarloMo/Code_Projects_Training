#include <iostream>

#include "cat_class.hpp"

Cat::Cat(int new_age, std::string new_name, std::string new_color)
    : age(new_age), name(new_name), color(new_color) {}

int Cat::get_age() { return age; }

std::string Cat::get_color() { return color; }

std::string Cat::get_name() { return name; }

void Cat::get_call() { std::cout << "Meow! \n"; }