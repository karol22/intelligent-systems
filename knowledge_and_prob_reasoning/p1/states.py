#------------------------------------------------------------------------------------------------------------------
#   Geography analyzer.
#
#   This code is an adaptation of the geography analyzer described in:
#   Artificial intelligence with Python. Alberto Artasanchez and Prateek Joshi. 2nd edition, 2020, 
#   editorial Pack. Chapter 9.
#
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------
from kanren import run, fact, eq, Relation, var

#------------------------------------------------------------------------------------------------------------------
#   Main function
#------------------------------------------------------------------------------------------------------------------
def main():

    # Define relations
    adjacent = Relation()
    coastal = Relation()

    # Read the file containing the coastal states
    file_coastal = 'coastal_states.txt'
    with open(file_coastal, 'r') as f:
        line = f.read()
        coastal_states = line.split(',')

    # Add the info to the fact base
    for state in coastal_states:
        fact(coastal, state)

    # Read the file containing the coastal states
    file_adjacent = 'adjacent_states.txt'
    with open(file_adjacent, 'r') as f:
        adjlist = [line.strip().split(',') for line in f if line and line[0].isalpha()]

    # Add the info to the fact base
    for L in adjlist:
        head, tail = L[0], L[1:]
        for state in tail:
            fact(adjacent, head, state)

    # Initialize the variables
    x = var()
    y = var()

    # Is Nevada adjacent to Louisiana?
    output = run(0, x, adjacent('Nevada', 'Louisiana'))
    print('\nIs Nevada adjacent to Louisiana?:')
    print('Yes' if len(output) else 'No')

    # States adjacent to Oregon
    output = run(0, x, adjacent('Oregon', x))
    print('\nList of states adjacent to Oregon:')
    for item in output:
        print(item)

    # States adjacent to Mississippi that are coastal
    output = run(0, x, adjacent('Mississippi', x), coastal(x))
    print('\nList of coastal states adjacent to Mississippi:')
    for item in output:
        print(item)

    # List of 7 states that border a coastal state    
    output = run(7, x, coastal(y), adjacent(x, y))
    print('\nList of ' + str(7) + ' states that border a coastal state:')
    for item in output:
        print(item)

    # List of states that adjacent to the two given states
    output = run(0, x, adjacent('Arkansas', x), adjacent('Kentucky', x))
    print('\nList of states that are adjacent to Arkansas and Kentucky:')
    for item in output:
        print(item)


if __name__ == '__main__':
    main()

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------