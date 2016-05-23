from datetime import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))

#hundred = 100 - age
#current_year = datetime.now().year
#tomb = current_year + hundred

#print("You'll be 100 years old in %d" % tomb)
tomb = ()


def years(age):
    hundred = 100 - age
    current_year = datetime.now().year
    tomb = current_year + hundred
    return tomb


def main():
    print("You'll be 100 years old in %d" % years(age))
    return

if __name__ == '__main__':
    main()
