#include <iostream>

#include "profile.hpp"

int main() {

  std::string user_name;
  int user_age;
  std::string user_city;
  std::string user_country;
  std::string user_pronouns;

  std::cout << "Enter user name: \n";
  std::cin >> user_name;
  std::cout << "Enter age: \n";
  std::cin >> user_age;
  std::cout << "Enter city: \n";
  std::cin >> user_city;
  std::cout << "Enter country: \n";
  std::cin >> user_country;
  std::cout << "Enter pronouns: \n";
  std::cin >> user_pronouns;

  int view_profile_bool;

  std::cout << "View user profile? : \n"
            << "Click 0 for yes or click 1 for no. \n";
  std::cin >> view_profile_bool;

  Profile user(user_name, user_age, user_city, user_country, user_pronouns);

  /// Enter hobbies manually:
  user.add_hobby("Shooting");
  user.add_hobby("Music production");
  user.add_hobby("hiking");

  if (view_profile_bool == 0) {
    user.view_profile();
  }

  return 0;
}
