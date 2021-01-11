import random
import string


def generatePassword():

    characters = string.ascii_lowercase + \
        string.ascii_uppercase + string.digits + string.punctuation
    password = []

    for i in range(15):
        characterRandom = random.choice(characters)
        password.append(characterRandom)

    return "".join(password)


def main():
    print(generatePassword())


if __name__ == "__main__":
    main()
