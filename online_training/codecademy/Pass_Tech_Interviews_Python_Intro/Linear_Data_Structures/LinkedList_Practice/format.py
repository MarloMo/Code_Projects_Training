# TWO POINTERS MOVING IN PARALLEL
def list_nth_last_marlo(self):
    '''
        Marlo (try myself) version. 
        '''
    current_node = self.head_node

    while current_node:
        next_node = current_node.get_next_node()

        if next_node.get_next_node() == None:
            return str(current_node.get_value())
        else:
            current_node = next_node


def nth_last_node(self, n):
    '''
        Codecademy correct version!
        '''
    current_node = None
    tail_ptr = self.head_node
    count = 1
    while tail_ptr:
        tail_ptr = tail_ptr.get_next_node()
        count += 1
        if count >= n + 1:
            if current_node == None:
                current_node = self.head_node
            else:
                current_node = current_node.get_next_node()
    return current_node
