import random as rand
from tkinter import END

color = "null"

def main() :
    go = "y"
    if(go== "y"):
        #color = "null"
        random = rand.randint(0,9)
        if(random in (0,1,2,3,4)):
            color = "red"
        elif(random in (5,6,7)):
            color = "yellow"
        elif(random in (8,9)):
            color = "blue"
        return(color)
        go = "n"
        color = "null"

mylist=[]
for x in range(1000000):
    mylist.append(main())

print("red",mylist.count("red"))
print("yellow",mylist.count("yellow"))
print("blue",mylist.count("blue"))