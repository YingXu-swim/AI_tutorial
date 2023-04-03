This exercise is about transition system models that are central in many parts of AI and also common in other areas of computer science, including computer-aided verification and validation.

A basic transition system model consists of

* a set of states, and

* a transition relation that associates with each state zero or more successor states.

This type of model could be viewed as a directed graph, with the states coinciding with the nodes of the graph, and the elements of the transition relation corresponding to the (directed) arcs of the graph.

More advanced transition system models could associate probabilities between the difference successor state of a state, or have multiple transition relations, each corresponding to a different action possible for the decision-maker, with each action associating alternative successor states for each state.

In this exercise, we formalize the movements of the Pac-Man character from the 1980 video game. The states of the transition system represent the different locations in the maze Pac-Man moves in as well as the direction it is currently moving. The following rules govern Pac-Man’s movement.

If there is an empty grid cell in the direction of movement, then Pac-Man can move to that cell.

If there is an empty grid cell to the left of the current location (considering the current direction of movement), then Pac-Man can move to that cell and change the direction of movement 90 degrees to the left.

Turning right is similarly possible.

If no movement forward, left or right is possible, then Pac-Man moves one step backward and turns 180 degrees to the direction it came from.

Your task is to implement this Pac-Man behavior in the code template, and to test that it works with the given code. The code allows you to find all states that are reachable from a given initial state, as well as to find shortest paths between given two states. This path would tell you how to reach a given goal from a given starting state, representing a simple form of sequential decision-making, where a sequence of decision about the next actions has to be taken to satisfy a given objective.
