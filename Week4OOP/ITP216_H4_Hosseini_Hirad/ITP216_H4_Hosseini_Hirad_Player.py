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

'''
Class Player
See Lab 4 for requirements.
'''

import random

class Player(object): # Class Player
    # Class Attributes
    # 1. Player_count
    # a. The number of Players created.
    Player_count = 0

    # Instance Methods
    # 1. __init__()
    # a. Description: Constructs a new Player object
    # b. Parameters: 3
    # i. name_param (String)
    # ii. color_param (String)
    # iii. health_points_param (int)
    # c. Returns 0
    # d. Assigns parameters to instance attributes. Increases Player Player_count by 1.
    def __init__(self, name_param, color_param, health_points_param):
        # Instance Attributes
        # 1. self.name
        # a. The name of the Player (string)
        # 2. self.health_points
        # a. The number of health_points the Player has (int)
        # 3. self.color
        # a. The color of the Player’s clothes (String)
        self.name = name_param
        self.health_points = health_points_param
        self.color = color_param
        Player.Player_count += 1

    # 2. __str__()
    # a. Description: Returns a string representation of the Player object to be used to print out the Player for human
    # consumption.
    # b. Parameters: None
    # c. Returns a string representation of the Player object
    # d. Should show the current state / value of each attribute.
    def __str__(self):
        return ("Player named: " + self.name + " is wearing " + self.color
                + " colored clothes and has " + str(self.health_points)
                + " health points.")
    def __repr__(self):
        return ("Player { \n"
                + "\tName: " + self.name + "\n"
                + "\tHealth points: " + str(self.health_points) + "\n"
                + "\tColor: " + self.color + "\n")

    # 3. get_name()
    # a. Description: Retrieves Player name.
    # b. Parameters: 0
    # c. Returns: 1
    # i. self.name instance attribute
    def get_name(self):
      return self.name

    # 4. get_color()
    # a. Description: Retrieves Player color.
    # b. Parameters: 0
    # c. Returns: 1
    # i. self.color instance attribute
    def get_color(self):
        return self.color

    # 5. get_health_points()
    # a. Description: Retrieves Player health_points.
    # b. Parameters: 0
    # c. Returns: 1
    # i. self.health_points instance attribute
    def get_health_points(self):
        return self.health_points
    def set_health_points(self, new_health_points_value):
        if new_health_points_value > 0:
            self.health_points = new_health_points_value
        else:
            print("ERROR: Must specify a positive value!")

    # 6. set_color()
    # a. Description: Changes Player color.
    # b. Parameters: 1
    # i. A color (String)
    # c. Returns: 0
    def set_color(self, new_color_param):
        self.color = new_color_param

    # 7. lose_fight()
    # a. Description: Player potentially loses health_points.
    # b. Parameters: 0
    # c. Returns: 0
    # d. Based on the number of existing health_points, randomly generate a number and lose that number of
    # health_points. update self.health_points instance attribute.
    def lose_fight(self):
        self.health_points -= random.randint(1, self.health_points)
