#imports Athlete parent class from Athlete.py
from .Athlete import Athlete

# Class Swimmer
# Represents a swimmer athlete.
class Swimmer(Athlete):
# Class Attributes
# All inherited class attributes, plus:
# 1. swimmer_count
# a. The number of swimmers created.
    swimmer_count = 0

# Instance Methods
# All inherited instance methods, plus:
# 1. __init__()
# a. Description: Constructs a new Swimmer object.
# b. Parameters: 5
# i. name_param (String)
# ii. dob_param (String)
# iii. origin_param (String)
# iv. medals_param (list)
# v. strokes (list)
# c. Returns: 0
# d. Assigns parameters to instance attributes. Increases swimmer_count by 1.
    def __init__(self, name_param, dob_param, origin_param, medals_param, strokes_param):
        # Instance Attributes
        # All inherited class attributes, plus:
        # 1. self.strokes
        # a. the strokes that the swimmer knows (list)
        super().__init__(name_param, dob_param, origin_param, medals_param) #inherits __init__ from Athlete parent class
        #swimmer class specific attributes
        self.strokes = strokes_param
        Swimmer.swimmer_count += 1


# 2. __str__()
# a. Description: retrieves data about the swimmer when printing.
# b. Parameters: 0
# c. Returns: 1
# i. Data about the swimmer. (String)
    def __str__(self):
        # Sample: Dave Thomas is a swimmer from USA born on 1932/07/02. Dave Thomas knows ['freestyle', 'breaststroke'], and has
        # won 2 medals: ['Silver (1992)', 'Gold (1996)'].
        return f"{self.name} is a swimmer from {self.origin} born on {self.dob}. {self.name} knows {self.strokes}, and has won {len(self.medals)} medals: {self.medals}."

# 3. get_strokes()
# a. Description: retrieves the strokes attribute
# b. Parameters: 0
# c. Returns: 1
# i. self.strokes
    def get_strokes(self):
        return self.strokes()

# 4. add_stroke()
# a. Description: adds a new stroke to the swimmer's repertoire. Checks to make sure the stroke is
# not already in the list
# b. Parameters: 1
# c. Returns: 0
    def add_stroke(self, stroke_param):
        if stroke_param not in self.strokes: #checks if stroke type is already in list
            self.strokes.append(stroke_param)
