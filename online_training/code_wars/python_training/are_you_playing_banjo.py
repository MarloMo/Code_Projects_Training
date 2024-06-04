def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0].lower(
    ) == "r" else name + " does not play banjo"


name = input("Enter your name: ")
print(are_you_playing_banjo(name))
