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

# Class Barbarian
# Inherits from Player class.
class Barbarian(Player):

# Class Attributes
# All inherited class attributes, plus:
# 1. Barbarian_count
# a. The number of Barbarians created.
    Barbarian_count = 0


# Instance Methods
# All inherited instance methods, plus:
# 1. __init__()
# a. Description: Constructs a new Barbarian object.
# b. Parameters: 4
# i. name_param (String)
# ii. color_param (String)
# iii. health_points_param (int)
# iv. rage_points_param (int)
# c. Returns 0
# d. Inherits from Player and extends functionality. Assigns parameters to instance attributes. Increases
# Barbarian_count by 1.
    def __init__(self, name_param, color_param, health_points_param, rage_points_param: int):
        # Instance Attributes
        # All Inherited instance attributes, plus:
        # 1. self.rage_points
        # a. The number of rage_points on the Barbarian (int)
        super().__init__(name_param, color_param, health_points_param) #super() allows for inheritance of Player __init__
        self.rage_points: int = rage_points_param
        Barbarian.Barbarian_count += 1

# 2. __str__()
# a. Description: retrieves data about the Barbarian when printing.
# b. Parameters: 0
# c. Returns: 1
# i. Data about the Wizard, such as: "The blue plainsman barbarian has 6 health
# points and 2 rage points." (String)
    def __str__(self):
        return(f"The {self.color} Barbarian named {self.name} has {self.health_points} health points and {self.rage_points} rage points.")

# 3. get_rage_points()
# a. Description: Retrieves Barbarian rage points count.
# b. Parameters: 0
# c. Returns: 1
# i. self.rage_points instance attribute
    def get_rage_points(self):
        return self.rage_points

# 4. get_power()
# a. Description: retrieves the power of the Barbarian
# b. Parameters: 0
# c. Returns: 1
# i. self.health_points + self.rage_points (int)
    def get_power(self):
        return self.health_points + self.rage_points

# 5. lose_fight()
# a. Description: Barbarian potentially loses health_points and rage_points.
# b. Parameters: 0
# c. Returns: 0
# d. Inherits from Player to potentially lose health_points. Additionally, based on the number of existing rage
# points, randomly generate a number and lose that number of rage points. update self.rage_points
# instance attribute.
    def lose_fight(self):
        super().lose_fight() #super() allows for inheritance of Player lose_fight()
        self.rage_points -= random.randint(1, self.rage_points)






