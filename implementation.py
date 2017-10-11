"""
    F29AI - Artificial Intelligence and Intelligent Agents
    Coursework - Part I - A* Search

    Sample code from http://www.redblobgames.com/pathfinding/
    Copyright 2014 Red Blob Games <redblobgames@gmail.com>

    Feel free to use this code in your own projects, including commercial projects
    License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>
    !/usr/bin/env python
    -*- coding: utf-8 -*

    This code contains values for our wall and trap positions and allows us to build
    the robot paths as well as build and display the grid.

    Edited by: Ronan Smith & Jamie McCulloch
    Last edited: 01.11.2016
"""
import collections

number = 2
length = 12
height = 10

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

# utility functions for dealing with square grids
def from_id_width(id, width):
    return (id % width, id // width)

def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    for i in range(number):
        if id in graph.robots: r = "R"+str(graph.robots.index(id))
        if id in graph.goals: r = "G"+str(graph.goals.index(id))
    if id in graph.walls: r = "#" #* width
    if id in graph.weights: r="T"
    return r

def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end = "")
        print()


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.robots = []
        self.goals = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return diagram4.weights.get(to_node, 1)

diagram4 = GridWithWeights(length, height)
# insert wall and trap locations here
diagram4.walls = [(0,0), (3,1), (4,1), (5,1), (6,1), (7,1), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (7,7), (6,7), (5,7), (4,7)]
diagram4.weights = {trap: 5 for trap in [(1,5), (6,9), (7,0), (10,6)]}

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

from collections import OrderedDict

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    #path.append(start) # optional
    path.reverse() # optional
    print("The path taken by the robot is: ", list(OrderedDict.fromkeys(path)))
    return path
