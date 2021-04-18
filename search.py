import time
from game import CoastState, GameState

# the search algorithms code
def breadth_first_search():
    tic = time.perf_counter()
    left = CoastState(3, 3) #creating the coasts and assigning number of missionaries and cannibals
    right = CoastState(0, 0)
    root_data = {"left": left, "right": right, "boat": "left"}

    visited = []
    nodes = []
    solution = []
    nodes.append(GameState(root_data))

    while len(nodes) > 0 :
        g = nodes.pop(0)
        visited.append(g)
        if g.data["right"].goal_coast():
            solution.append(g)
            toc = time.perf_counter()
            end_time = toc - tic
            return g , end_time
        else:
            next_children = g.building_tree()
            for x in next_children:
                if x not in visited :
                    nodes.append(x)
    return None


def depth_fisrt_search():
    tic = time.perf_counter()
    left = CoastState(3, 3) #creating the coasts and assigning number of missionaries and cannibals
    right = CoastState(0, 0)
    root_data = {"left": left, "right": right, "boat": "left"}

    visited = []
    nodes = []
    solution = []
    nodes.append(GameState(root_data))

    while len(nodes) > 0 :
        g = nodes.pop(-1)
        visited.append(g)
        if g.data["right"].goal_coast():
            solution.append(g)
            toc = time.perf_counter()
            end_time = toc - tic
            return g , end_time
        else:
            next_children = g.building_tree()
            for x in reversed(next_children):
                #print(1)
                if x not in visited :
                    nodes.insert(0,x)
    return None
