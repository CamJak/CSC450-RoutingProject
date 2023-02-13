# Node class for defining and operating with nodes on our network topography
class Node:
    def __init__(self, name, network):
        self.name = name            # This is the name of the node ("u","v",etc.)
        self.network = network      # This is a dictionary where the keys are node names ("u","v",etc.) and values are costs (1,20,9999,etc.)

    def __str__(self):
        outputString = ""
        for item in self.network:
            outputString += (item + ":" + str(self.network[item]) + ", ")
        return outputString[:-2]   # Returns created string put cuts off extra comma

    # Gives the cost from this node to others on the network
    # This will be altered by the routing algorithm
    def costTo(self, node):
        return self.network[node]

    # Set the cost to specified node from this node
    def setCost(self, node, cost):
        self.network[node] = cost

