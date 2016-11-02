import tkinter 

		# run 'python -m tkinter' on the command line to see if tkinter is set up properly
		# 	 - this should bring up a little frame with a click me button on it
		#    - if it doesn't run, you may need to install the TK software manually. 
		#		- i had to install it on my computer, but im not sure about windows/mac
		#		- I believe you can get the activetcl distro from activestate.com which should work
import xlrd

from writeClassFile import writeFile
from tkinter import filedialog
from functools import partial

""" 
	This tool provides a GUI to create python class files

	see the README for usage instructions
"""

top = tkinter.Tk()

# set the window size for page 1
top.minsize(300,200);
top.maxsize(300,200);



filename = ''

#runs when you click the 'open file...' button. Used to get the filename. 
#also does some parsing by removing the absolute filepath and the .xlsx part. 
	#this parsed value is set as the default for the tableName entry field
def openFileCallback() :
    	
	global filename
	filename = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
	print(filename)
	strings = filename.split('/')
	filenameNoAbs = ''
	for item in strings :
		filenameNoAbs = item

	filenameNoAbs = filenameNoAbs.split('.')[0]
	e.insert(0, filenameNoAbs)

tableName = ''

# goes to the next page when you click 'next'
def nextCallback() : #hide the page 1 widgets, show the page 2 widgets
	b.pack_forget()
	global tableName
	tableName = e.get()
	e.pack_forget()
	nextButton.pack_forget()

	top.minsize(1000,700);
	top.maxsize(1000,700);
	bottomButtons.pack(side="bottom")


	createButtons() # parses the XLSX file and creates the tkinter.Button() objects
	leftside.pack(side="left", fill="both")
	middle.pack(side="left", fill="both")
	rightside.pack(side="left", fill="both")

#note about pack()
	# this is basically used in tkinter to place a widget (button, label, entry field) on screen
	# I'm using tkinter Frames to hold these widgets throughout

	#pack can take arguments:
		# (side = "left") aligns to the left, and goes sequentially
			#i.e. leftside is put on the left, then middle is put beside leftside, then rightside is put beside middle
		# (fill = <value>) is used to expand the contents of the widget to the edge of the container
			#"both" means x & y, but you can do just "x" for example


#This is the Open File... button. Runs openFileCallback() on press
b = tkinter.Button(top, text = "Open File...", command = openFileCallback)
b.pack()
#doing some background color hacking here. pay no attention
defaultactivebg = b.cget('activebackground')


#this is the entry field for Table Name
e = tkinter.Entry(top)
e.pack(fill="x")

#this is responsible for page transition
nextButton = tkinter.Button(top, text = "Next", command = nextCallback)
nextButton.pack(side = 'bottom') #align to the bottom of the window


#These frames are kind of weird because they use scrollbars
	#basically you have to put a Frame (used to hold the widgets) inside of a Canvas, 
	# attach the Canvas to a Scrollbar,
	# then put both inside of another Frame (to hold the Canvas/Scrollbar)
#its just mostly some boilerplate functionality to allow scrolling


leftside =  tkinter.Frame(top)
canvas = tkinter.Canvas(leftside)
buttonHolder=tkinter.Frame(canvas)
myscrollbar=tkinter.Scrollbar(leftside,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=500,height=600)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left", fill = 'x')
canvas.create_window((0,0),window=buttonHolder, width=500,height=600)
buttonHolder.bind("<Configure>",myfunction)


#this is called when you press any given button. It changes the color to red/resets it to the default
def colsCallback(index) :

	defaultbg = top.cget('bg') #get the default background color from the main window
	if(buttonsList[index].cget('bg') ==  "red") :
		buttonsList[index].configure(bg = defaultbg)
		buttonsList[index].configure(activebackground = defaultactivebg)
	else :
		buttonsList[index].configure(bg = "red")
		buttonsList[index].configure(activebackground = "red")


buttonsList = []

#this creates the actual buttons. Parses the XLSX and then creates Button objects in a loop. 

#I added the row number/letter so you don't have to count down to the 15th row 
# when working from the mappings doc

def createButtons() :

	xl_workbook = xlrd.open_workbook(filename)
	xl_sheet = xl_workbook.sheet_by_index(0)
	row = xl_sheet.row(1)  # 1st row

	for idx, cell_obj in enumerate(row) :

		b2 = tkinter.Button(buttonHolder, text = str(idx) + "/" + chr(idx+97) + " " + cell_obj.value, command = partial(colsCallback, idx))
		#partial() is used to provide an argument to colsCallback()

		b2.pack(fill = "x")
		buttonsList.append(b2)


