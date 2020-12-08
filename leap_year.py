#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program tells the user if the typed year is a leap year

import constants


def main():
    # this function can tell the user if the year is a leap year

    print("This program can check if the entered year is a leap year.")
    print("")

    # input
    year_string = input("Type in a year: ")
    print("")

    # process & output
    try:
        year_number = int(year_string)

        divisible_four = year_number % constants.LEAP_YEAR_FOUR
        divisible_hundred = year_number % constants.LEAP_YEAR_HUNDRED
        divisible_four_hundred = year_number % constants.LEAP_YEAR_FOUR_HUNDRED

        if divisible_four == 0:
            if divisible_hundred == 0:
                if divisible_four_hundred == 0:
                    print("{} is a leap year!".format(year_number))
                else:
                    print("{} is not a leap year".format(year_number))
            else:
                print("{} is a leap year!".format(year_number))
        else:
            print("{} is not a leap year".format(year_number))

    except Exception:
        print("This is not a number!")


if __name__ == "__main__":
    main()
