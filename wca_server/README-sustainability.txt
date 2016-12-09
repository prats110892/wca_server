***Use Case/Purpose***
	This tool is meant as a demonstration of the sustainability workflow within the WCA Data Danager application. It is written in Python, and this workflow isn't currently available wihtin the web application. It could be added, though, using this tool as the base of the workflow. 
	The main use case here is when you need to add a new class of data into the system. Right now, we have the existing data categories pre-defined as Python classes within the 'tables' folder on the root directory. Adding a new category of data would entail creating a new Python class file, and this tool functions as a GUI to do so. The important metadata that a Python table class hold includes column names (such as "Own Child - Biological")  for the SQL database and mappings from the data spreadsheet to the attributes of the SQL database (such as column 5 -> "Own child - stepchild"). The reason that we have to specify these mappings is because sometimes, columns are dropped from the spreadsheets and some SQL attributes are composed of summations of multiple spreadsheet colummns. 

***Installation/Dependencies***

	The main dependency for this file is the python module Tkinter. This is the de facto standard GUI library for Python which utilizes the Tcl/Tk widget toolkit. To run this program, you will also likely need to install Tcl/Tk. 
This should be straightforward on a Linux machine (sudo apt-get Tk8.5 on Ubuntu, for example). 
On Windows/Mac, the easiest way to install Tcl/Tk seems to be using Activetcl (http://www.activestate.com/activetcl)

You may also need to install the Python module XLRD ('pip install xlrd' on a terminal).

***To test your Tcl/Tk installation***
run 'python -m tkinter' on the command line to see if Tkinter is set up properly
- this should bring up a little GUI frame with a 'click me' button on it
If it doesn't run, this probably means there is an issue with your Tcl/Tk install	
	

***Program Usage***
The GUI consists of 2 dialog pages.
Page 1 is for file selection. Pressing the 'Open file...' button will bring up a local file selector. You use this dialog to select an XLSX file. (TODO: switch to CSV instead of XLSX).
It copies the filename into an entry box. This is to be used in the database as the table name. You probably want to delete the 'ACS_14_5YR_B09018_' part, so it looks like Relationship_Children for example. Click 'Next' to move on to page 2 when you are ready. 

Page 2 is where you define the mappings and column names. It is split into 3 panes:

On the left is a list of columns. They are clickable buttons, and turn red when you click. This is used to select columns for spreadsheet-to-database mappings. You can click multiple buttons for a more advanced mapping, such as a summation. When you have a mapping ready, click 'Add'

The middle column shows mappings (from columns of the input spreadsheet to SQL attributes). 
This column gets populated with the mappings one at a time as you click 'Add'. Selecting multiple columns will default to summation, but you can change the math operator by editing the entry field

The right column is a list of column names. 
This will also be populated with fields one at a time as you click 'Add'. It pre-fills column names, but you can type in the actual column name if you need to change it. 
		
		
When you hit 'Finish', it will create the <tablename>_table.py class definition file. It will probably overwrite whatever is there, so watch out. It calls the helper file writeclassFile.py to do the actual file writing. 

***Example***
Video demonstration here if you'd like: 
https://www.youtube.com/watch?v=f3v798SskNQ

So to create a class definition for Relationship_Children as an example
	-run 'python CreateTableClass.py'
	-open the spreadsheet, ACS_14_5YR_B09018_Relationship_Children.XLSX
	-change the name in the entry field to Relationship_Children
	-hit next
	On the next page, do the mappings:
		-press 'total' button, hit 'add'
		-press 'biological' button, hit 'add'
		-press 'adopted' button, hit 'add'
		-press 'stepchild' button, hit 'add'
		-press 'grandchild' button, hit 'add'
		-press 'other relatives' button, hit 'add'
		-press 'foster' button, hit 'add'
		-change the column names if you'd like
		-hit finish.
This will output the relationship_children.py table definition.

				
TODO:
-Scrolling issues
-The __init__.py file and categories.py file will need to be updated to put this table into the web application
-do some null checking, so you don't accidentally add blank mappings or something



