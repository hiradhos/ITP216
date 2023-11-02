# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# Assignment 2
# Description:
# Describe what this program does in your own words.
'''
This program takes in a variety of collections of different types (list, tuple, set) containing animal
types and names, and then organizes them into a main dictionary with keys being animal type and values being a list
of all animal names belonging to that type. This program also provides the user with a navigable menu containing
options such as viewing all animals in their collection and adding a new animal to the collection.
'''
def main():
    cats_names = ('Cassandra', 'Sir Whiskington', 'Truck')
    dogs_names = {'Barkey McBarkface', 'Leeloo Dallas', 'Taro'}
    parrots_names = ['Squawk', 'Squawk 2: the Squawkquel', 'Larry']

    #The names list below is indexed in concordance with the animal_types tuple
    names = ['peter', 'paul', 'mary']
    animal_types = ('cat', 'cat', 'hamster')

    main_dict = {} #Main dictionary containing animal type keys with animal name values

    #First, we populate a new dictionary with the concordant names and animal_types data
    i = 0 #counter variable for matching indices of names with animal_types
    for type in animal_types:
        if type not in main_dict: #adds new animal type key to dictionary with pet name list
            main_dict[type] = [names[i].title()]
        else: #adds new pet name to existing animal type key
            main_dict[type].append(names[i].title())
        i += 1

    for name in cats_names: #Merges cats_names list with existing dictionary
        main_dict['cat'].append(name)

    for name in dogs_names: #Merges dogs_names list with existing dictionary
        if 'dog' not in main_dict.keys(): #creates dog key if not found
            main_dict['dog'] = [name]
        else: #appends dog name if key is found
            main_dict['dog'].append(name)

    for name in parrots_names: #Merges parrots_names list with existing dictionary
        if 'parrot' not in main_dict.keys(): #creates parrot key if not found
            main_dict['parrot'] = [name]
        else: #appends parrot name if key is found
            main_dict['parrot'].append(name)

    uname = input("Please enter your username: ").strip().title()
    print("Hi, " + uname + "!")

    def user_console(): #This function outputs a navigable user menu and allows for selection of which function to execute
        print("Please choose from the following options:")
        print("\t" + "1. See all your pets' names.")
        print("\t" + "2. Add a pet.")
        print("\t" + "3. Exit")
        user_option = input("What would you like to do? (1,2,3): ").strip()
        return user_option

    def add_animal(): #This function allows the user to add a new animal to their collection
        print("")
        type_input = input("What kind of animal is this? ").strip().lower()
        print("")
        name_input = input("What is the name of the " + type_input + "? ").strip().title()
        print("")
        if type_input in main_dict.keys(): #If type key already exists, add animal name
            main_dict[type_input].append(name_input)
        else: #If type key does not exist, add new key with sole animal name in a list
            main_dict[type_input] = [name_input]
        print("")
        print("Great! " + name_input + " the " + type_input + " is now added to your pets.")

    def animal_counter(): #This function counts the total number of animals in the user's collection and is outputted in Option 1
        count = 0
        for k,v in main_dict.items():
            for animal in v:
                count += 1
        return count


    option = user_console() #Invokes the navigable user menu and collects first input
    while option != '3': #This loop will persist as long as the user does not "Exit"
        if option == '1': #Prints animal count followed by list of all animal types and names in collection
            print("")
            animal_count = animal_counter()
            print("You have " + str(animal_count) + " pets.")
            for k, v in main_dict.items():
                print(k + ": ", end='')
                i = 1
                for name in v:
                    if i < len(v):
                        print(name, end=', ')
                    else:
                        print(name)
                    i += 1

            print("")
        elif option == '2': #Adds a new animal to user collection
            add_animal()
            print("")
        else: #Admonishes user to enter valid option
            print("")
            print("Invalid option. Please choose again...")
            print("")
        option = user_console()

    print("")
    print("Goodbye!") #Prints once user exits

if __name__ == '__main__':
    main()