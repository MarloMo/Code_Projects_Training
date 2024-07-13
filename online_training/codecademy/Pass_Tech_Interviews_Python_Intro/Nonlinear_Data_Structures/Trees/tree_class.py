class TreeNode:

    def __init__(self, value):
        self.value = value  # story_piece
        self.children = []  # choices

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse(self):
        node_to_visit = self  # story_node

        while node_to_visit.children is not None:
            print(node_to_visit.value)

            # If there are no children, the story ends
            if not node_to_visit.children:
                print("No more choices. ")
                break

            try:
                # Get the user's choice and subtract 1 to match the list index
                user_input = int(input("Enter your choice: ")) - 1

                # Check if the choice is valid
                if user_input < 0 or user_input >= len(node_to_visit.children):
                    print("Invalid choice, try again!")
                    continue

                # Move to the chosen child node
                node_to_visit = node_to_visit.children[user_input]

            except ValueError:
                # Handle the case thwere the user input is not a number
                print("Invalid input, please enter a number.")
                continue
