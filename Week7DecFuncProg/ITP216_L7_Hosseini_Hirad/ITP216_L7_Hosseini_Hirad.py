# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# Lab 7
# Description:
# Describe what this program does in your own words such as:
'''
This program uses our newly learned concepts of generators and functional programming to output a series of strings and dictionaries.
'''

def validator_decorator(func):
    def wrapper(*args, **kwargs):
        all_good = True
        print("Testing arguments:")
        for arg in args:
            if type(arg) != str:
                print("\tArguments rejected: not all args are strings")
                all_good = False
        # if all_good:
        #     for kwarg in kwargs:
        #         if type(kwarg) != dict:
        #             print("\tArguments rejected: not all kwargs are dictionaries")
        #             all_good = False
        if all_good:
            for kwarg in kwargs.values():
                if len(kwarg) != 2:
                    print("\tArguments rejected: not all dictionaries have two k:v pairs")
                    all_good = False
        if all_good:
            print("\tArguments accepted: all args are strings, and all kwargs are dictionaries with two k:v pairs")
        print("Printing arguments:")
        for arg in args:
            print("\t", arg)
        print("Printing kwargs:")
        for key, value in kwargs.items():
            print("\t", str(key) + ":" + str(value))
        print("Running function:")
        func(*args, **kwargs)

    return wrapper

@validator_decorator
def print_all_the_things(*args, **kwargs):
    print("This will print all the things.")
    print("\t", end = '')
    for arg in args:
        print(arg, end = ' ')
    print()
    for kwarg in kwargs.values():
        if type(kwarg) == dict:
            for key, value in kwarg.items():
                print("\t", str(key) + ":" + str(value))

def main():
    print_all_the_things("Another", "lab", "involving", "animals", animal={'cat': True, 'dog': False})
    print_all_the_things("Another", "lab", "involving", 4, animal={'cat': True, 'dog': False})
    print_all_the_things("Another", "lab", "involving", "animals", animal={'cat': True, 'dog': False, 'hamster': 'never'})


if __name__ == "__main__":
    main()