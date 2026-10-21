#!/usr/bin/env python3
# Created By: Bryson
# Date: 10 21, 2026
# This program gets a number from the user and tells the user
# if it is positive, negative or 0
def main():

    # Get number from the user
    number = float(input("Enter your number: "))

    # See if the guessed number is equal to the random number
    if number > 0:
        print("Your number is positive")
    elif number < 0:
        print("Your number is negative")
    elif number == 0:
        print("Your number is 0")
    else:
        print("Your number is not a valid number")


if __name__ == "__main__":
    main()
