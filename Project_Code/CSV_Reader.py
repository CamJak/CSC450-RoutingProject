import pandas as pd

df = pd.read_csv(r"/home/blake/Desktop/CSC450 Project/topology-1.csv")
df.dropna()
print(df)

for i, j in df.iterrows():
    print("I = " + str(i))
    
    n = 0
    for stuff in j:
        if n == 0:
            print("Distance from {} to...".format(stuff))
        if n == 1:
            print("U: " + str(stuff))
        if n == 2: 
            print("V: " + str(stuff))
        if n == 3: 
            print("W: " + str(stuff))
        if n == 4: 
            print("X: " + str(stuff))        
        if n == 5: 
            print("Y: " + str(stuff))
        if n == 6: 
            print("Z: " + str(stuff))
        n += 1
