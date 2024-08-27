from tkinter import *
import matplotlib.pyplot as plt

def plot(valx,valy,labelx = "label",labely = "label"):
    #reste de la fonction a faire
    plt.axis((min(valx),max(valx),min(valy),max(valy)))
    plt.plot(valx,valy)
    plt.show()

def savepoint():
    listofval.append(entryForPoint.get())
    listofxval,listofyval = []
    for i in range(len(listofval)):
        listofxval.append(listofval[i][0])
        listofyval.append(listofval[i][1])

def getlabel():
    global labelx,labely
    labelx = entryForLabelx.get()
    labely = entryForLabely.get()


listofxval = []
listofyval = []
listofval = []

window = Tk()

window.geometry("1920x1080")
window.title("plot graph app")
window.iconphoto(True,PhotoImage(file="C:\\Users\\lopib\Downloads\\117-1170352_line-graph-graph-icon-png-free-transparent-png.png"))
plotButton = Button(master=window,text="plot",command=plot(listofxval,listofyval,labelx,labely))
savePointButton = Button(master=window,text="new point",command=savepoint)
savelabels = Button(master=window,text ="save labels",command=getlabel)
entryForPoint = Entry(master=window)
entryForLabelx = Entry(master=window)
entryForLabely = Entry(master=window)

plotButton.pack()
entryForPoint.pack()
entryForLabelx.pack()
entryForLabely.pack()
savelabels.pack()
savePointButton.pack()

window.mainloop()