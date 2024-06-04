import numpy as np


def quadratic_formula(a, b, c):
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        result = "No real roots"
        return result
    else:
        result_pos = (-b + np.sqrt(discriminant)) / (2 * a)
        result_neg = (-b - np.sqrt(discriminant)) / (2 * a)

    return result_pos, result_neg


solution = quadratic_formula(a=10, b=-1, c=3)
print("The real roots: ", solution)
