def twice_as_old(fathers_age, sons_age):
    if 2 * sons_age > fathers_age:
        return 2 * sons_age - fathers_age
    else:
        return fathers_age - 2 * sons_age

print(twice_as_old(55,30))
