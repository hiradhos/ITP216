# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# HW 6
# Description:
# Describe what this program does in your own words such as:
'''
Re-implemented HW 3 using list/set/dictionary comprehensions and/or generator expressions instead of the for loops in file_reader() and find_movies_above_score().
'''

# file_reader()
# a. Description: Retrieves the entire contents of a text file.
# b. Parameters: 1
# i. File name (string)
# c. Returns: 2
# i. The header from the file (list)
# ii. All the rest of data from the file (list)
def file_reader(file_name: str) -> tuple: #reads in header and body text into respective variables and outputs them
    header: list[str] = []
    body: list[list[str]] = [[]]
    with open(file_name, 'r') as f_in:
        header = f_in.readline().strip().split(", ")  # read in header and split category terms
        header = [header[i].replace("\"","") for i in range(len(header))] #remove quotation marks
        body = [[line.strip().split(", ",2)[0], line.strip().split(", ", 2)[1].strip(), line.strip().split(", ", 2)[2].replace("\"", "")] for line in f_in if len(line) > 1]
    return header, body


# find_movies_above_score()
# a. Description: from an initial list, retrieves a list of all the movies with scores above a certain value.
# b. Parameters: 2
# i. A collection of movies (list)
# ii. A score (float)
# c. Returns: 1
# i. A collection of all movies - in the format of [year, score, title] - with a score above the given score
# (list)
def find_movies_above_score(movies_list: list, score: float) -> list:
    return [movie for movie in movies_list if float(movie[1]) > score]

def calculate_mean(scores_list: list) -> float: #takes list of integers (such as movie scores) and returns the mean score
    return float(sum(scores_list)/len(scores_list))

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