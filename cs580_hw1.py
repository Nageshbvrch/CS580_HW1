# -*- coding: utf-8 -*-
"""CS_580_HW1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uhh79FKY6Jwj8iBAvZqLUtHa7KpsIxEY

$$ CS480/580 Introduction to Artificial Intelligence $$

 **$$Assignment-1 $$** 

$$ Total Points: 100 $$

$$ Due Date: 02/18/2021 $$

##The 24-puzzle problem

The 24-puzzle is a larger version of the 8-puzzle.

**Goal:**

|1|	2|	3|	4|	5|
|--|--|--|--|--|
|6	|7	|8	|9	|10|
|11	|12	|13	|14	|15|
|16	|17	|18	|19	|20|
|21|	22|	23|	24|0|	

**Initial:**

|9	|24|	3|	5|	17|
|--|--|--|--|--|
|6|	|	13|	19|	10|
|11	|21	|12	|1	|20|
|16|	4|	14|	22|	15|
|8	|18	|23	|2	|7|


For this programming assignment, you will implement the two uninformed search algorithms that find solutions to the 24-puzzle problem. You are requested to implement the programs to the 24-puzzle problem using:
1.	breadth-first search (BFS) 
2.	depth-first search (DFS)
For each of the search routines, avoid returning to states that have already been visited on the current solution path i.e., there should be no repeated states in a solution. 
CS580 only: Your programs should also be able to accept arbitrary initial states and find solutions for these states.


What to Hand in
1.	Well documented codes implementing breadth first search and depth first search. A README file should provide instructions on how to compile and execute the code.
2.	Provide the sample solutions generated by your programs using BFS and DFS.
3.	Analysis of your program. Record and compare the computational time and lengths of solutions for BFS and DFS. 
Please upload the program and the analysis report (in a zip file) on Blackboard before the assignment due date.
Hints:
1.	It is much better to model the problem of moving the blank around than moving movable tiles.
2.	Good data structure representation can make your life easy.
3.	You may want to start from the 8-puzzle problem

state  - Location of all the tiles, including blank one

parent - parent of the current state

move   - from which move did we obtain the current state

depth  - depth of current state

cost   - cost of current state

key    - decided by the heuristic function
"""

# StateMachine/State.py
# A State has an operation, and can be moved
# into the next State given an Input:

class State:
    def run(self):
        assert 0, "run not implemented"
    def next(self, input):
        assert 0, "next not implemented"

# StateMachine/stateMachine2/State.py

class State:
    def __init__(self, name): self.name = name
    def __str__(self): return self.name

class State:

    def __init__(self, state, parent, move, depth, cost, key):

        self.state = state

        self.parent = parent

        self.move = move

        self.depth = depth

        self.cost = cost

        self.key = key

        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map

#import libraries
from math import sqrt
from collections import deque
from heapq import heappush, heappop
import time


#--- Specify a goal state which will be tested to stop the program.
goalState = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0]

goalNode = State
initialState = []   #--- Initial State to be empty List
puzzleLen = 0       #--- Length of the puzzle (Eg - for 24 puzzle problem, len = 25)  
puzzleSide = 0      #--- Length of puzzleSide (Eg - for 24 puzzle problem, side = 5)

nodesExpanded = 0   #--- no of nodes expanded, will be used in the end, initial = 0
maxDepthReached = 0 #--- Length of the depth reached
maxFringeSize = 0   #--- Maximum Size of Fringe, will be used in the end, initial = 0

moves = []          #--- this keeps track of all the moves that are required to reach the goal state


"""
Function - bfs() (Breadth First Search)
    - works as a Breadth First Search algorithm.
"""
def bfs(startState):

    global goalNode, maxFringeSize, maxDepthReached
    
    visited, queue = set(), deque([State(startState, None, None, 0, 0, 0)])
    while queue:                            #--- Execute until we have elements left in queue 
        node = queue.popleft()              #--- pop the first state
        
        visited.add(node.map)               #--- Keep Track of Visited Nodes
        
        #--- Goal Test
        if node.state == goalState:
            goalNode = node
            return True, queue
        
        #--- If not a goal state then expand the node
        childNodes = expand(node)
        
        for child in childNodes:            #--- Traverse every child in the Level
            if child.map not in visited:    #--- Check if visited or not
                queue.append(child)         #--- if not visited append as a child
                visited.add(child.map)      #--- add it to the visited nodes set
                
                if child.depth > maxDepthReached:
                    maxDepthReached += 1
        
        if len(queue) > maxFringeSize:
            maxFringeSize = len(queue)
    
    #--- if search is complete and goal state not reached then return goal not found
    return False, None       
    
"""
Function - dfs() (Breadth First Search)
    - works as a Depth First Search algorithm.

"""
def dfs(startState):
    
    global goalNode, maxFringeSize, maxDepthReached
    
    visited, stack = set(), list([State(startState, None, None, 0, 0, 0)])

    while stack:                                #--- Execute until we have elements left in queue

        node = stack.pop()                      #--- pop the first state

        visited.add(node.map)                   #--- Keep Track of Visited Nodes

        if node.state == goalState:
            goalNode = node
            return True, stack

        neighbors = reversed(expand(node))      #--- reversing the order to behave as a stack(Last In First Out)

        for neighbor in neighbors:              #--- Traverse every child in the depth
            if neighbor.map not in visited:     #--- Check if visited or not
                stack.append(neighbor)          #--- if not visited append as a child
                visited.add(neighbor.map)       #--- add it to the visited nodes set

                if neighbor.depth > maxDepthReached:
                    maxDepthReached += 1

        if len(stack) > maxFringeSize:
            maxFringeSize = len(stack)
    
    #--- if search is complete and goal state not reached then return goal not found
    return False, None


   
