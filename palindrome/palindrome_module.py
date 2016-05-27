def palindrome(str):
    string = input('Please enter a string to check: ')
    without_space = string.replace(' ','')
    reverse = without_space[::-1]
    if without_space == reverse:
        return("That's a palindrome!")
    else:
        return("That's not a palindrome!")


def main():
    print(palindrome(str))



if __name__ == '__main__':
    main()
