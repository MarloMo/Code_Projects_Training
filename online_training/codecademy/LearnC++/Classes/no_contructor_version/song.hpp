#include <string>

// add the Song class here:
class Song {

  /// Attributes or member variables
  std::string title;
  std::string artist;

public:
  void add_title(std::string new_title);
  void add_artist(std::string new_artist);

  std::string get_title();
  std::string get_artist();
};
