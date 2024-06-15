def decode(file_path):
    # Open the file for reading
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines from the file

    print(lines)

    # Create a dictionary to store the number and corresponding word
    number_word_dict = {}
    for line in lines:
        parts = line.split()  # Split each line into parts
        number = int(parts[0])  # The first part is the number
        word = parts[1]  # The second part is the word
        number_word_dict[number] = word  # Store them in the dictionary
        
    print(number_word_dict)
    print(number_word_dict[3])

    # We need to find the words at the end of each pyramid line
    words_to_extract = []
    current_line = 1
    current_index = 1

    # Loop until there are no more numbers to process
    while current_index in number_word_dict:
        # Calculate the end index of the current line in the pyramid
        end_index = current_index + current_line - 1

        # Check if the end index is a valid key in our dictionary
        if end_index in number_word_dict:
            # If it is, add the corresponding word to our list
            words_to_extract.append(number_word_dict[end_index])
            # Move to the next line in the pyramid
            current_index = end_index + 1
            current_line += 1
        else:
            break  # If the end index is not valid, stop the loop

    # Join all the words we collected into a single string
    decoded_message = ' '.join(words_to_extract)
    return decoded_message


# Example usage:
file_path = 'file.txt'
decoded_message = decode(file_path)
print(decoded_message)
