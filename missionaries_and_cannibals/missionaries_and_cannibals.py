
### Explanation: 
### (M, C, B) means that in the original side of the river there are
###  - M missionaries
###  - C Cannibals and
###  - B is 0 if it is in the other side of the river and 1 if it is in the original side
###   
###  A move (m, c, b) means that the boat will take m missionaries and c cannibals from one
###  side of the river to the other
### 
###  We can calculate that the a new state can be defined as 
###  new_state = (M, C, B) - (m, c, b), taking (B-b)%2
###
### Then, our goal is to get the final state (0, 0, 0)

# Initial configuration

NUM = 3
initial_state = (NUM, NUM, 1)
moves = [(1, 0, 1), (2, 0, 1), (0, 1, 1), (0, 2, 1), (1, 1, 1)]
visited = {initial_state}
goal = (0, 0, 0)
states = {
        initial_state: []
}

# Autodescriptive
def is_valid_move(current_state, move):
    tentative_left = next_state(current_state, move)
    tentative_right = (NUM - tentative_left[0],  NUM - tentative_left[1])
    # cannot get negative values
    if((tentative_left[0]< 0) or (tentative_left[1]< 0)):
        return False
    # Cannot get numbers greater than 3
    if( (tentative_left[0] > 3) or (tentative_left[1] > 3) ):
        return False
    #it cannot be more cannibals than missionaries at each side after the move
    if( (tentative_left[1] > tentative_left[0] and tentative_left[0] > 0) or (tentative_right[1] > tentative_right[0] and tentative_right[0] > 0)):
        return False
    return True


# List of next valid steps
def next_state(current_state, move):
    if(current_state[2] == 1):
        return (current_state[0] - move[0], current_state[1] - move[1], 0)
    return (current_state[0] + move[0], current_state[1] + move[1], 1)


# return list of non-repeated states from node
def next_states(node, moves, visited):
    ans = []
    for m in moves:
        if(is_valid_move(node, m)):
            new_node = next_state(node, m)
            if not (new_node in visited):
                visited.add(new_node)
                ans.append(new_node)
    return ans

def bfs(start, end):
    # queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while (queue):
        # get node to process
        path = queue.pop(0)
        node = path[-1]

        # return condition
        if (node == end):
            return path
        
        # append new nodes
        new_nodes = next_states(node, moves, visited)

        states[node] += new_nodes

        for elem in new_nodes:
            states[elem] = []

        # create new path and add to queue
        for adjacent in states.get(node, []): 
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

def print_path(path):
    print()
    print("This is the solution: ")
    print()
    print("M   C            M   C")
    path.pop(0)
    print("3   3            0   0")
    for elem in path:
        if elem[2] == 1:
            way = "  <---  "
        else:
            way = "  --->  "
        print(elem[0], " ", elem[1], way, " ", 3 -elem[0], " ", 3 -elem[1])
    print()

answer = bfs(initial_state, goal)
print_path(answer)

