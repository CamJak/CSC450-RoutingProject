# Main file
from NodeClass import Node
import pandas as pd
from sys import *

# Import CSV data and convert into Node objects
if (len(argv) == 2):
    filename = argv[1]

    try:
        df = pd.read_csv(r"{}".format(filename))
        df.dropna()

        # Create data structure to hold full network data (this is what the routing function will access and modify)
        fullNetwork = []
        # Iterrate through rows in CSV and create node objects
        for i, j in df.iterrows():
            nodeName = str(j[0])
            currNetwork = {}
            for x in range(1, len(j)):
                currNetwork[j.index[x]] = j[x]
            newNode = Node(nodeName, currNetwork)
            fullNetwork.append(newNode)
    except Exception:
        print("Error reading file...")
    
    # Run algorithms to find shortest paths and modify/write to data structure

    # Output data structure (?)


else:
    print("Usage: python {} <filename>\n".format(argv[0]))
    exit(0)