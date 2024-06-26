def dequeue(self):
    '''
        Allow us to remove a node from the head of the queue and return its value
        '''
    if not self.is_empty():

        item_to_remove = self.head
        print("Removing " + str(item_to_remove.get_value()) +
              " from the queue!")

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next_node()

        self.size -= 1

        return item_to_remove.get_value()

    else:
        print("This queue is totally empty!")
