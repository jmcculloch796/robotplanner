"""
    F29AI - Artificial Intelligence and Intelligent Agents
    Coursework - Part I - A* Search

    Example Problem 1. This file models the first example
    problem we were given as described in our submission
    document.

    Ronan Smith & Jamie McCulloch
    Last edited: 10.11.2016
"""

from implementation import *
from nodes import *
from a_star import *
from collisions import *

"""
    Print a newline.
"""
def nl():
    print("\n")

"""
    The main method.
"""
def main():
    #for choosing the no of robots from command line
    # remember to uncomment random generators below
    #noOfRobots = int(input("How many robots would you like? "))
    #print("")

    #robots = [None] * noOfRobots
    #goals = [None] * noOfRobots
    #paths = [None] * noOfRobots
    # -----------------------------------------------------

    # for manually entering no of robots.
    noOfRobots = 2

    robots = [None] * noOfRobots
    goals = [None] * noOfRobots
    paths = [None] * noOfRobots

    # for manually choosing the robots starting and goal positions.
    # remember to comment out random generators below.
    robots[0] = (0,0)   #R0
    robots[1] = (6,4)   #R1
    goals[0] = (5,2)    #G0
    goals[1] = (2,0)    #G1
    # -----------------------------------------------------

    for i in range(noOfRobots):
        #robots[i] = nodeGenerator(length, height)
        while ((robots[i]) in diagram4.walls) or ((robots[i]) in diagram4.weights):
            robots[i] = wallspawn(robots[i], goals[i])
        print("The start for robot R", i, " is ", (robots[i]))
        #goals[i] = goalGenerator(length, height, robots[i])
        while ((goals[i]) in diagram4.walls or (goals[i]) in diagram4.weights):
            goals[i] = wallspawn(robots[i], goals[i])
            nl()
        print("The goal for R", i, ", G", i, " is ", goals[i])
        came_from, cost_so_far, paths[i] = a_star_search(diagram4, noOfRobots, start=(robots[i]), goal=(goals[i]))
        #paths[i] = reconstruct_path(came_from, robots[i], goals[i])
        print("-------------------------------------------------------------")
        diagram4.robots.append((robots[i]))
        diagram4.goals.append((goals[i]))
    draw_grid(diagram4, width=4, point_to=came_from)
    nl()
    collisionChecker(paths)
    print("-------------------------------------------------------------")

"""
    Checks for collisions in the paths.
"""
def collisionChecker(p):
    collisionFound = False
    for i in range(0,len(p)):
        for j in range(0,len(p[i][:-1])):
            for k in range(0,len(p[i][:-1])):
                if(i == k):
                    break
                if (i > len(p[k])):
                    break
                elif(p[i][j] == p[k][j]):
                    print("Collision between R",k,"and R",i, "at",p[i][j],".")
                    print("These two Robots must travel at seperate times.")
                    collisionFound = True
    if(collisionFound == False):
        print("No collisions found on these paths.")
        print("The robots can travel simultaneously. ")
    return collisionFound


"""
    Tells Python interpreter to run the main method first.
"""
if __name__ == '__main__':
    main()
