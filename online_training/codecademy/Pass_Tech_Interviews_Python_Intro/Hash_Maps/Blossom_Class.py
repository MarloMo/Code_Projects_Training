class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        """
        Allows you to update the link to the next node.
        """
        self.next_node = next_node
        return self.next_node


class LinkedList:

    def __init__(self, value=None):
        """
        Constructor
        """
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        """
        Insert a new head node
        Visual explanation:
        head_node -> NewNode -> Node1 -> Node2 -> Node3 -> None

        """
        new_node = Node(new_value)
        # Set the next node of the new node to the current head node
        # (Remember that Node has a .set_next_node()
        # class method you can use to set new_node‘s next_node.)
        new_node.set_next_node(self.head_node)
        # Update the head node of the linked list to the new node:
        self.head_node = new_node

    def stringify_list(self):
        """
        Return a string representation of a lists nodes values.

        Traverse the list, beginning at the head node, and collect
        each nodes value in a string.
        """
        string_list = ""
        current_node = self.head_node

        # Continue looping as long as current_node is not None
        while current_node:
            string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()

        return string_list

    def remove_node(self, value_to_remove):
        """
        Function that removes the first node that contains a particular
        value.
        """
        current_node = self.head_node

        if current_node and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            return
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node and next_node.get_value() == value_to_remove:
                    # If the next kid is the one to remove, you ask the current
                    #  kid to let go of the next kid's hand and instead hold
                    # hands with the kid after the next kid. This way, the kid
                    # you want to remove is no longer in the line.
                    current_node.set_next_node(next_node.get_next_node())
                    return
                else:
                    current_node = next_node

            print("Error: The link does no exist, you entered: ",
                  value_to_remove)

    def remove_mult_nodes(self, value_to_remove):
        """
        Method that removes nodes that contains a particular
        value.
        """
        current_node = self.head_node
        found = False

        if current_node and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            found = True

        while current_node:
            next_node = current_node.get_next_node()
            if next_node and next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                found = True
            else:
                current_node = next_node

        if not found:
            print("Error: The link does no exist, you entered: ",
                  value_to_remove)


class HashMap:

    def __init__(self, size):
        self.array_size = size
        # A list of LinkedList's Class
        self.array = [LinkedList()] * self.array_size
        self.size = 0

    def hash(self, key):

        key_bytes = key.encode()
        hash_code = sum(key_bytes)

        return hash_code

    def compressor(self, hash_code):

        return hash_code % self.array_size

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        list_at_index = self.array[array_index]

        current_node = list_at_index.get_head_node()
        while current_node:
            if current_node.get_value() != None and current_node.get_value(
            )[0] == key:
                return current_node.get_value()[1]

            current_node = current_node.get_next_node()

        return f"There is no value for the key \"{key}\" in the hash map!"

    def assign(self, key, value):

        if self.has_space():
            array_index = self.compressor(self.hash(key))
            list_at_array = self.array[array_index]

            current_node = list_at_array.get_head_node()
            while current_node:
                if current_node.get_value(
                ) != None and key == current_node.get_value()[0]:
                    current_node.get_value()[1] = value
                    return

                current_node = current_node.get_next_node()

            list_at_array.insert_beginning([key, value])
        else:
            print("All out of space!")

    def has_space(self):
        if self.array == None:
            return True
        else:
            return self.size < self.array_size