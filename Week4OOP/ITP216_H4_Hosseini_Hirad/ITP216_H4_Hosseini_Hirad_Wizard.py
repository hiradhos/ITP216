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
from ITP216_H4_Hosseini_Hirad_Player import Player

class Wizard(Player):
# Class Attributes
# All inherited class attributes, plus:
# 1. Wizard_count
# a. The number of Wizards created.
    Wizard_count = 0

# 1. __init__()
# a. Description: Constructs a new Wizard object.
# b. Parameters: 4
# i. name_param (String)
# ii. color_param (String)
# iii. health_points_param (int)
# iv. magic_points_param (int)
# c. Returns: 0
# d. Inherits from Player and extends functionality. Assigns parameters to instance attributes. Increases
# Wizard_count by 1.
    def __init__(self, name_param, color_param, health_points_param, magic_points_param: int):
        # Instance Attributes
        # All Inherited instance attributes, plus:
        # 1. self.magic_points
        # a. The numerical value of magical power (int)
        # Instance Methods
        # All inherited instance methods, plus:
        super().__init__(name_param, color_param, health_points_param) #super() allows for inheritance of Player __init__
        self.magic_points: int = magic_points_param
        Wizard.Wizard_count += 1

# 2. __str__()
# a. Description: retrieves data about the Wizard when printing.
# b. Parameters: 0
# c. Returns: 1
# i. Data about the Wizard, such as: "The gray battle mage wizard has 8 health
# points and 10 magic points." (String)
    def __str__(self):
        return(f"The {self.color} wizard named {self.name} has {self.health_points} health points and {self.magic_points} magic points.")

# 3. get_magic_points()
# a. Description: retrieves the Wizard’s number of magic_points
# b. Parameters: 0
# c. Returns: 1
# i. self.magic_points attribute (int)
    def get_magic_points(self):
        return self.magic_points

# 4. get_power()
# a. Description: retrieves the power of the Wizard
# b. Parameters: 0
# c. Returns: self.health_points + self.magic_points (int)
    def get_power(self):
        return self.health_points + self.magic_points