#this is the right side pane, which is used to input the column names
rightside =  tkinter.Frame(top)
canvas2 = tkinter.Canvas(rightside)
entryHolder=tkinter.Frame(canvas2)
myscrollbar2=tkinter.Scrollbar(rightside,orient="vertical",command=canvas2.yview)
canvas2.configure(yscrollcommand=myscrollbar2.set)

def myfunction2(event):
    canvas2.configure(scrollregion=canvas2.bbox("all"),width=200,height=600)

myscrollbar2.pack(side="right",fill="y")
canvas2.pack(side="left", fill = 'x')
canvas2.create_window((0,0),window=entryHolder, width=200,height=600)
entryHolder.bind("<Configure>",myfunction2)



#this is the middle pane, which displays the mapping, like 'row[3]+row[6]+row[7]'
middle =  tkinter.Frame(top)
canvas3 = tkinter.Canvas(middle)
labelHolder=tkinter.Frame(canvas3)
myscrollbar3=tkinter.Scrollbar(middle,orient="vertical",command=canvas3.yview)
canvas3.configure(yscrollcommand=myscrollbar3.set)

def myfunction3(event):
    canvas3.configure(scrollregion=canvas3.bbox("all"),width=200,height=600)

myscrollbar3.pack(side="right",fill="y")
canvas3.pack(side="left", fill = 'x')
canvas3.create_window((0,0),window=labelHolder, width=200,height=600)
labelHolder.bind("<Configure>",myfunction3)

entryList = [] #holds the entries (right side pane -- they are text input fields)
labelList = [] #holds the labels (middle pane -- they are static text once they are created)


#this is run when you click the add button
#functionally, it adds the mapping as a new label, and creates a new Entry
#TODO: autofill the entry if it is not a summation
	#label names like this are basically copied over, or at least its a good place to start
def addLabelCallback() :

	defaultbg = top.cget('bg')
	labelText = ''
	#loop through the buttons and check if they are red -- this means they have been clicked
	#this is pretty unclean code practice but whatever
	for idx, button in enumerate(buttonsList):
		if(button.cget('bg') ==  "red") :

			#reset the color to the default
			button.configure(bg = defaultbg)
			button.configure(activebackground = defaultactivebg)

			labelText = labelText + "row[" + str(idx) + "]" + "+"

	#chop the extra plus sign
	labelText = labelText[:-1]

	#lframe/eframe are used here to maintain a fixed height
	# so the labels/Entry fields line up properly
		#this was way too annoying to do with tkinter widgets
	lframe = tkinter.Frame(labelHolder)
	lframe.pack()
	lframe.pack_propagate(0)

	#heres the actual label
	l2 = tkinter.Label(lframe)
	l2.configure(text=labelText)
	l2.pack()

	lframe.configure(height = 25)
	lframe.pack(fill = "both")
	labelList.append(l2)

	eframe = tkinter.Frame(entryHolder)
	eframe.pack()
	eframe.pack_propagate(0)

	#heres the actual Entry
	e2 = tkinter.Entry(eframe)
	e2.insert(0, "entry text")
	e2.pack()

	eframe.configure(height = 25)
	eframe.pack(fill = "both")
	entryList.append(e2)

#this is run when you hit the finish button
#it does some formatting on the DataQuery string
	#TODO: probably should move that formatting stuff over to writeClassFile.py
#

def finishCallback() :

	#this adds the '%d' part of the DataQuery string
	dataQueryStr = "\""
	for label in labelList :
		dataQueryStr = dataQueryStr + "%d, "
	#chop the extra ', ' and add closing quotes
	dataQueryStr = dataQueryStr[:-2]
	dataQueryStr = dataQueryStr + "\""

	#this puts the row[x] values into 'int(row[x]),' form
	dataQueryStr = dataQueryStr + " %(\n"
	for label in labelList :
		dataQueryStr = dataQueryStr + "\t\t\t\tint(" + label.cget("text") + "),\n"
	
	dataQueryStr = dataQueryStr[:-2]
	dataQueryStr = dataQueryStr + ")"

	#get the string value from each Entry in the list
	colNamesList = []
	for entry in entryList :
		colNamesList.append(entry.get())

	#call the function from writeClassFile.py, with the args from this file
	writeFile(tableName, colNamesList, dataQueryStr)

	#close the window
	top.destroy()


#this holds the Add/Finish buttons, so they are side by side & snapped to the bottom of the screen
bottomButtons = tkinter.Frame(top)
addButton = tkinter.Button(bottomButtons, text = "Add", command = addLabelCallback)
addButton.pack(side = "left")
finishButton = tkinter.Button(bottomButtons, text = "Finish", command = finishCallback)
finishButton.pack(side = "left")


top.mainloop()
