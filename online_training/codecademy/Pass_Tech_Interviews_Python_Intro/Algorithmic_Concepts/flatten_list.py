def flatten(my_list):
    result = []

    for i in my_list:
        if isinstance(i, list):
            print("List found!")

            flat_list = flatten(i)
            for j in flat_list:
                result.append(j)

    return result


### reserve for testing...
planets = [
    'mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus',
    ['neptune', 'pluto']
]

flatten(planets)
