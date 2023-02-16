# Main file
from NodeClass import Node
import pandas as pd
from sys import *
from copy import deepcopy

# Function definitions
# Finds the node in a list with least cost to source
def minNode(source, nodeList):
    currNode = nodeList[0]
    for node in nodeList:
        if (node.costTo(source) < currNode.costTo(source)):
            currNode = node
    return currNode

def minCost(source, dest):
    leastCost = source.costTo(dest.name)
    for node in source.network:
        if ((source.costTo(node) +  dest.costTo(node)) < leastCost):
            leastCost = (source.costTo(node) + dest.costTo(node))
    return leastCost

# Calculates the shortest path nodes by tracing the predecessor nodes for entire network
# Returns results as an array of paths
def shortestPath(network, source, Nprime):
    resultArray = []
    for node in Nprime:
        if node != source:
            result = node
            while node != source:
                if network[node].predecessor != source:
                    result = network[node].predecessor + result
                    node = network[node].predecessor
                else:
                    result = source + result
                    break
            resultArray.append(result)
    return resultArray


# Import CSV data and convert into Node objects (using pandas)
if (len(argv) == 2):
    filename = argv[1]

    try:
        df = pd.read_csv(r"{}".format(filename))
        df.dropna()

        # Create data structure to hold full network data (this is what the routing function will access and modify)
        fullNetwork = {}
        # Iterrate through rows in CSV and create node objects
        for i, j in df.iterrows():
            nodeName = str(j[0])
            currNetwork = {}
            for x in range(1, len(j)):
                currNetwork[str(j.index[x])] = j[x]
            newNode = Node(nodeName, currNetwork)
            fullNetwork[str(j[0])] = newNode
    except Exception:
        print("Error reading file...")
        exit(0)
    
    # Make two copies of fullNetwork
    networkDijkstra = deepcopy(fullNetwork)
    networkBellman = deepcopy(fullNetwork)

    # Ask user for source node
    source = input("Please, provide the source node: ")

    # Run algorithms to find shortest paths and modify/write to data structure
    # Dijkstra's Algorithm -- Add shortest path tree!
    # initialize N-prime
    Nprime = [source]
    # Set all predecessors to source to start
    for node in networkDijkstra:
        networkDijkstra[node].predecessor = source
    # While not all nodes are in N-prime
    while (len(networkDijkstra) != len(Nprime)):
        availableNodes = []
        # Make list of nodes not in N-prime
        for node in networkDijkstra:
            if node not in Nprime:
                availableNodes.append(networkDijkstra[node])
        # Set "current node" to node with minimum cost to source
        currNode = minNode(source, availableNodes)
        # Add "current node" to N-prime
        Nprime.append(currNode.name)
        # Check all other nodes in network
        for node in currNode.network:
            # If node is adjacent to "current node" and not in N-prime 
            if currNode.costTo(node) < 999 and currNode.costTo(node) != 0 and node not in Nprime:
                possCost = networkDijkstra[source].costTo(currNode.name) + currNode.costTo(node)
                # If the cost using this "current node" is cheaper than current cost update it
                if possCost < networkDijkstra[source].costTo(node):
                    networkDijkstra[source].setCost(node, possCost)
                    networkDijkstra[node].predecessor = currNode.name

    # Output Dijsktra's results
    print("Shortest path tree for node {}:".format(source))
    print(shortestPath(networkDijkstra, source, Nprime))
    print("Costs of the least-cost paths for node {}:".format(source))
    print(networkDijkstra[source])
    print()

    # Calculate distance vectors for each node
    # Bellman-Ford equation
    for node in networkBellman:
        for node1 in networkBellman[node].network:
            leastCost = minCost(networkBellman[node], networkBellman[node1])
            networkBellman[node].setCost(node1, leastCost)

    # Print distance vectors for each node
    for node in networkBellman:
        print("Distance vector for node {}:".format(node), end=" ")
        for node1 in networkBellman[node].network:
            print(networkBellman[node].costTo(node1), end=" ")
        print()

else:
    print("Usage: python {} <CSV filename>\n".format(argv[0]))
    exit(0)