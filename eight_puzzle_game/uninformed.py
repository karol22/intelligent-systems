import random

N = 3
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

def bfs(start,goal):
    queue = [[start]]
    nodes = set()
    num_nodes=0
    while queue:
        i = 0
        for j in range(1, len(queue)):
            if len(queue[i]) > len(queue[j]):
                i=j
        path = queue[i]         
        queue = queue[0:i] + queue[i+1:]
        front = path[-1]
        if front in nodes: 
            continue
        for step in next_steps(front):
            if step in nodes: 
                continue
            queue.append(path + [step])
        nodes.add(front)
        num_nodes += 1
        if front == goal: 
            break
    return path, num_nodes

NUM_TRIES = 100
sum_nodes = 0
for _ in range(NUM_TRIES):
    rr = randmat(N, 30) 
    start = str(rr)
    goal = str(initial_matrix(N))
    _, num_expansions = bfs(start, goal)
    sum_nodes+=num_expansions
    #print("Number of nodes: ", num_expansions)
    #print("Solution:")
    #for step in solution:
    #    print(step)
print("Average number of nodes: ", sum_nodes/NUM_TRIES)