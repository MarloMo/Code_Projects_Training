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
        print("Error: The link does no exist, you entered: ", value_to_remove)
