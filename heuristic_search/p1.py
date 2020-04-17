# Original laberynth
original = """++++++++++++++++++++++
+ O +   ++ ++        +
+     +     +++++++ ++
+ +    ++  ++++ +++ ++
+ +   + + ++         +
+          ++  ++  + +
+++++ + +      ++  + +
+++++ +++  + +  ++   +
+          + +  + +  +
+++++ +  + + +     X +
++++++++++++++++++++++
"""
lab1 = """++++++++++++++++++++++
+ O       ++         +
+++++++     +++++++ ++
+ +    ++  ++++ +++ ++
+ +   + +            +
+          ++  ++  + +
+++++ + +       +  + +
+++++ +++  + +  ++   +
+          + +  + +  +
+++++ +  + + +     X +
++++++++++++++++++++++
"""
lab2 = """++++++++++++++++++++++
+ O +   ++ ++        +
+           +++++++ ++
+ +    ++  ++++ +++ ++
+ +   + + ++         +
+          ++  ++  + +
+++++ + +      ++  + +
+++++ +++  + +++++   +
+          + +  + +  +
+++++ +            X +
++++++++++++++++++++++
"""
lab3 = """++++++++++++++++++++++
+ O +   ++           +
+           +++++++ ++
+ +    ++  ++++ +++ ++
+ +   + + ++      +  +
+          ++  +++++ +
+++++ + +      +++++ +
+++++ +++  + +  ++   +
+          + +  + +  +
+++++ +  + + +     X +
++++++++++++++++++++++
"""

def main():
    # Change lab = to one of the laberynths above
    lab = lab3 #modify this line

    n_rows = lab.count("\n")
    n_cols = int((len(lab)-n_rows)/n_rows)
    lab = lab.replace("\n", "")

    # Get positions for start and end
    find_st = lab.find('O')
    start = (int(find_st/n_cols), int(find_st%n_cols))

    find_end = lab.find('X')
    end = (int(find_end/n_cols), int(find_end%n_cols))

    # create maze matrix to ease future calculations
    maze = ([[ 1 if(lab[n_cols*i + j] == '+') else 0
    for j in range(n_cols)] for i in range(n_rows)])

    maze_string = [[lab[n_cols*i + j] for j in range(n_cols)] for i in range(n_rows)]

    print("\nOriginal laberynth: ")
    for i in range(n_rows):
        for j in range(n_cols):
            c = maze_string[i][j]
            print(c, end="")
        print() 

    path = astar(maze, start, end)

    print("\nSolved laberynth: ")
    for i in range(n_rows):
        for j in range(n_cols):
            c = maze_string[i][j]
            if ((i, j) in path):
                c = '.' 
            print(c, end="")
        print()




# Define class for each square in path
class Square():
    def __init__(self, pos=None, parent=None):
        self.parent = parent
        self.pos = pos
        self.f = 0
        self.g = 0
        self.h = 0

    def heuristic(self, x):
        return (self.pos[0] - x.pos[0])**2 + (self.pos[1] - x.pos[1])**2

# A* Algorithm
def astar(lab, start, end):
    open = []
    closed = []

    st = Square(start, None)
    tg = Square(end, None)

    open.append(st)
    while len(open) > 0:
        curr_sq = open[0]
        index = 0
        for i, sq in enumerate(open):
            if(sq.f < curr_sq.f):
                index = i
                curr_sq = sq
        closed.append(curr_sq)
        open.pop(index)

        moves = []
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (curr_sq.pos[0] + move[0], curr_sq.pos[1] + move[1])
            if(lab[new_pos[0]][new_pos[1]] != 0):
                continue
            next_sq = Square(new_pos, curr_sq)
            moves.append(next_sq)

        for sq in moves:
            for el in closed:
                if(sq.pos == el.pos):
                    continue
            sq.g = curr_sq.g + 1
            sq.h = sq.heuristic(tg)
            sq.f = sq.g + sq.h
            for el in open:
                if(sq.pos == el.pos and sq.g > el.g):
                    continue
            open.append(sq)

        if(curr_sq.pos == tg.pos):
            path = []
            el = curr_sq
            while el is not None:
                path.append(el.pos)
                el = el.parent
            return path[::-1]

if __name__ == '__main__':
    main()
