import string
import random


def passwordgen(lenght):
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(lenght))


def main():
    print(passwordgen(8))
    return


if __name__ == '__main__':
    main()
