def fizzbuzz(number):
    value = ""
    if number % 15 == 0:
        value = ("FizzBuzz")
    elif number % 5 == 0:
        value = ("Buzz")
    elif number % 3 == 0:
       value = ("Fizz")
    else:
       value = number
    return value


def main():
    for i in range(1, 101):
        print(fizzbuzz(i))
    return

if __name__ == '__main__':
    main()
