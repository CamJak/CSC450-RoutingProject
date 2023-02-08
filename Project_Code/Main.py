# Main file
from NodeClass import Node 

# Some sample code showing how the Node class works

network1 = {
    "u":0,
    "v":1,
    "w":5
}
u = Node("u", network1)

print(u)
print(u.costTo("v"))

## Skeleton of what our code should look like ##

# Import CSV data and convert into Node objects

# Create data structure to hold full network data (this is what the routing function will access and modify)
# fullNetwork = {
#     "u": u,
#     "v": v,
#     "w": w,
#     "x": x,
#     "y": y
# }

# Run algorithms to find shortest paths and modify/write to data structure

# Output data structure (?)
