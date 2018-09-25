import sys


class state:
    state = []
    f = -1

    def __init__(self, newState):
        state = newState
        fSum = 0
        for i in range(0,8):
            if i != state[i]:
                fSum += abs((i % 3) - (state[i] % 3)) + abs((i / 3) - (state[i] / 3))
        f = fSum


class Problem:

    def goalState(self, state):
        goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8] #This is the desired goal state
        return state == goalstate

    def actionList(self, state):
        action = []
        pos = -1
        for i in range(0,8):
            if state[i] == 0:
                pos = i
        if (pos % 3) != 0:
            action.append('left')
        if (pos % 3) != 2:
            action.append('right')
        if (pos / 3) != 0:
            action.append('up')
        if (pos / 3) != 2:
            action.append("down")

        return action


def parseInput(file):
    f = open(file, "r")
    state = []
    data = f.read(18)
    for char in data:
        if (char != '\t' and char != '\n'):
            state.append(int(char))
    return state


def successor(node, action):
    pos = node.index(0)
    newState = node
    if action == 'up':
        swap = newState[(pos / 3) - 1]
        newState[(pos / 3) - 1] = 0
        newState[pos] = swap
    elif action == 'down':
        swap = newState[(pos / 3) + 1]
        newState[(pos / 3) + 1] = 0
        newState[pos] = swap
    elif action == 'left':
        swap = newState[(pos % 3) - 1]
        newState[(pos % 3) - 1] = 0
        newState[pos] = swap
    elif action == 'right':
        swap = newState[(pos % 3) + 1]
        newState[(pos % 3) + 1] = 0
        newState[pos] = swap
    return newState


def main():
    inp = parseInput("inputTest.txt")
    print(inp)
    return

main()