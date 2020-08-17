#------------------------------------------------------------------
#   Libraries
#------------------------------------------------------------------
import csv

#------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------
# Finds the coords from the tour and assigns them to the list
# TODO: add in an arg for the csv name
def make(coords, mols_list, size):

    chapters = size * size
    chapters_list = range(1, chapters + 1)

    with open("default.csv", newline="") as fopen:
        reader = csv.reader(fopen, delimiter=",")
        
        # Skips headers and addes them to a list item
        headers = next(reader)

        prompts_list = []

        for row in reader:
            prompts_list.append(row)

    chapter_prompts = {i:[] for i in chapters_list}

    for chapter in range(chapters):
        
        x = coords[chapter][0] - 1
        y = coords[chapter][1] - 1 

        # TODO: Figure out how to make the 21 lists count dynamic
        for idx in range(21):
            current_mols_cell = mols_list[idx][x][y]
            cell_x = current_mols_cell[0] + 2
            cell_y = current_mols_cell[1] + 2
            
            row_pair = []
            
            for row in prompts_list:
                if int(row[1]) == idx:
                    row_pair.append(row)
                if len(row_pair) == 2:
                    break    

            prompt0 = dict({row_pair[0][0]: row_pair[0][cell_x]})
            prompt1 = dict({row_pair[1][0]: row_pair[1][cell_y]})
            chapter_prompts[chapter + 1].append(prompt0)
            chapter_prompts[chapter + 1].append(prompt1)

        
    return chapter_prompts


#TODO: Iterate through the knigt's coordinates ex 6, 6
#TODO: Iterate through each MOLS in the MOLS list
#TODO: Using the MOLS index number as the meta_list (prompts_list[i][1]), find the bi-square value of each cell
#TODO: Using those 10 pair-values, index into the prompts_list and return the four meta lists and they x values