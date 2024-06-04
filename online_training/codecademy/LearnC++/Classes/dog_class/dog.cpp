#include <iostream>

#include "dog.hpp"

/// definitions file

Dog::Dog(std::string new_name, int new_age, std::string new_breed)
    : name(new_name), age(new_age), breed(new_breed) {}

std::string Dog::get_name() { return name; }

int Dog::get_age() { return age; }

std::string Dog::get_breed() { return breed; }
