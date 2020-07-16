#Question1
#Define a function DotProduct(N, ListA, ListB) that takes 2 lists, ListA and ListB integers, each of size N,
#interpreted as a 1-dimensional arrays and returns the dot product of ListA and ListB

import numpy as um
import random
def DotProduct():
    ListA = []
    ListB = []
    N = int(input("Enter the size you want the list to be: "))
    
    for i in range(0,N):
        ListA.append(random.randint(1,1000))
        ListB.append(random.randint(1,1000))
        
    print(ListA)
    print(ListB)
    si = um.dot(ListA,ListB)
    print(si)

DotProduct()


