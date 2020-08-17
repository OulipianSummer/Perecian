def make(size):
    """
    Usage:
    make() is the main function of squares.
    It produces an arbitrary number of graeco latin squares for use in indexing the prompt csv's.

    Arguments:
    size : A number greater than 6, and equal to or less than 10
    
    """

    latin_squares = []
    
    # Loop is called size squared times for the sake of having more latin squares than needed
    for square in range(1, (size * size)):
        
        all_squares = []
        
        # Loop creates latin squares of size by size order
        for i in range(size):
            row = []
            
            for j in range(size):
                
                # Formula ensures valid latin squares are produced
                value = (square*i + j) % size
                row.append(value)
            
            all_squares.append(row)
        
        latin_squares.append(all_squares)

    valid_squares = []

    num_of_ls = len(latin_squares)
    
    for i in range(num_of_ls):
        
        current_sq = latin_squares[i]
        
        for j in range(i+1, num_of_ls):
            
            next_sq = latin_squares[j]
            new_mols = []
            
            for current_row, next_row in list(zip(current_sq, next_sq)):
                new_mols.append(list(zip(current_row, next_row)))
                
                if is_valid(new_mols):
                    valid_squares.append(new_mols)

                # TODO: Develop some sort of shuffling mechanic for the MOLS list
                # TODO: Develop a dynamic length varable for this test below
            if len(valid_squares) == 21:
                break
            else:
                continue

    return valid_squares      

def is_valid(mols):
    """
    is_valid() checks each mols to see if the rows contain unique pairings of numbers

    Arguments:
    mols : a mutually orthogonal latin square
    
    """
    size = len(mols) ** 2
    row_set = set()
    for row in mols:
        row_set.update(row)
    return len(row_set) == size

