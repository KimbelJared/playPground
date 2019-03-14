import numpy as np
import sys

#Collect the userInput
print("Enter the information of Matrix[1]")
m1_r = int(input("Rows: "))
m1_c = int(input("Columns: "))

print("Enter the information of Matrix[2]")
m2_r = int(input("Rows: "))
m2_c = int(input("Columns: "))

#Test for invalid Matrix
if m1_r != m2_c:
    print("Error M1 Rows not equal to M2 Columns")
    sys.exit()
