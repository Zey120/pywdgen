import string
import random as rd


# r = string.ascii_lowercase + string.ascii_uppercase + string.digits


def password_generator(length: int, number: int):
    # Transform a string into a list & Remove the last 6 elements of the list
    l = list(string.printable)[:-6]

    for i in range(number):
        global password
        password = []
        password = [""] * length

        for j in range(length):
            password.append(l[rd.randint(0, len(l) - 1)])

        print(f"{i + 1}. {''.join(password)}")


password_generator(13, 100)
