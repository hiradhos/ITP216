# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# HW 4
# Description:
# Describe what this program does in your own words such as:
'''
This program is a very elementary emulation of an arcane-themed game (such as World of Warcraft) which utilizes newly learned
concepts underlying inheritance. There is a master class of Player which is inherited for two subclasses called Wizard and Barbarian.
The user can elect the character types and customize them before observing them in combat.
'''
import random
from ITP216_H4_Hosseini_Hirad_Barbarian import Barbarian
from ITP216_H4_Hosseini_Hirad_Wizard import Wizard

def main():
    print("Welcome to the game!")
    print("")
    #Collect all pertient information from the user regarding the two characters
    p1_char_type = input("Please enter Player 1's character type: (Wizard, Barbarian) ")
    print("")
    p1_char_name = input("Great! Please enter Player 1's character name: ")
    print("")
    p1_char_color = input("Awesome! Please enter Player 1's wardrobe color: ")
    print("")
    p1_char_health_points = int(input("Phenomenal! Please enter Player 1's max health points: (Between 5 and 10) "))
    print("")
    if p1_char_type.lower() == "barbarian": #if user elects barbarian, ask for rage points
        p1_char_rage_points = int(input("Yay! Please enter Player 1's max rage points: (Between 1 and 5) "))
        player_one = Barbarian(p1_char_name, p1_char_color, p1_char_health_points, p1_char_rage_points)
    else: #if user asks for wizard, ask for magic points
        p1_char_magic_points = int(input("Yay! Please enter Player 1's max magic points: (Between 1 and 5) "))
        player_one = Wizard(p1_char_name, p1_char_color, p1_char_health_points, p1_char_magic_points)
    print("")
    p2_char_type = input("Superb! Please enter Player 2's character type: (Wizard, Barbarian) ")
    print("")
    p2_char_name = input("Splendid! Please enter Player 2's character name: ")
    print("")
    p2_char_color = input("Awesome! Please enter Player 2's wardrobe color: ")
    print("")
    p2_char_health_points = int(input("Phenomenal! Please enter Player 2's max health points: (Between 5 and 10) "))
    print("")
    if p2_char_type.lower() == "barbarian":
        p2_char_rage_points = int(input("Yay! Please enter Player 2's max rage points: (Between 1 and 5) "))
        player_two = Barbarian(p2_char_name, p2_char_color, p2_char_health_points, p2_char_rage_points)
    else:
        p2_char_magic_points = int(input("Yay! Please enter Player 2's max magic points: (Between 1 and 5) "))
        player_two = Wizard(p2_char_name, p2_char_color, p2_char_health_points, p2_char_magic_points)
    print("")
    #Begin game by listing contenders
    print("Your contenders:")
    print("\t",end="")
    print(player_one.__str__())
    print("\t",end="")
    print(player_two.__str__())
    print("")
    round_counter = 1 #keeps track of round number
    while int(player_one.get_health_points()) > 0 and int(player_two.get_health_points()) > 0:
        #termiantes once any player's health decreases to 0 or below
        rand = random.randint(1, 100) #winner is decided randomly, with 40% win odds for each player and 20% odds of draw
        #when either player wins, the other's lose_fight() method triggers
        if rand < 41:
            winner = player_one
            loser = player_two
            player_two.lose_fight()
        elif rand < 61:
            print(f"Round {round_counter}:This round was a tie!")
            winner = "none"
        else:
            winner = player_two
            loser = player_one
            player_one.lose_fight()
        if winner != "none": #if there is a draw, skips this portion
            print(f"Round {round_counter}: {winner.get_name()} wins this round!")
            print(f"\t {loser.get_name()} has {loser.get_health_points()} health points.")
        #checks if either player won, and if so, announces the winner to console
        if int(player_one.get_health_points()) <= 0:
            print("There is a winner!")
            print(f"{player_two.get_name()} has {player_two.get_health_points()} health points.")
        elif int(player_two.get_health_points()) <= 0:
            print("There is a winner!")
            print(f"{player_one.get_name()} has {player_one.get_health_points()} health points.")
        round_counter += 1

if __name__ == "__main__":
    main()