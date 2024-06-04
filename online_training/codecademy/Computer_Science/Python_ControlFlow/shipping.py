def ground_shipping(weight):

    result = 0

    if weight <= 2:
        result = weight * 1.5 + 20
    elif (weight > 2 and weight <= 6):
        result = weight * 3. + 20
    elif (weight > 6 and weight <= 10):
        result = weight * 4. + 20
    elif weight > 10:
        result = weight * 4.75 + 20

    return result


def drone_shipping(weight):

    result = 0

    if weight <= 2:
        result = weight * 4.5
    elif (weight > 2 and weight <= 6):
        result = weight * 9.
    elif (weight > 6 and weight <= 10):
        result = weight * 12.
    elif weight > 10:
        result = weight * 14.25

    return result


def premium_shipping(weight):
    return weight + 125.


print("------------------------")

weight_test_case_1 = 4.8  #lbs
print("Shipping weight:", weight_test_case_1, "lbs \n")
print("Ground shipping price: $", f"{ground_shipping(weight_test_case_1):.2f}")
print("Premium shipping price: $",
      f"{premium_shipping(weight_test_case_1):.2f}")
print("Drone shipping price: $", f"{drone_shipping(weight_test_case_1):.2f}")

print("------------------------")

weight_test_case_2 = 41.5  #lbs
print("\n Shipping weight:", weight_test_case_2, "lbs \n")
print("Ground shipping price: $", f"{ground_shipping(weight_test_case_2):.2f}")
print("Premium shipping price: $",
      f"{premium_shipping(weight_test_case_2):.2f}")
print("Drone shipping price: $", f"{drone_shipping(weight_test_case_2):.2f}")

print("------------------------")
