import copy

class CoastState:

    def __init__(self, c, m):
        self.cannibals = c
        self.missionaries = m

    # function that checks for safe coast states
    def valid_coast(self):
        if self.missionaries >= self.cannibals or self.missionaries == 0:
            return True
        else:
            return False

    #function thta checks if the given state is the end one
    def goal_coast(self):
        if self.cannibals == 3 and self.missionaries == 3:
            return True
        else:
            return False



class GameState:

    def __init__(self, data):
        self.data = data
        self.parent = None


    #checks if both the right and left coasts are valid ones
    def is_valid(self,coast,across_coast,children,temp):
        if coast.valid_coast() and across_coast.valid_coast():
            child = GameState(temp)
            child.parent = self
            children.append(child)

    #calculates the number of cannibals and missionaries after each move
    def calculator(mis,can,coast,across_coast,temp):
        coast.cannibals = coast.cannibals - can
        across_coast.cannibals = across_coast.cannibals + can
        coast.missionaries = coast.missionaries - mis
        across_coast.missionaries = across_coast.missionaries + mis


    # Creating the Search Tree with all possible moves
    def building_tree(self):
        children = []
        coast = ""
        across_coast = ""
        temp = copy.deepcopy(self.data)
        if self.data["boat"] == "left":
            coast = "left"
            across_coast = "right"
        elif self.data["boat"] == "right":
            coast = "right"
            across_coast = "left"

        # MOVING 2 CANNIBALS (CC)
        if temp[coast].cannibals >= 2:
            GameState.calculator(0,2,temp[coast],temp[across_coast],temp)
            temp["boat"] = across_coast
            GameState.is_valid(self,temp[coast],temp[across_coast],children,temp)

        temp = copy.deepcopy(self.data)

        # MOVING 2 MISSIONARIES (MM)
        if temp[coast].missionaries >= 2:
            GameState.calculator(2,0,temp[coast],temp[across_coast],temp)
            temp["boat"] = across_coast
            GameState.is_valid(self,temp[coast],temp[across_coast],children,temp)

        temp = copy.deepcopy(self.data)

        # MOVING 1 CANNIBAL (C)
        if temp[coast].cannibals >= 1:
            GameState.calculator(0,1,temp[coast],temp[across_coast],temp)
            temp["boat"] = across_coast
            GameState.is_valid(self,temp[coast],temp[across_coast],children,temp)

        temp = copy.deepcopy(self.data)

        # MOVING 1 MISSIONARY (M)
        if temp[coast].missionaries >= 1:
            GameState.calculator(1,0,temp[coast],temp[across_coast],temp)
            temp["boat"] = across_coast
            GameState.is_valid(self,temp[coast],temp[across_coast],children,temp)

        temp = copy.deepcopy(self.data)

        # MOVING 1 CANNIBAL AND 1 MISSIONARY (CM && MC)
        if temp[coast].missionaries >= 1 and temp[coast].cannibals >= 1:
            GameState.calculator(1,1,temp[coast],temp[across_coast],temp)
            temp["boat"] = across_coast
            GameState.is_valid(self,temp[coast],temp[across_coast],children,temp)

        temp = copy.deepcopy(self.data)


        return children
