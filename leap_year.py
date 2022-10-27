#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 26th, 2022
# This program asks the user for a year,
# then uses a try... catch statement to make
# sure the user input is actually an integer,
# then the program uses nested if... statements
# to check the remainder of the leap year when divided
# by 4, 100 and 400 respectively.
import math


# this function gets the user's year, checks
# to make sure the year is actually an integer, then
# checks to see if it is divisible by 4, 100 and 400
# by using % (the modulo operation).
def main():
    # getting the user's year.
    user_year = input(
        "Hello! Please give me a year, and I will tell you "
        "if it is a leap year or not! "
    )

    # initializing the user year as int variable to prevent
    # a run-time error in the "exceptions" part of the try...catch,
    # since this same issue happened for my assign-03.
    user_year_as_int = user_year

    # try...catch statement to make sure the user year is an int.
    try:
        user_year_as_int = int(user_year)
        if user_year_as_int % 4 == 0:
            if user_year_as_int % 100 == 0:
                if user_year_as_int % 400 == 0:
                    print("{} is a leap year!".format(user_year_as_int))
                else:
                    print("{} is NOT a leap year!".format(user_year_as_int))
            else:
                print("{} is a leap year!".format(user_year_as_int))
        else:
            print("{} is not a leap year!".format(user_year_as_int))
    except Exception:
        print("Sorry, this is not a valid year. Please only input an integer.")
    finally:
        print("")
        print("Thank you for using this program! I hope you found it helpful!")


if __name__ == "__main__":
    main()
