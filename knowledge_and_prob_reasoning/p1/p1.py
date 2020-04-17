# Imports
from kanren import run, fact, eq, Relation, var, conde

def main():
    # Define relations
    adjacent = Relation()
    crime = Relation()
    drought = Relation()
    brandy = Relation()
    industrial = Relation()
    agricultural = Relation()
    smart = Relation()


    # Read the file containing the coastal states
    file_adjacent = 'mexican_adjacent_states.txt'
    with open(file_adjacent, 'r') as f:
        adjlist = [line.strip().split(',') for line in f if line and line[0].isalpha()]
    # Add the info to the fact base
    for L in adjlist:
        head, tail = L[0], L[1:]
        for state in tail:
            fact(adjacent, head, state)
    
    # Read the file containing the high crime states
    file_crime = 'crime_rate.txt'
    with open(file_crime, 'r') as f:
        line = f.read()
        crime_states = line.split("\n")
        print("crime states: ", crime_states)
    # Add the info to the fact base
    for state in crime_states:
        fact(crime, state)
    
    # Read the file containing the severe drought states
    file_drought = 'drought.txt'
    with open(file_drought, 'r') as f:
        line = f.read()
        drought_states = line.split("\n")
        print("drought states: ", drought_states)
    # Add the info to the fact base
    for state in drought_states:
        fact(drought, state)

    # Read the file containing the brandy states
    file_brandy = 'brandy.txt'
    with open(file_brandy, 'r') as f:
        line = f.read()
        brandy_states = line.split("\n")
        print("brandy states: ", brandy_states)
    # Add the info to the fact base
    for state in brandy_states:
        fact(brandy, state)

    # Read the file containing the industrial states
    file_industrial = 'industrial.txt'
    with open(file_industrial, 'r') as f:
        line = f.read()
        industrial_states = line.split("\n")
        print("industrial states: ", industrial_states)
    # Add the info to the fact base
    for state in industrial_states:
        fact(industrial, state)

    # Read the file containing the industrial states
    file_smart = 'smart.txt'
    with open(file_smart, 'r') as f:
        line = f.read()
        smart_states = line.split("\n")
        print("smart states: ", smart_states)
    # Add the info to the fact base
    for state in smart_states:
        fact(smart, state)

    # Read the file containing the industrial states
    file_agricultural = 'agricultural.txt'
    with open(file_agricultural, 'r') as f:
        line = f.read()
        agricultural_states = line.split("\n")
        print("agricultural states: ", agricultural_states)
    # Add the info to the fact base
    for state in agricultural_states:
        fact(agricultural, state)
    
    # Initialize the variables
    x = var()
    y = var()
    z = var()

    # What states have high crime rates and have a severe drought?
    print("\nWhat states have high crime rates and have a severe drought?\n")
    output = run(0, x, crime(x), drought(x))
    for item in output:
        print(item)

    # What states are adjacent to the states with people that prefer to drink brandy?
    print("\nWhat states are adjacent to the states with people that prefer to drink brandy?\n")
    output = run(0, x, adjacent(x, y), brandy(y))
    for item in output:
        print(item)

    # What states are industrialized and are good places for smart people?
    print("\nWhat states are industrialized and are good places for smart people?\n")
    output = run(0, x, industrial(x), smart(x))
    for item in output:
        print(item)

    # What states are adjacent to the agricultural states or adjacent to industrialized states?
    print("\nWhat states are adjacent to the agricultural states or adjacent to industrialized states?\n")
    output = run(0, x, conde((adjacent(x, y), agricultural(y)), (adjacent(x, y), industrial(y))))
    for item in output:
        print(item)

    # What states are adjacent to both Estado de México and Ciudad de México?
    print("\nWhat states are adjacent to both Estado de México and Ciudad de México?\n")
    output = run(0, x, adjacent(x, "Estado de México"), adjacent(x, "Ciudad de México"))
    for item in output:
        print(item)

    # What agricultural states have severe drought and high crime rates?
    print("\nWhat agricultural states have severe drought and high crime rates?\n")
    output = run(0, x, agricultural(x), drought(x), crime(x))
    for item in output:
        print(item)

    # What states are adjacent to a state with high crime rates?
    print("\nWhat states are adjacent to a state with high crime rates?\n")
    output = run(0, x, adjacent(x, y), crime(y))
    for item in output:
        print(item)

    # What states have smart people or have large populations that prefer to drink brandy?
    print("\nWhat states have smart people or have large populations that prefer to drink brandy?\n")
    output = run(0, x, conde([smart(x)], [brandy(x)]))
    for item in output:
        print(item)


if __name__ == '__main__':
    main()
