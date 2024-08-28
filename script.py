from tkinter import *
import matplotlib.pyplot as plt
#----------
def plotf():
    plt.plot(tupleofvalx,tupleofvaly)
    plt.show()

def savepoint():
    global tupleofvalx,tupleofvaly
    listofvalx = entryForPointx.get()
    tupleofvalx = list()
    for i in listofvalx:
        if i.isnumeric():
            tupleofvalx.append(int(i))
    tupleofvalx = tuple(tupleofvalx)

    listofvaly = entryForPointy.get()
    tupleofvaly = list()
    for i in listofvaly:
        if i.isnumeric():
            tupleofvaly.append(int(i))
    tupleofvaly = tuple(tupleofvaly)

def getlabel():
    global labelx,labely
    plt.xlabel(entryForLabelx.get())
    plt.ylabel(entryForLabely.get())
tupleofvalx = ()
listofvalx = []
tupleofvaly = ()
listofvaly = []
#----------
window = Tk()

window.geometry("400x300")
window.title("plot graph app")
window.iconphoto(True,PhotoImage(file="C:\\Users\\lopib\Downloads\\117-1170352_line-graph-graph-icon-png-free-transparent-png.png"))
plotButton = Button(master=window,text="plot",command=plotf)
savePointButton = Button(master=window,text="new point",command=savepoint)
savelabels = Button(master=window,text ="save labels",command=getlabel)
labelbuttonpx = Label(text="enter the list of the x coordinates")
entryForPointx = Entry(master=window)
labelbuttonpy = Label(text="enter the list of the y coordinates")
entryForPointy = Entry(master=window)
labelbuttonlx = Label(text="enter the x label")
entryForLabelx = Entry(master=window)
labelbuttonly = Label(text="enter the y label")
entryForLabely = Entry(master=window)

plotButton.pack()
labelbuttonpx.pack()
entryForPointx.pack()
labelbuttonpy.pack()
entryForPointy.pack()
labelbuttonlx.pack()
entryForLabelx.pack()
labelbuttonly.pack()
entryForLabely.pack()
savelabels.pack()
savePointButton.pack()

window.mainloop()
#-------------