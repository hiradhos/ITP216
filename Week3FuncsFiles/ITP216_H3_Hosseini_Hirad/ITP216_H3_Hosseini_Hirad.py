# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# Homework 3
# Description:
# Describe what this program does in your own words.
'''
This program takes in a csv file containing all movies starring Robert Deniro and stores the header and movies list in a separate variables, which are then
analyzed via various functions such as calculate_mean() and find_movies_above_score() to output relevant details.
'''

'''
1. file_reader()
a. Description: Retrieves the entire contents of a text file.
b. Parameters: 1
i. File name (string)
c. Returns: 2
i. The header from the file (list)
ii. All the rest of data from the file (list)

2. calculate_mean()
a. Description: calculates the average value of a collection of values.
b. Parameters: 1
i. A collection of integers (list)
c. Returns: 1
i. The mean score (float)

3. find_movies_above_score()
a. Description: from an initial list, retrieves a list of all the movies with scores above a certain value.
b. Parameters: 2
i. A collection of movies (list)
ii. A score (float)
c. Returns: 1
i. A collection of all movies - in the format of [year, score, title] - with a score above the given score
(list)

4. main()
a. Description: Primary entrypoint to your codebase.
b. Parameters: 0
c. Returns: 0
d. Loads the contents of the file into two variables, and then analyzes that data and presents the results on the
console.
'''

def file_reader(file_name: str) -> list[list[str]]: #reads in header and body text into respective variables and outputs them
    header: list[str] = []
    body: list[list[str]] = [] #we are using a list of lists because we want to separate the movie year, score, and title for further processing
    with open(file_name, 'r') as f_in:
        header = f_in.readline().strip().split(", ")  # read in header and split category terms
        for i in range(len(header)):
            header[i] = header[i].replace("\"", "") #remove quotation marks
        for line in f_in: #read in rest of file
            line = line.strip().split(", ", 2) #separates movie year, score, and title. The max-split argument of split() allows us to prevent splitting of movie titles containing commas
            if len(line) > 1:
                line[1] = line[1].strip() #removes leading whitespace in score string
                line[2] = line[2].replace("\"", "") #removes quotation marks in movie title string
                body.append(line)
    return header, body

def calculate_mean(values: list[int]) -> float: #takes list of integers (such as movie scores) and returns the mean score
    rolling_value = 0
    for value in values:
        rolling_value += value
    return float(rolling_value)/len(values) #we need to type cast the sum as a float such that we have decimal points

def find_movies_above_score(movies: list[list[str]], score: float) -> list[list[str]]: #takes a list of movie strings and checks if score category is above given score threshold, and outputs list containing only movies with appropriate score
    output: list[list[str]] = []
    for movie in movies:
        if int(movie[1]) > score: #index 1 of movie string is the score of the movie
            output.append(movie)
    return output

def main():
    file_name = "deniro.csv"
    header, body = file_reader(file_name)
    print("I love Robert Deniro!")
    scores: list[int] = []
    for i in range(len(body)): #extracts the score of each movie and appends to list of ints called "scores"
        scores.append(int(body[i][1]))
    print(f"The average Rotten Tomatoes score for his movies is {calculate_mean(scores)}.")
    print(f"Of {len(body)} movies, {len(find_movies_above_score(body, calculate_mean(scores)))} are above average.") #we use len() to find the number of movies above the score threshold
    print("Here they are:")
    print("\t" + "\t".join(header)) #outputs header
    for movie in body: #outputs all movies
        i = 1
        for detail in movie:
            if i != 3: #we use indexing to ensure that there is no endline for non-terminal indices
                print("\t" + detail, end="")
                i += 1
            else: #once we reach terminal index, we insert an endline and reset the index counter
                print("\t\t" + detail)
                i = 0

if __name__ == "__main__":
    main()