import Blossom_Class as bc

blossom = bc.HashMap(3)

blossom.assign("Rose", "Love and Romance")
blossom.assign("Sunflower", "Happiness and Positivity")
blossom.assign("Cactus", "Photosynthesis")
blossom.assign("Black Rose", "Darkness")
blossom.assign("White Rose", "Hunger Games")

print(blossom.retrieve("Rose"))
print(blossom.retrieve("Daisy"))
print(blossom.retrieve("Black Rose"))

print(blossom.array_size)