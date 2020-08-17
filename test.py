
def show_grid(g):
    for row in g:
        print(row)
    print()

def test_mols(g):
    ''' check that all entries in g are unique '''
    size = len(g) ** 2
    a = set()
    for row in g:
        a.update(row)
    return len(a) == size

def mols(n):
    ''' Generate a set of mutually orthogonal latin squares 
        n must be prime
    ''' 
    r = range(n)

    #Generate each Latin square
    allgrids = []
    for k in range(1, n):
        grid = []
        for i in r:
            row = []
            for j in r:
                a = (k*i + j) % n
                row.append(a)
            grid.append(row)
        allgrids.append(grid)

    for g in allgrids:
        show_grid(g)

    print('- ' * 20 + '\n')

    #Combine the squares to show their orthoganility
    m = len(allgrids)
    for i in range(m):
        g0 = allgrids[i]
        for j in range(i+1, m):
            g1 = allgrids[j]
            newgrid = []
            for r0, r1 in list(zip(g0, g1)):
                newgrid.append(list(zip(r0, r1)))
            print(test_mols(newgrid))
            show_grid(newgrid)

mols(10)