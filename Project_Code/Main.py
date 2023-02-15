# Main file
from NodeClass import Node
import pandas as pd
from sys import *

def minNode(source, nodeList):
    currNode = nodeList[0]
    for node in nodeList:
        if (node.costTo(source) < currNode.costTo(source)):
            currNode = node
    return currNode

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
        exit(0)
    
    # Ask user for source node
    source = input("Please, provide the source node: ")

    # Run algorithms to find shortest paths and modify/write to data structure
    # Dijkstra's Algorithm -- Add shortest path tree!
    Nprime = [source]
    while (len(fullNetwork) != len(Nprime)):
        availableNodes = []
        for node in fullNetwork:
            if node not in Nprime:
                availableNodes.append(fullNetwork[node])
        currNode = minNode(source, availableNodes)
        Nprime.append(currNode.name)
        for node in currNode.network:
            if currNode.costTo(node) < 999 and currNode.costTo(node) != 0 and node not in Nprime:
                fullNetwork[source].setCost(node, min(
                    fullNetwork[source].costTo(node),
                    (fullNetwork[source].costTo(currNode.name) + currNode.costTo(node))
                ))

    # Output Dijsktra's results
    print("Shortest path tree for node {}:".format(source))
    print()
    print("Costs of the least-cost paths for node {}:".format(source))
    print(fullNetwork[source])
    print()

    # Calculate distance vectors for each node
    # Bellman-Ford equation
    for node in fullNetwork:
        for node1 in fullNetwork[node].network:
            print(fullNetwork[node].costTo(node1))

    # Print distance vectors for each node
    for node in fullNetwork:
        print("Distance vector for node {}:".format(node))
        for node1 in fullNetwork[node].network:
            print(fullNetwork[node].costTo(node1))
        

else:
    print("Usage: python {} <CSV filename>\n".format(argv[0]))
    exit(0)