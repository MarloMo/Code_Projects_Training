print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

### Set up the Game ##
# num_disks = int(input("\nHow many disks do you want to play with?\n"))
num_disks = 3

while num_disks < 3:
    print("Please enter a number of disks greater than or equal to 3.")
    num_disks = int(input("\nHow many disks do you want to play with?\n"))

for i in range(num_disks, 0, -1):
    left_stack.push(i)
# print(left_stack.get_size(), middle_stack.get_size(), right_stack.get_size())

# Now that we created our initial stacks and set up the disks, let’s
# calculate the number of optimal moves.
num_optimal_moves = 2**num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

### Get User Input ###
# Test function
get_input(stacks).is_empty()

### Play the Game ###
num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks..")

    for i in range(len(stacks)):
        stacks[i].print_items()

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input(stacks)

        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input(stacks)

        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)

            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print(
    f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}"
)
