# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# HW 5
# Description:
# Describe what this program does in your own words such as:
'''
This program creates a Python library called "athlete" which contains a parent class Athlete along with child classes of Swimmer and Boxer. The main script
tests this library by constructing swimmer and boxer objects and testing various methods within these classes.
'''

#import the Boxer and Swimmer classes from the athlete library
from athlete.Boxer import Boxer
from athlete.Swimmer import Swimmer
def main():
    #construct swimmer and boxer objects
    swimmer = Swimmer("Dave Thomas", "1932/07/02", "USA", ['Silver (1992)', 'Gold (1996)'], ["freestyle", "breaststroke"])
    boxer = Boxer("Mary Berry", "1935/03/24", "UK", ['Gold (2012)', 'Gold (2016)'], "Light Flyweight")
    print(boxer)
    print(swimmer)
    #test swimmer and boxer class methods
    swimmer.add_stroke('backstroke')
    swimmer.add_medal('gold (now)')
    print(swimmer)
    boxer.win_fight()
    boxer.lose_fight()
    boxer.add_medal('gold (now)')
    print(boxer)
    print(boxer.lose_fight())
    print(boxer)

if __name__ == "__main__":
    main()