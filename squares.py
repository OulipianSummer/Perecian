def make(size, csv_len):
    """
    Usage:
    make() is the main function of squares.
    It produces an arbitrary number of graeco latin squares for use in indexing the prompt csv's.

    Arguments:
    size : A number greater than 6, and equal to or less than 10
    
    """

    # A list for holding all of the latin squares about to be produced
    latin_squares = []
    
    # HACK: Although it does work, it feels like a hack to call the loop size * 2 times just for the sake of getting more latin squares
    # TODO: Find some way to make this more dynamic or (at the very least) more appropriately sized to the problem at hand
    for square in range(1, (size * 2)):
        
        # A list for holding a single latin square
        current_suqare = []
        
        # Loop creates latin squares of order (size)
        for i in range(size):
           
            # A list for holding rows of squares
            row = []
            
            for j in range(size):
                
                # Formula ensures valid latin squares are produced
                value = (square*i + j) % size
                row.append(value)
            
            current_suqare.append(row)
        
        latin_squares.append(current_suqare)

    # A list that holds all valid MOLS about to be produced
    valid_squares = []

    # A variable to hold the length of the latin_squares list, for the sake of reducing stack frames
    num_of_ls = len(latin_squares)
    
    # Creates MOLS from combining two latin squares
    for i in range(num_of_ls):
        
        # Holds the current latin square in memory
        current_latin_sq = latin_squares[i]
        
        # Calls the next latin square in the sequence
        for j in range(i+1, num_of_ls):
            
            # Holds the next latin square
            next_latin_sq = latin_squares[j]
            
            # A list for holding a new MOLS object about to be created
            new_mols = []
            
            # Combines the entries of each latin square row into a new MOLS row
            for current_row, next_row in list(zip(current_latin_sq, next_latin_sq)):
                new_mols.append(list(zip(current_row, next_row)))
                
                # Checks that each new MOLS is actually valid ie. each pairing is unique
                if is_valid(new_mols, size):
                    valid_squares.append(new_mols)


            # HACK: The 21 here is a bit of hack too since there is no guarantee that the csv will always contain 42 rows.
            # TODO: Make this number actually associated to the number of rows in the csv list
            # TODO: Also, use seeded sampling to return the lists instead of just taking the first 21
            if len(valid_squares) == 21:
                break
            else:
                continue

    return valid_squares      

# Using the set function from python, checks that each entry is unique. Rows containing repeated items are thrown out
def is_valid(mols, size):
    """
    is_valid() checks each mols to see if the rows contain unique pairings of numbers

    Arguments:
    mols : a mutually orthogonal latin square
    
    """
    
    square_size = size ** 2
    row_set = set()
    
    for row in mols:
        row_set.update(row)
    
    # Since set throws out repeats, any mols that does not pass the size comparison must be invalid 
    if len(row_set) == size:
        return True
    else:
        return False    

