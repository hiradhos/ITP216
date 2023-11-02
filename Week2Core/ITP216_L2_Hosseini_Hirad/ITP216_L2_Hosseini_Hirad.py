# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# Lab 2 (there is no lab 1)
# Description:
# Describe what this program does in your own words such as:
# This program prints out a given statement as a string, list, tuple and set. It also represents the statement in a dictionary and utilizes a counter function output all of the keys (chars)
# and their corresponding counts.

def main():
    # your code goes here
    # get user input
    user_input = input("Please enter an input to be converted: ")

    # print out string
    print("string: ", end=" ")
    for char in user_input:
        print(char, end=", ")

    print()

    # print out list
    user_list = list(user_input)
    print("list: ", end="")
    for char in user_list:
        print(char, end=", ")

    print()

    # print out tuple
    user_tuple = tuple(user_input)
    print("tuple: ", end="")
    for char in user_tuple:
        print(char, end=", ")

    print()

    # print out set
    user_set = set(user_input)
    print("set: ", end="")
    for char in user_set:
        print(char, end=", ")

    print()

    # create counter for dict and print out dict with counts
    print("dictionary:")
    user_dict = {}
    for char in user_input:
        if char not in user_dict:
            user_dict[char] = 1  # first time that we encounter given char
        else:
            user_dict[char] += 1  # increment counter for existing char
    for k, v in user_dict.items():
        print('\t' + k + ': ' + str(v))


'''

Alternate methods for counter:

def counter_slicker(input_str: str) -> dict:
    print('dictionary: ')
    user_dict = {}
    for char in input_str:
        user_dict[char] = user_dict.setdefault(char, 0) + 1
    return user_dict

from collections import Counter
def counter_slickest(input_str: str) -> dict:
    return Counter(input_str)

'''
if __name__ == '__main__':
    main()