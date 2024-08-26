import matplotlib.pyplot as plt
import tkinter as tk

#listOfData = list(input("enter a list of data(the format should be [[x component , y component]...]) :  "))
listOfData = [[1,1],[1,2],[2,3]]
labelY = input("enter the y label : ")
labelX = input("enter the x label : ")

listOfxValues = [i[0] for i in listOfData]
listOfyValues = [i[1] for i in listOfData]

plt.ylabel(labelY)
plt.xlabel(labelX)
plt.axis((0,max(listOfxValues),0,max(listOfyValues)))
plt.plot(listOfData)
plt.show()
