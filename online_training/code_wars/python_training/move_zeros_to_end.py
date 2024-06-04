# Write an algorithm that takes an array and moves all of
# the zeros to the end, preserving the order of the other elements.


def move_zeros(lst):
    new_lst = []
    zeros = []
    for i in lst:
        if i == 0:
            zeros.append(i)
        else:
            new_lst.append(i)
    return new_lst + zeros


list = [1, 3, 0, 2, 0, 1, 6]

print(move_zeros(list))
