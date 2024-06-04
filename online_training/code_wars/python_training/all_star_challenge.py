# Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.
def str_count(strng, letter):
    result = 0

    for i in strng.lower():
        if i == letter.lower():
            result += 1

    return result


print(str_count("Hello World", "h"))

# def check_function(word, letter):
#     result = 0
#     for i in range(len(word.lower())):
#         if word.lower()[i] == letter.lower():
#             result += 1

#     return result

# print(check_function('HHH', 'H'))

##x = 'Marloo'
##lower_case = x.lower()
##
##count = 0
##for i in range(len(lower_case)):
##    if x[i] == 'a':
##        count += 1
##    elif x[i] == 'b':
##        count += 1
##    else:
##        print('none')
##
##print(count)
