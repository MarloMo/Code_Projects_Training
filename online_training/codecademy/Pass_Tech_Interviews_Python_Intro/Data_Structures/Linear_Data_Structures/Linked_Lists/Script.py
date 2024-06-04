class Node:

    def __init__(self, value, link_node=None):

        self.value = value
        self.link_node = link_node

    ### Methods to access the value data and link (getter methods)
    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    # Define set_link_node method:
    def set_link_node(self, link_node):
        self.link_node = link_node
        return self.link_node


yacko = Node("likes to yak")
dot = Node("enjoys spending time in movie lots")
wacko = Node("has a penchant for hoarding snacks")

### Link yacko (node1) to dot(node2)
yacko.set_link_node(dot)
dot.set_link_node(wacko)

### Use getter methods to get data
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print("dots_data = ", dots_data)
print("wackos_data = ", wackos_data)

### How can I get yackos value?

print("yackos_data =", yacko.value)

### How could you get from yacko to wacko‘s value?
yacko.set_link_node(wacko)
print("yackos_data(linked to wacko) =", yacko.get_link_node().get_value())
