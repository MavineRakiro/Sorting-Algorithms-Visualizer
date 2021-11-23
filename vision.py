from tkinter import *
from tkinter import ttk
import random
from sorting_algs import bubble_sort, quick_sort, merge_sort, selection_sort


#Initializing
root =  Tk()
root.title("Sorting Algorithm Visualization.")
root.maxsize(950, 800)
root.config(bg = 'black') ###

#variables
selected_alg = StringVar()



def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 400  # units?????
    c_width = 600
    #scaling for different kinds of data(width of the bar graphs)
    x_width = c_width /len(data) + 1
    offset = 30
    spacing = 10
    normalizedData = [i /max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left of rectangle:
        x0 = i * x_width + offset + spacing
        y0 = c_height - height *340
        #Bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))


    root.update_idletasks()



def Generate():
    global data

    print("Algorithm selected: " + selected_alg.get())
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 20
    try:
        size = int(sizeEntry.get())
    except:
        size = 15
    
    if minVal < 0 : minVal = 0
    if maxVal > 100 : maxVal = 100
    if size > 20 : size = 20
    if size < 3 : size = 4

    data =[]

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['white' for x in range(len(data))])


def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, speedscale.get())
        
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedscale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedscale.get()) 

    elif algMenu.get() == 'Selection Sort':
        selection_sort(data, drawData, speedscale.get())


    drawData(data, ['green' for x in range(len(data))])


#creating user interface and canves for drawing
User_Interface = Frame(root, width=800, height=150, bg='grey')
User_Interface.grid(row=0, column=0, pady=5, padx=10)

canvas = Canvas(root, width=800, height= 400, bg='purple')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#First Row
Label(User_Interface, text="Algorithm: ", bg='grey').grid(row=0, column=0, pady=5, padx=5, sticky=W)
algMenu = ttk.Combobox(User_Interface, textvariable=selected_alg, values=['Merge Sort', 'Bubble Sort', 'Quick Sort', 'Selection Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Button(User_Interface, text="Start", command = StartAlgorithm, bg = "blue").grid(row=0, column=5, padx=5, pady=5, sticky=W )

Label(User_Interface, text="Speed", bg="purple").grid(row=0, column=3, padx=5, pady=5, sticky=W)
speedscale = Scale(User_Interface, from_= 0.1, to =2.0, length= 150, digits=2, resolution=0.2, orient=HORIZONTAL)
speedscale.grid(row=0, column=4, padx=10, pady=5, sticky=W)

#Second Row.
Label(User_Interface, text="Number of Arrays", bg = "grey").grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(User_Interface)
sizeEntry.grid(row=1, column=1, pady=5, padx=5, sticky=W)

Label(User_Interface, text = "Minimum Value", bg = "grey" ).grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(User_Interface)
minEntry.grid(row=1, column=3, pady=5, padx=5, sticky=W)

Label(User_Interface, text="Maximum Value", bg="grey").grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(User_Interface)
maxEntry.grid(row=1, column=5, pady=5, padx=5, sticky=W)

Button(User_Interface, text = 'Generate', command=Generate, bg='red').grid(row=0, column=2, pady=5, padx=5)




root.mainloop()
