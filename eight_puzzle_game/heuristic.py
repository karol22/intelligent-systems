import random

N = 5
def initial_matrix(size):
    return [[size*i + j for j in range(size)] for i in range(size)]

# create random matrix after performing moves to matrix
def randmat(size, moves):
    my_mat = initial_matrix(size)
    ix, iy = 0, 0
    for _ in range(moves):
        direction = random.randrange(4)
        ix, iy = move(my_mat, direction, ix, iy)
    return my_mat

def misplaced(mat_str):
    m = eval(mat_str)
    diffs = 0        
    for i in range(N):
        for j in range(N):
            if(m[i][j]<N*i+j and m[i][j] != 0):
                diffs = diffs +1
    return diffs

# move , matrix and direction (1, 2, 3, 4) up, left, down, right
def move(mat, direction, i, j):
    n = len(mat[0])
    if direction == 0: # up
       if i > 0:
           mat[i][j], mat[i-1][j] = mat[i-1][j], mat[i][j]
           return i-1, j
    elif direction == 1: # left
        if  j > 0:
            mat[i][j], mat[i][j-1] = mat[i][j-1], mat[i][j]
            return i, j-1
    elif direction == 2: # down
        if  i < n-1:
            mat[i][j], mat[i+1][j] = mat[i+1][j], mat[i][j]
            return i+1, j
    elif direction == 3: # right
        if  j < n-1:
            mat[i][j], mat[i][j+1] = mat[i][j+1], mat[i][j]
            return i, j+1
    return i, j

def astar(start,goal):
    queue = [[misplaced(start), start]]
    nodes = set()
    num_nodes=0
    while queue:
        i = 0
        for j in range(1, len(queue)):
            if queue[i][0] > queue[j][0]:
                i=j
        path = queue[i]
        queue = queue[0:i] + queue[i+1:]
        front = path[-1]
        if front in nodes:
            continue
        for nd in next_steps(front):
            if nd in nodes:
                continue
            best = [path[0]+misplaced(nd)-misplaced(front)]+path[1:]+[nd] 
            queue.append(best)
            nodes.add(front)
        num_nodes += 1 
        if front == goal:
            break
    return path[1:], num_nodes

# Generate all configurations for una state
def next_steps(mat_str): 
    m_list = eval(mat_str)   
    possible_matrices = [] 
    i = 0
    while 0 not in m_list[i]: i += 1
    j = m_list[i].index(0)
    if i > 0:                                   
        m_list[i][j], m_list[i-1][j] = m_list[i-1][j], m_list[i][j]
        possible_matrices.append(str(m_list))
        m_list[i][j], m_list[i-1][j] = m_list[i-1][j], m_list[i][j] 
    if j > 0:                                                      
        m_list[i][j], m_list[i][j-1] = m_list[i][j-1], m_list[i][j] 
        possible_matrices.append(str(m_list))
        m_list[i][j], m_list[i][j-1] = m_list[i][j-1], m_list[i][j]
    if i < N -1:                                   
        m_list[i][j], m_list[i+1][j] = m_list[i+1][j], m_list[i][j]
        possible_matrices.append(str(m_list))
        m_list[i][j], m_list[i+1][j] = m_list[i+1][j], m_list[i][j]
    if j < N -1:                                   
        m_list[i][j], m_list[i][j+1] = m_list[i][j+1], m_list[i][j]
        possible_matrices.append(str(m_list))
        m_list[i][j], m_list[i][j+1] = m_list[i][j+1], m_list[i][j]
    return possible_matrices

NUM_TRIES = 1
sum_nodes = 0
for _ in range(NUM_TRIES):
    rr = randmat(N, 40) 
    start = str(rr)
    goal = str(initial_matrix(N))
    solution, num_expansions = astar(start, goal)
    sum_nodes+=num_expansions
    print("Number of nodes: ", num_expansions)
    print("Solution:")
    for step in solution:
        print(step)
print("Average number of nodes: ", sum_nodes/NUM_TRIES)