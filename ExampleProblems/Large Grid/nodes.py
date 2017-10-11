
"""
	F29AI - Artificial Intelligence and Intelligent Agents
	Coursework - Part I - A* Search

	Code to create node values for the robot start point
	and for the goal.

	Ronan Smith & Jamie McCulloch
	Last edited: 18.10.2016
"""
from random import randint

"""
	Creates a random node to be the robot's starting point.
	This method takes the grid's width and height as
	parameters.
"""
def nodeGenerator(width, height):
	randomheight = randint(0, (height-1))
	randomwidth = randint(0,(width-1))

	robot_node = (randomwidth, randomheight)
	return robot_node

"""
	Generates a random node to be the goal for a specific robot.
	The grid width and height are parameters along with the robot
	which will be assigned to this goal.
"""
def goalGenerator(width, height, robot_node):

	randomwidth = randint(0,(width-1))
	randomheight = randint(0, (height-1))

	goal_node = (randomwidth, randomheight)
	if (goal_node == robot_node):
		print("The goal generated was the same as the robot's starting node, a new goal has been created")
		newrandomheight = randint(0, (height-1))
		newrandomwidth = randint(0,(width-1))
		goal_node = (newrandomwidth, newrandomheight)
	return goal_node
