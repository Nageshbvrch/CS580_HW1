# -*- coding: utf-8 -*-
"""CS580_HW1_Draft.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cke4RIJ2wuBYaJkwlEXOq_0sOxf1fWzz
"""

import argparse
import time
import timeit
from collections import deque


#Information *****************************************************
class PuzzleState:
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
    def __str__(self):
        return str(self.map)    

#Global variables***********************************************
GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
GoalNode = None # at finding solution
NodesExpanded = 0 #total nodes visited
MaxSearchDeep = 0 #max deep
MaxFrontier = 0 #max frontier


#BFS**************************************************************
def bfs(startState):

    global MaxFrontier, GoalNode, MaxSearchDeep

    boardVisited= set()
    Queue = deque([PuzzleState(startState, None, None, 0, 0, 0)])

    while Queue:
        node = Queue.popleft()
        boardVisited.add(node.map)
 
        if node.state == GoalState:
            GoalNode = node
            return Queue
        posiblePaths = subNodes(node)
        for path in posiblePaths:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Queue) > MaxFrontier:
            QueueSize = len(Queue)
            MaxFrontier = QueueSize
        
            

def dfs(startState):

    global MaxFrontier, GoalNode, MaxSearchDeep

    boardVisited = set()
    stack = list([PuzzleState(startState, None, None, 0, 0, 0)])
    while stack:
        node = stack.pop()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return stack
        #inverse the order of next paths for execution porpuses
        posiblePaths = reversed(subNodes(node))
        for path in posiblePaths:
            if path.map not in boardVisited:
                stack.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = 1 + MaxSearchDeep
        if len(stack) > MaxFrontier:
            MaxFrontier = len(stack)
    
