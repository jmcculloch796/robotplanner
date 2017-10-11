"""
    F29AI - Artificial Intelligence and Intelligent Agents
    Coursework - Part I - A* Search

    The A* search algorithm. This file also contains heuristic
    functions for Manhatton Distance and Euclidean 'straight
    line' distance.
    Much of this code has been adapted from: http://www.redblobgames.com/

    Ronan Smith & Jamie McCulloch
    Last edited: 31.10.2016
"""
from implementation import *
import math

"""
    Euclidean distance. Calculates a 'straight line' distance
    to the goal. Less efficient for A* search when movement is
    only allowed in four directions.
    Params: s (start), g (goal/next).
"""
def heuristicE(s, g):
    (x1, y1) = s
    (x2, y2) = g

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    result = (dx * dx) + (dy * dy)
    rootResult = math.sqrt(result)

    return rootResult

"""
    Manhattan Distance on a square grid.
    Params: a (current node), b (next node).
"""
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    return (dx + dy)

"""
    The A* search algorithm.
"""
def a_star_search(graph, noRobots, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    paths = [None] * noRobots
    i = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(current, next)
                frontier.put(next, priority)
                came_from[next] = current
    print("The cost for this journey was ", cost_so_far[current], " units of energy.")
    paths[i] = reconstruct_path(came_from, start, goal)
    return came_from, cost_so_far, paths[i]
