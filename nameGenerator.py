import random

male_names = ["Alex", "Brandon", "Bradley", "Chris", "Caden", "Cayden", "Colby", "Kaydn", "Harrison",\
                     "Hunter"]
female_names = ["Ashley", "Bridgett", "Daniela", "Erica", "Haley", "Isabel", "Jessica", "Kayla", "Myla"\
                     "Nina"]

def name_array(file):
    # open file with names
    with open(file) as fp:
        new_list = []
        # loop through each line in the txt file
        for line in fp:
            # remove white spaces next to each name and add
            # to the new_list array
            new_list.append(line.strip())
    return new_list

# call the function three times to transform names from each
# file into arrays
file = "male_first_names.txt"

file = "female_first_names.txt"