#Obtain Sub Nodes********************************************************
def subNodes(node):

    global NodesExpanded
    NodesExpanded = NodesExpanded+1

    nextPaths = []
    nextPaths.append(PuzzleState(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    nodes=[]
    for procPaths in nextPaths:
        if(procPaths.state!=None):
            nodes.append(procPaths)
    return nodes

#Next step**************************************************************
def move(state, direction):
    #generate a copy
    newState = state[:]
    
    #obtain poss of 0
    index = newState.index(0)
    


    if (index in [6, 7, 8, 11, 12, 13, 16, 17, 18]):
        if(direction==1):
            temp=newState[index]
            newState[index]=newState[index - 5]
            newState[index - 5]=temp
        if(direction==2):
            temp=newState[index]
            newState[index]=newState[index + 5]
            newState[index + 5]=temp
        if(direction==3):
            temp=newState[index]
            newState[index]=newState[index - 1]
            newState[index - 1]=temp
        if(direction==4):
            temp=newState[index]
            newState[index]=newState[index + 1]
            newState[index + 1]=temp
        return newState
    if index in [1, 2, 3]:
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[index]
            newState[index]=newState[index + 5]
            newState[index + 5]=temp
        if(direction==3):
            temp=newState[index]
            newState[index]=newState[index - 1]
            newState[index - 1]=temp
        if(direction==4):
            temp=newState[index]
            newState[index]=newState[index + 1]
            newState[index + 1]=temp
        return newState    
    if index in [9, 14, 19]:
        if(direction==1):
            temp=newState[index]
            newState[index]=newState[index - 5]
            newState[index - 5]=temp
        if(direction==2):
            temp=newState[index]
            newState[index]=newState[index + 5]
            newState[index + 5]=temp
        if(direction==3):
            temp=newState[index]
            newState[index]=newState[index - 1]
            newState[index - 1]=temp
        if(direction==4):
            return None
        return newState
    if index in [21, 22, 23]:
        if(direction==1):
            temp=newState[index]
            newState[index]=newState[index - 5]
            newState[index - 5]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[index]
            newState[index]=newState[index - 1]
            newState[index - 1]=temp
        if(direction==4):
            temp=newState[index]
            newState[index]=newState[index + 1]
            newState[index + 1]=temp
        return newState
    if index in [5, 10, 15]:
        if(direction==1):
            temp=newState[index]
            newState[index]=newState[index - 1]
            newState[index - 1]=temp
        if(direction==2):
            temp=newState[index]
            newState[index]=newState[index + 5]
            newState[index + 5]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[index]
            newState[index]=newState[index + 1]
            newState[index + 1]=temp
        return newState
    if index == 0:
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[0]
            newState[0]=newState[5]
            newState[5]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[0]
            newState[0]=newState[1]
            newState[1]=temp
        return newState  
    if index == 4:
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[4]
            newState[4]=newState[5]
            newState[5]=temp
        if(direction==3):
            temp=newState[4]
            newState[4]=newState[3]
            newState[3]=temp
        if(direction==4):
            return None
        return newState
    if index == 20:
        if(direction==1):
            temp=newState[20]
            newState[20]=newState[15]
            newState[15]=temp
        if(direction==2):
            return None
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[20]
            newState[20]=newState[21]
            newState[21]=temp
        return newState
    if index == 24:
        if(direction==1):
            temp=newState[24]
            newState[24]=newState[19]
            newState[19]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[24]
            newState[24]=newState[23]
            newState[23]=temp
        if(direction==4):
            return None
        return newState
        
#MAIN**************************************************************
def main():

    global GoalNode

    #a = [1,8,2,3,4,5,6,7,0]
    #point=Heuristic(a)
    #print(point)
    #return
    
    #info = "6,1,8,4,0,2,7,3,5" #20
    #info = "8,6,4,2,1,3,5,7,0" #26
    
    #Obtain information from calling parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('method')
    parser.add_argument('initialBoard')
    args = parser.parse_args()
    data = args.initialBoard.split(",")

    #Build initial board state
    InitialState = []
    InitialState.append(int(data[0]))
    InitialState.append(int(data[1]))
    InitialState.append(int(data[2]))
    InitialState.append(int(data[3]))
    InitialState.append(int(data[4]))
    InitialState.append(int(data[5]))
    InitialState.append(int(data[6]))
    InitialState.append(int(data[7]))
    InitialState.append(int(data[8]))
    InitialState.append(int(data[9]))
    InitialState.append(int(data[10]))
    InitialState.append(int(data[11]))
    InitialState.append(int(data[12]))
    InitialState.append(int(data[13]))
    InitialState.append(int(data[14]))
    InitialState.append(int(data[15]))
    InitialState.append(int(data[16]))
    InitialState.append(int(data[17]))
    InitialState.append(int(data[18]))
    InitialState.append(int(data[19]))
    InitialState.append(int(data[20]))
    InitialState.append(int(data[21]))
    InitialState.append(int(data[22]))
    InitialState.append(int(data[23]))
    InitialState.append(int(data[24]))

    #Start operation
    start = timeit.default_timer()

    function = args.method
    if(function=="bfs"):
        bfs(InitialState)
    if(function=="dfs"):
        dfs(InitialState)  

    stop = timeit.default_timer()
    time = stop-start

    #Save total path result
    deep=GoalNode.depth
    moves = []
    while InitialState != GoalNode.state:
        if GoalNode.move == 1:
            path = 'Up'
        if GoalNode.move == 2:
            path = 'Down'
        if GoalNode.move == 3:
            path = 'Left'
        if GoalNode.move == 4:
            path = 'Right'
        moves.insert(0, path)
        GoalNode = GoalNode.parent

    #'''
    #Print results
    print("path: ",moves)
    print("cost: ",len(moves))
    print("nodes expanded: ",str(NodesExpanded))
    print("search_depth: ",str(deep))
    print("MaxSearchDeep: ",str(MaxSearchDeep))
    print("running_time: ",format(time, '.8f'))
    #'''

    #Generate output document for grade system
    #'''
    file = open('output.txt', 'w')
    file.write("path_to_goal: " + str(moves) + "\n")
    file.write("cost_of_path: " + str(len(moves)) + "\n")
    file.write("nodes_expanded: " + str(NodesExpanded) + "\n")
    file.write("search_depth: " + str(deep) + "\n")
    file.write("max_search_depth: " + str(MaxSearchDeep) + "\n")
    file.write("running_time: " + format(time, '.8f') + "\n")
    file.close()
    #'''

if __name__ == '__main__':
    main()