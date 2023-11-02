'''
Functions
1. file_read_header()
a. Description: Retrieves the first line from a text file.
b. Parameters: 1
i. File name (string)
c. Returns: 1
i. The first line of the file (String)
2. file_read_data()
a. Description: Retrieves all data from a text file except the first line.
b. Parameters: 1
i. File name (String)
c. Returns: 1
i. All the data from the file except for the first line (list)
3. main()
a. Description: Primary entrypoint to your codebase.
b. Parameters: 0
c. Returns: 0
d. Loads the contents of the file into two variables by calling their respective functions. Then prints the header
row and iterates through (item by item) and prints the rest of the data
'''
def file_read_header(file_name): #opens file and extracts first line (header)
    f_in = open(file_name, 'r')
    headers = f_in.readline()
    f_in.close() #always close
    return headers
#return open(file_name, 'r').readline()

def file_read_data(file_name: str) -> list[str]: #reads lines beyond header and stores them in list which is returned
    result_lines: list[str] = []
    with open(file_name, 'r') as f_in:
        f_in.readline() #skip header
        for line in f_in:
            line = line.strip()
            if line:
                result_lines.append(line)
    return result_lines

def main():
    input_file_name = "oscar_age_female.csv"
    headers = file_read_header(input_file_name)
    file_data = file_read_data(input_file_name)
    print("Header:")
    print("\t" + headers, end="") #returns headers
    print("Data:")
    for line in file_data: #returns main data
            print("\t" + line)

if __name__ == "__main__":
    main()

