#include "song.hpp"

// add Song method definitions here:

std::string Song::get_title() { return title; }

std::string Song::get_artist() { return artist; }

/// Contructor function
Song::Song(std::string new_title, std::string new_artist)
    : title(new_title), artist(new_artist) {}
