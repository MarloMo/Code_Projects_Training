#include <string>

// add the Song class here:
class Song {

  /// Attributes or member variables
  std::string title;
  std::string artist;

public:
  std::string get_title();
  std::string get_artist();

  // Add a constructor here:
  Song(std::string new_title, std::string new_artist);
};