"""
Function - expand()
    - expands the node and creates valid child nodes
    - returns all valid child nodes of the current node 
"""
def expand(node):
    global nodesExpanded
    nodesExpanded += 1
    childNodes = []
    
    #Append all the child to childNode for a valid move
    childNodes.append(State(validMove(node.state,'D'),node,'D',node.depth + 1, node.cost + 1, 0)) #--- Down
    childNodes.append(State(validMove(node.state,'L'),node,'L',node.depth + 1, node.cost + 1, 0)) #--- Left
    childNodes.append(State(validMove(node.state,'R'),node,'R',node.depth + 1, node.cost + 1, 0)) #--- Right
    childNodes.append(State(validMove(node.state,'U'),node,'U',node.depth + 1, node.cost + 1, 0)) #--- UP
    
    nodes = [child for child in childNodes if child.state]
    return nodes

"""
Function validMove()
    - validates the next move as valid or invalid
    - returns valid state if move is valid otherwise returns None
"""
def validMove(state, position):
    newState = state[:]
    index = newState.index(0) #--- get the position of blank tile
    if position == 'U':  # Up

        if index not in range(0, puzzleSide): #--- Valid iff not present in top row
            #--- Swap the empty tile with top element
            temp = newState[index - puzzleSide]
            newState[index - puzzleSide] = newState[index]
            newState[index] = temp

            return newState
        else:
            return None

    if position == 'D':  # Down
        #--- Swap the empty tile with bottom element
        if index not in range(puzzleLen - puzzleSide, puzzleLen):

            temp = newState[index + puzzleSide]
            newState[index + puzzleSide] = newState[index]
            newState[index] = temp

            return newState
        else:
            return None

    if position == 'L':  # Left

        if index not in range(0, puzzleLen, puzzleSide):

            temp = newState[index - 1]
            newState[index - 1] = newState[index]
            newState[index] = temp

            return newState
        else:
            return None

    if position == 'R':  # Right

        if index not in range(puzzleSide - 1, puzzleLen, puzzleSide):

            temp = newState[index + 1]
            newState[index + 1] = newState[index]
            newState[index] = temp

            return newState
        else:
            return None
"""
Function - get(dataList) 
    - Reads input from user and updates puzzle configuration
"""
def get(dataList):
    global puzzleLen, puzzleSide
    
    data = dataList.split(',') 
    for element in data:
        initialState.append(int(element))
    puzzleLen = len(initialState)                   #--- get the length f puzzle
    puzzleSide = int(sqrt(puzzleLen))       #--- calculate square root in order to get the length of puzzle size

"""
Function - backtrack()
"""
def backtrack():
    currentNode = goalNode
    while initialState != currentNode.state : #--- terminating condition when we reach top node from bottom 
        moves.insert(0, currentNode.move)
        currentNode = currentNode.parent
    return moves

"""
Function - output(fringe, time)
    - creates an output file with all the required elements
"""
def output(fringe, time, testNum):
    if fringe:
        
        global moves
        moves = backtrack() #--- get all the moves performed to reach the goal state
        file = open('testcase_'+str(testNum)+'.txt', 'w')
        file.write("\nProblem State : "+str(initialState))
        file.write("\npath_to_goal : " + str(moves))
        file.write("\ncost_of_path(Moves): " + str(len(moves)))
        file.write("\nnodes_expanded: " + str(nodesExpanded))
        file.write("\nfringe_size: " + str(len(fringe)))
        file.write("\nmax_fringe_size: " + str(maxFringeSize))
        file.write("\nsearch_depth: " + str(goalNode.depth))
        file.write("\nmax_search_depth: " + str(maxDepthReached))
        file.write("\nrunning_time: " + format(time, '.8f'))
        file.close()
    else :
        file = open('testcase_unsolvable.txt', 'w')
        file.write("<-- # UNSOLVABLE # -->")
        file.write("\nnodes_expanded: " + str(nodesExpanded))
        file.write("\nmax_fringe_size: " + str(maxFringeSize))
        file.write("\nmax_search_depth: " + str(maxDepthReached))
        file.write("\nrunning_time: " + format(time, '.8f'))
        file.close()

"""
Function - main() 
    - Executed everytime the python file starts.
"""
def main():
    algorithm = input('--> Please select the algorithm \
                      \n1. bfs : Breadth First Search \
                      \n2. dfs : Depth First Search \
                      \n enter the selection : ')
    
         
    data = input('--> Enter puzzle elements : ')
    
    get(data)

    function = function_map[algorithm]
    
    start = time.time()  
        
    search, fringe = function(initialState)
    
    stop = time.time()

    if not search : 
        print('<-- # UNSOLVABLE # -->')
    else : 
       output(fringe, stop-start, 'No_Solution')
        
        
function_map = {
    'bfs': bfs,
    'dfs': dfs
    }

if __name__ == '__main__':
    main()

"""## References:

[8-Puzzle](https://github.com/speix/8-puzzle-solver)






"""