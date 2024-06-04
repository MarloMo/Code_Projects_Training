def reverse_sequence(n):
    result = []
    for i in range(n):
        result.append(n - i)
    return result


# n = 5

# myList = []
# for i in range(n):
#     myList.append(n - i)

# print(myList)

print(list(range(5, 0, -1)))
