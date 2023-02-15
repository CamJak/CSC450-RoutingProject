# Main file
from NodeClass import Node
import pandas as pd
from sys import *

# Function definitions
# Finds the node in a list with lest cost to source
def minNode(source, nodeList):
    currNode = nodeList[0]
    for node in nodeList:
        if (node.costTo(source) < currNode.costTo(source)):
            currNode = node
    return currNode

# Updates the list of node links by replacing outdated links if needed
def updateLinks(links, source, dest):
    for i in range(len(links)):
        if links[i][1] == dest:
            links[i] = (source, dest)
            return links
    links.append((source, dest))
    return links

# Outputs the shortest path tree given a base tree and list of node links
def pathTree(fullTree, links):
    finishedTree = []
    for i in range(len(fullTree)):
        print("temp")  # Finish later
    return finishedTree


# Import CSV data and convert into Node objects
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
    
    # Make two copies of fullNetwork
    networkDijkstra = fullNetwork.copy()
    networkBellman = fullNetwork.copy()

    # Ask user for source node
    source = input("Please, provide the source node: ")

    # Run algorithms to find shortest paths and modify/write to data structure
    # Dijkstra's Algorithm -- Add shortest path tree!
    # initialize N-prime
    Nprime = [source]
    fullTree = []
    links = []
    # While not all nodes are in N-prime
    while (len(networkDijkstra) != len(Nprime)):
        availableNodes = []
        currTree = source
        # Make list of nodes not in N-prime
        for node in networkDijkstra:
            if node not in Nprime:
                availableNodes.append(networkDijkstra[node])
        # Set "current node" to node with minimum cost to source
        currNode = minNode(source, availableNodes)
        # Add "current node" to N-prime
        Nprime.append(currNode.name)
        currTree += currNode.name
        # Check all other nodes in network
        for node in currNode.network:
            # If node is adjacent to "current node" and not in N-prime 
            if currNode.costTo(node) < 999 and currNode.costTo(node) != 0 and node not in Nprime:
                possCost = networkDijkstra[source].costTo(currNode.name) + currNode.costTo(node)
                # If the cost using this "current node" is cheaper than current cost update it
                if possCost < networkDijkstra[source].costTo(node):
                    networkDijkstra[source].setCost(node, possCost)
                    links = updateLinks(links, currNode.name, node)
        fullTree.append(currTree)

    # Output Dijsktra's results
    print("Shortest path tree for node {}:".format(source))
    print(pathTree(fullTree, links))
    print("Costs of the least-cost paths for node {}:".format(source))
    print(networkDijkstra[source])
    print()

    # Calculate distance vectors for each node
    # Bellman-Ford equation

    # Print distance vectors for each node
    for node in fullNetwork:
        print("Distance vector for node {}:".format(node))

else:
    print("Usage: python {} <CSV filename>\n".format(argv[0]))
    exit(0)