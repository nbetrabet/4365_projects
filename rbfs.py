import sys
import math


class State:
    state = [] #holds state of the board
    f = -1 #holds manhattan distance of the current state

    def __init__(self, newState):
        self.state = newState #initializes with passed in state array
        fSum = 0 #begin to calc the manhattan sum
        for i in range(0,9): #for each tile
            if i != self.state[i]: # if tile is not in correct position
                fSum += abs((i % 3) - (self.state[i] % 3)) + abs((int)(i / 3) - (int)(self.state[i] / 3)) #calc manhattan distance and add to sum
        self.f = fSum #save sum in object variable
        return
    def printState(self):
        stateForm = "" #will hold printable string
        for i in range(0, 9): # for each item in the list
            stateForm += str(self.state[i]) #add the tile number to string
            if (i == 2 or i == 5 or i == 8): #if the tile is at the end of a 'row'
                stateForm += '\n' #add newline char
            else: #else
                stateForm += '\t' #add tab char
        print(stateForm)
        return
    def getState(self): #getter function for state data, isolates object data from manipulation by function
        return self.state


class Problem:

    def goalState(self, state):
        goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8] #This is the desired goal state
        return state == goalstate #check if the current state is equal to the goal

    def actionList(self, state): #creates list of legal actions given position of 0
        action = []
        pos = -1
        #for i in range(0,8):
            #if state[i] == 0:
                #pos = i #finds index of 0, replace with state.index(0) eventually
        pos = state.index(0)
        if (pos % 3) != 0:
            action.append('left') #if the 0 is not on the 'left edge' of the board, include left as legal move
        if (pos % 3) != 2:
            action.append('right') #if the 0 is not on the 'right edge' of the board, include left as legal move
        if int(pos / 3) != 0:
            action.append('up')#if the 0 is not on the 'top edge' of the board, include left as legal move
        if int(pos / 3) != 2:
            action.append("down") #if the 0 is not on the 'bottom edge' of the board, include left as legal move

        return action


def parseInput(file): #parses input file
    f = open(file, "r") #open readable file
    state = []
    data = f.read(18) #read in the 18 chars that make up the board
    for char in data:
        if (char != '\t' and char != '\n'):
            state.append(int(char)) #add each char that isn't a newline or tab char
    return state #return the initial state list


def successor(state, action): #creates the state of the successor based on action
    pos = state.index(0) #find position of 0 on board
    newState = state
    if action == 'up': #if we want to move the 0 up
        swap = newState[pos - 3] #swap with tile 'above' the 0
        newState[pos - 3] = 0
        newState[pos] = swap
    elif action == 'down': #if we want to move the 0 down
        swap = newState[pos + 3] #swap with the tile 'below' the 0
        newState[pos + 3] = 0
        newState[pos] = swap
    elif action == 'left': #if we want to move the 0 left
        swap = newState[pos - 1] #swap with the tile to the left of the 0
        newState[pos - 1] = 0
        newState[pos] = swap
    elif action == 'right': #if we want to move the 0 to the right
        swap = newState[pos + 1] #swap with the tile to the right of the 0
        newState[pos + 1] = 0
        newState[pos] = swap
    return newState #return the succeeding state list


def rbfs(prob, node, fLim, pList, vList, g): #handles the rbfs
    #if node.state in vList: #if the node has been visited before
        #return None, math.inf, pList, vList
    vList.append(node.state)
    if prob.goalState(node.state): #if we are at the goal state
        pList.insert(0, node) #push the current state onto the path list
        return node, 0, pList, vList #return current node, f = 0, and the new path list
    successors = [] #create list of successors
    actList = prob.actionList(node.state) #create action list for current state
    for act in actList: #for each action
        suc = State(successor(node.state.copy(), act)) #create the state obj and state list based upon current state list and action
        successors.append(suc) #append new successor to the list of successors
    if len(successors) == 0: #if there are no successors
        return None, math.inf, pList, vList #return no node, infinite fcost, and current path list
    for su in successors: #for each successor in the list
        su.f = max(su.f + g, node.f) #determine if the successor fcost is higher than that of the current node
    while True: #repeat forever
        successors.sort(key=lambda x: x.f) #sort our successors by fcost
        best = successors[0] #identify the best successor
        if best.f > fLim: #if the fcost of the best node is greater than that of the flim
            return None, best.f, pList, vList #return no node, but maintain flim
        if len(successors) > 1: # if there is more than one successor
            alternative = successors[1].f #hold the best alternative fcost
        else: #else
            alternative = math.inf #alternative cost is infinite
        result, best.f, pListNew, vListNew = rbfs(prob, best, min(fLim, alternative), pList, vList, g + 1) #begin to expand the best successor
        if result is not None: #if there is a node returned
            pListNew.insert(0, node) #push the current node onto the path list
            return result, best.f, pListNew, vListNew #return the current nodem, best fcost, and new path list


def main():
    inp = parseInput("inputTest.txt")
    #x = State([3,4,1,6,0,2,7,8,5])
    #x.printState()
    x = State(inp)
    puzzle = Problem()
    pathList = []
    visitedList = []
    result, best, pathList, visitedList = rbfs(puzzle, x, math.inf, pathList, visitedList, 0)
    print(len(pathList) - 1)
    for t in pathList:
        t.printState()


main()
