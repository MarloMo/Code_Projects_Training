import random as rnd


def magic_8(random_number):
    result = ""

    if random_number == 1:
        result = "Yes - definitely"
    elif random_number == 2:
        result = "It is decidedly so"
    elif random_number == 3:
        result = "Without a doubt"
    elif random_number == 4:
        result = "Reply hazy, try again"
    elif random_number == 5:
        result = "Ask again later"
    elif random_number == 6:
        result = "Better not tell you now"
    elif random_number == 7:
        result = "My sources say no"
    elif random_number == 8:
        result = "Outlook not so good"
    elif random_number == 9:
        result = "Very doubtful"
    else:
        result = "Error"

    return result


name = input("Enter username: ")
question = input("Enter question: ")

if question == "":
    print("Error: You must ask a question!")
elif name == "":
    print("Question: ", question)
else:
    print(name + " asks: ", question)

random_number = rnd.randint(1, 9)
# print(random_number)

if question != "":
    print("Magic 8-Ball's answer: ", magic_8(random_number))
