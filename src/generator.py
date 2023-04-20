import string
import random as rd
from checker import check
from eval import password_strength


def password_generator(length: int, number: int,
                       tocheck: bool = False, toeval: bool = False,
                       digit: bool = False, lowercase: bool = False,
                       uppercase: bool = False, symbol: bool = False):

    l = []

    if not (digit or lowercase or uppercase or symbol):
        l = list(string.printable)[:-6]

    if digit:
        l += string.digits

    if lowercase:
        l += string.ascii_lowercase

    if uppercase:
        l += string.ascii_uppercase

    if symbol:
        l += string.punctuation



    for i in range(number):
        global password
        password = []
        password = [""] * length

        for j in range(length):
            password.append(l[rd.randint(0, len(l) - 1)])

        if tocheck and toeval:
            if check(''.join(password)):
                print(f"{i + 1}. {''.join(password)} {password_strength(str(password))}/10")

        elif tocheck:
            if check(''.join(password)):
                print(f"{i + 1}. {''.join(password)} {password_strength(str(password))}/10")

        elif toeval:
            print(f"{i + 1}. {''.join(password)} {password_strength(str(password))}/10")

        else:
            print(f"{i + 1}. {''.join(password)}")

    print(f"{i + 1} valid password were generated")

