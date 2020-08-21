#------------------------------------------------------------------
#   Libraries
#------------------------------------------------------------------
from csv import reader

#------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------

def make(coords, mols_list, size, path):

    chapters = size * size
    chapters_list = range(1, chapters + 1)

    # Opens a new csv file and begins reading the contents
    with open(path, newline="") as fopen:
        csvreader = reader(fopen, delimiter=",")
        
        # Skips headers and addes them to a list item
        headers = next(csvreader)

        # Holds all of the rows of prompts
        prompts_list = []

        for row in csvreader:
            prompts_list.append(row)   

    # Creates a dictionary for referencing each chapter of lists
    chapter_prompts = {i:[] for i in chapters_list}

    # Iterates through each chapter index
    for chapter in range(chapters):
        
        # Adjusts the coodrinates format for use in indexing
        x = coords[chapter][0] - 1
        y = coords[chapter][1] - 1 

        # Iterates through each pair of entries of the prompts_list variable
        for idx in range(int(len(prompts_list)/2)):
            
            # Holds the current MOLS pairing in memory
            current_mols_cell = mols_list[idx][x][y]
            
            # Skips the first two row entries for the list title and id respectively
            cell_x = current_mols_cell[0] + 2
            cell_y = current_mols_cell[1] + 2
            
            # Since prompts are collected two at a time, this variable temporarily holds them
            row_pair = []
            
            # Pulls the actuall row and all its contents into the row_pair variable
            for row in prompts_list:
                
                # Checks that the row ID matches the prompts index, matching rows are added to the list
                if int(row[0]) == idx:
                    row_pair.append(row)
                
                # Only two rows are added at a time, so this helps save a little bit of processing power and time
                if len(row_pair) == 2:
                    break    

            prompt0 = dict({row_pair[0][1]: row_pair[0][cell_x]})
            prompt1 = dict({row_pair[1][1]: row_pair[1][cell_y]})
            chapter_prompts[chapter + 1].append(prompt0)
            chapter_prompts[chapter + 1].append(prompt1)

        
    return chapter_prompts