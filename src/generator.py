import string
import random as rd
from checker import check




def password_generator(length: int, number: int):
    # Transform a string into a list & Remove the last 6 elements of the list
    l = list(string.printable)[:-6]

    for i in range(number):
        global password
        password = []
        password = [""] * length

        for j in range(length):
            password.append(l[rd.randint(0, len(l) - 1)])

        if check(''.join(password)):
            print(f"{i + 1}. {''.join(password)}")

    print(f"{i+1} valid password were generated")



