import random
from time import process_time

def convert(matrix):
    list = []
    for i in range(3):
        for j in range(3):
            list.append(matrix[i][j])
    return list

def print_matrix(list):
    for (index, value) in enumerate(list):
        print(' %s ' % value, end=' ') 
        if index in [x for x in range(2, 9, 3)]:
            print() 
    print() 

def check(cur, goal):
    x=True
    wrong = 0
    for i in range(len(cur)):
        if(cur[i] != goal[i]):
            x = False
            if(x == False and cur[i] != 0 ):
                wrong = wrong+1
    return x

# find possible way to move

def possible_st(cur, goal):
    posible_st = []
    pos = cur.index(0)
    if(pos == 0):
        go = [2, 4]
    elif(pos == 1):
        go = [1, 2, 4]
    elif(pos == 2):
        go = [1, 4]
    elif(pos == 3):
        go = [2, 3, 4]
    elif(pos == 4):
        go = [1, 2, 3, 4]
    elif(pos == 5):
        go = [1, 3, 4]
    elif(pos == 6):
        go = [2, 3]
    elif(pos == 7):
        go = [1, 2, 3]
    else:
        go = [1, 3]
  
    for g in go:
        #left
        if(g == 1):
            n_post = cur[:]
            n_post[pos-1], n_post[pos] = n_post[pos], n_post[pos-1]
            posible_st.append(n_post)
        #right
        if(g == 2):
            n_post = cur[:]
            n_post[pos+1], n_post[pos] = n_post[pos], n_post[pos+1]
            posible_st.append(n_post)
        #up
        if(g == 3):
            n_post = cur[:]
            n_post[pos-3], n_post[pos] = n_post[pos], n_post[pos-3]
            posible_st.append(n_post)

        #down
        if(g == 4):
            n_post = cur[:]
            n_post[pos+3], n_post[pos] = n_post[pos], n_post[pos+3]
            posible_st.append(n_post)
            
    return posible_st

def manhattan_distance(cur, g):
    h = 0
    for node in cur:
        if node != 0:
            gdist = abs(g.index(node) - cur.index(node))
            # print("---- node:", node, " gdist:", gdist)
            (jumps, steps) = (gdist // 3, gdist % 3)
            # print("jumps:", jumps, " step:", steps)
            h += jumps + steps
            # print("h:", h)
        
    #         print("mdist:", mdist)
    # print("total:", mdist)
    return h


def next_state(cur, g):
    exp_sts = possible_st(cur, g)
    mdists = []
    for cur in exp_sts:
        if(cur in visited):
            exp_sts.remove(cur)
    for cur in exp_sts:
        mdists.append(manhattan_distance(cur, g))
    mdists.sort()
    short_path = mdists[0]

    if mdists.count(short_path) > 1:
        least_paths = [cur for cur in exp_sts if manhattan_distance(cur, g) == short_path]
        print("least:", least_paths)
        return random.choice(least_paths)
    else:
        for cur in exp_sts:
            if (manhattan_distance(cur, g) == short_path):
                return cur

# Solve until reach goal
def solve(cur, goal):
    count = 0
    while not check(cur, goal):
        cur = next_state(cur, goal)
        print_matrix(cur)
        count = count + 1
        if(count == 1000):
            print("Cannot find the optimal solution")
            break

# many least
start = [[2, 8, 3],
         [1, 6, 4],
         [7, 0, 5]]

# start = [[1, 0, 2],
#          [4, 5, 3],
#          [7, 8, 6]]

# start = [[1, 2, 3],
#          [4, 0, 5],
#          [6, 7, 8]]

# goal = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 0]]

goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]

visited = []
print("-- start state --")
start_list = convert(start)
visited.append(start_list)
print(start_list)
print_matrix(start_list)

print("-- goal state --")
goal_list = convert(goal)
print_matrix(goal_list)

print("-- start solving A*--")
t1_start = process_time()
solve(start_list, goal_list)
t1_stop = process_time()
print("Process time:", t1_stop-t1_start)

