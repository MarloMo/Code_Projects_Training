class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(self.array_size)]
        self.size = 0

    def has_space(self):
        if self.array == None:
            return True
        else:
            return self.size < self.array_size

    def hash(self, key, count_collisions=0):
        # Encode the string to bytes
        key_bytes = key.encode()
        hash_code = sum(key_bytes)

        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        '''
        Define the Setter.
        '''
        array_index = self.compressor(self.hash(key))

        if self.has_space():

            # collision strategy:
            if self.array[array_index] == None:  # Check current index
                self.array[array_index] = [key, value]

                self.size += 1
                return

            elif key == self.array[array_index][0]:
                self.array[array_index] = [key, value]

                self.size += 1
                return

            else:
                # In the third case, we need to use our collision open addressing
                # strategy to find if our key is somewhere else (it may or may not be)
                # so we should recalculate the index of our array.
                number_collisions = 1

                while self.array[array_index][0] != key:
                    new_hash_code = self.hash(key, number_collisions)
                    new_array_index = self.compressor(new_hash_code)

                    if self.array[new_array_index] == None:
                        self.array[new_array_index] = [key, value]

                        self.size += 1
                        return
                    elif self.array[new_array_index][0] == key:
                        self.array[new_array_index] = [key, value]

                        self.size += 1
                        return
                    elif self.array[new_array_index][
                            1] and self.array[new_array_index][0] != key:
                        number_collisions += 1
        else:
            print("All out of space!")

    def retrieve(self, key):
        '''
        Define the Getter.
        '''
        array_index = self.compressor(self.hash(key))
        value = self.array[array_index]

        if value == None:
            return None
        elif key == value[0]:
            return value[1]
        else:
            retrieval_collisions = 1

            while value[0] != key and retrieval_collisions <= self.array_size:
                new_hash_code = self.hash(key, retrieval_collisions)
                new_array_index = self.compressor(new_hash_code)
                new_value = self.array[new_array_index]

                if new_value == None:
                    return None
                elif new_value[0] == key:
                    return new_value[1]
                else:
                    retrieval_collisions += 1

        return f"There is no value for the key \"{key}\" in the hash map!"
