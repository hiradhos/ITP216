# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# Lab 6
# Description:
# Describe what this program does in your own words such as:
'''
This program practices with the concepts of comprehensions and generators to do a variety of tasks.
'''

# 1. Write a comprehension which creates a list (called sevens) consisting of all multiples of seven from 1 to
# 1000. For context: this list should be 142 items long.
sevens = [i for i in range(1, 1001) if i % 7 == 0]
print(sevens)
print(len(sevens))

# 2. Write a comprehension which creates a dictionary (called birdos) consisting of the following content
# (paired currently by index):
name = ['Great potoo', 'Smew', 'Tundra bean goose', 'Southern pied babbler']
genus_and_species = ['Nyctibius grandis', 'Mergellus albellus', 'Anser serrirostris', 'Turdoides bicolor']

birdos = {key:value for key, value in zip(name, genus_and_species)}
print(birdos)

# 3. Write a generator
# expression which creates a generator (called square_gen) which will yield two values:
# a number and its square. You can test it by running the following code:

square_gen = ((num, num**2) for num in range(10))

for number, square in square_gen:
    print(number, 'squared:', square)