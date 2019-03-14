import numpy as np

n = int(input("enter a number: "))
i = 0
l = 0
b = 0
while i < n:
    tempRand=np.random.random()
    if tempRand < .50:
        l += 1
    else:
        b += 1
    i+=1
    print(tempRand)
print("Results: " + "{0:.1f}".format((l/(l+b))*100) + "% were [0.0-0.5]. " + "{0:.1f}".format((b/(l+b))*100) + "% were (0.5-1.0]")
