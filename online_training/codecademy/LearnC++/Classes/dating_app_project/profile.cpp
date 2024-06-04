#include "profile.hpp"

Profile::Profile(std::string new_name, int new_age, std::string new_city,
                 std::string new_country, std::string new_pronouns)
    : name(new_name), age(new_age), city(new_city), country(new_country),
      pronouns(new_pronouns) {}

void Profile::view_profile() {

  std::cout << "USER PROFILE: \n";

  std::cout << "\n Name: " << name << "\n"
            << "Age: " << age << "\n"
            << "City: " << city << "\n"
            << "Country: " << country << "\n"
            << "Pronouns: " << pronouns << "\n";

  std::cout << "\n Hobbies include: \n";

  for (int i = 0; i < hobbies.size(); i++) {
    std::cout << "> " << hobbies[i] << "\n";
  }
}

void Profile::add_hobby(std::string new_hobby) { hobbies.push_back(new_hobby); }
