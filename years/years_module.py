from datetime import datetime


def years(age, name):
    hundred = 100 - age
    current_year = datetime.now().year
    final = hundred + current_year
    return ('%s, you will be 100 years old in %d' % (name, final))


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(years(age, name))
    return

if __name__ == '__main__':
    main()
