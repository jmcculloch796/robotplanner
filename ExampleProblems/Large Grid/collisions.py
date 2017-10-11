"""
    F29AI - Artificial Intelligence and Intelligent Agents
    Coursework - Part I - A* Search

    Collisions. This file deals with the problems that arise when
    generating a new random node for the goal or the robot starting
    point.

    Ronan Smith & Jamie McCulloch
    Last edited: 18.10.2016
"""
from implementation import *
from a_star import *
from nodes import *

"""
    Deals with random nodes that have been created either inside
    a wall or inside a trap.
    Params: robot_node, goal_node
"""
def wallspawn(robot_node, goal_node):
    if ((robot_node) in diagram4.walls):
        print("The robot spawned in a wall ", robot_node, ", generating new starting node...")
        robot_node = nodeGenerator(length, height)
        return robot_node

    if((goal_node) in diagram4.walls):
        print("The goal spawned in a wall ", goal_node, ", generating a new goal node...")
        goal_node = goalGenerator(length, height, robot_node)
        return goal_node

    if((robot_node) in diagram4.weights):
        print("the robot spawned in a trap ", robot_node, ", generating a new robot node...")
        robot_node = nodeGenerator(length, height)
        return robot_node

    if((goal_node) in diagram4.weights):
        print("the goal spawned in a trap", goal_node, ", generating a new goal node...")
        goal_node = goalGenerator(length, height, robot_node)
        return goal_node

#def robocollision(robot1list, robot2list):
