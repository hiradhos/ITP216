#imports the Athlete parent class from Athlete.py
from .Athlete import Athlete

# Class Boxer
# Represents a boxer athlete.
class Boxer(Athlete):
# Class Attributes
# All inherited class attributes, plus:
# 1. boxer_count
# a. The number of boxers created.
    boxer_count = 0

# Instance Methods
# All inherited instance methods, plus:
# 1. __init__()
# a. Description: Constructs a new Boxer object.
# b. Parameters: 5
# i. name_param (String)
# ii. dob_param (String)
# iii. origin_param (String)
# iv. medals_param (list)
# v. weight_class (String)
# c. Returns: 0
# d. Assigns parameters to instance attributes. Increases boxer_count by 1.
    def __init__(self, name_param, dob_param, origin_param, medals_param, weight_class_param):
    # Instance Attributes
    # All inherited class attributes, plus:
    # 1. self.weight_class
    # a. the weight class of the boxer (String)
    # 2. self.record
    # a. the fight record of the boxer (list with two items: [wins (int), losses (int)] )
        super().__init__(name_param, dob_param, origin_param, medals_param) #inherits __init__ from Athlete class
        #boxer-specific attributes
        self.weight_class = weight_class_param
        self.record = [0,0]
        Boxer.boxer_count += 1

# 2. __str__()
# a. Description: retrieves data about the boxer when printing.
# b. Parameters: 0
# c. Returns: 1
# i. Data about the boxer. (String)
    def __str__(self):
        # Sample: Mary Berry is a Light Flyweight boxer from UK born on 1935/03/24.
        # Mary Berry has a 0 - 0 record, and has won 2 medals: ['Gold (2012)', 'Gold (2016)'].
        return f"{self.name} is a {self.weight_class} boxer from {self.origin} born on {self.dob}. {self.name} has a {self.record[0]}-{self.record[1]} record, and has won {len(self.medals)} medals: {self.medals}."

# 3. Getters for the two new instance attributes (weight_class, record)
# a. Description: retrieves an attribute
# b. Parameters: 0
# c. Returns: 1
# i. self.attribute
    def get_weight_class(self):
        return self.weight_class
    def get_record(self):
        return self.record

# 4. set_weight_class()
# a. Description: sets an attribute
# b. Parameters: 1
# i. weight_class_param (String)
# c. Returns: 0
    def set_weight_class(self, weight_class_param):
        self.weight_class = weight_class_param

# 5. win_fight()
# a. Description: adds one to the wins of the boxer's record
# b. Parameters: 0
# c. Returns: 0
    def win_fight(self):
        self.record[0] += 1

# 6. lose_fight()
# a. Description: adds one to the losses of the boxer's record, then checks to see if the boxer needs to
# retire (after 10 losses)
# b. Parameters: 0
# c. Returns: 1:
# i. A message about the number of fights left before retirement, or 'This boxer has retired.'
# (String)
    def lose_fight(self):
        self.record[1] += 1
        #checks boxer loss count before outputting appropriate string
        if self.record[1] >= 10:
            return "This boxer has retired."
        else:
            return f"This fighter has {10 - self.record[1]} fights left before retirement."