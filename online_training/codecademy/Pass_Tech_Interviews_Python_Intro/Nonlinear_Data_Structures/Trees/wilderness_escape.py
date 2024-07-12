from tree_class import TreeNode

# user_choice = input("What is your name? ")
user_choice = "Marlo"
print(user_choice)

print("Once upon a time...")

story_root = TreeNode(
    """
You are in a forest 
clearing. There is a path to the left. 
A bear emerges from the trees and roars! 
Do you:
1 ) Roar back!
2) Run to the 
left...
"""
)

print(story_root.value)
