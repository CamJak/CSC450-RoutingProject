import pandas as pd
from sys import *

if (len(argv) == 2):
    filename = argv[1]

    print("Filename: {}".format(filename))

    try:
        df = pd.read_csv(r"{}".format(filename))
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
    except Exception:
        print("Error reading file...")

else:
    print("Usage: python {} <filename>\n".format(argv[0]))
    exit(0)

    
