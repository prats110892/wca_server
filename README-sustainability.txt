	Usage: 
	The GUI consists of 2 dialog pages:
		Page 1 is for file selection. Pressing the 'open file...' button will bring up a local file selecter
			-grab the xlsx file 
			-(TODO: switch to CSV instead of XLSX)
		It copies the local name into an entry box. This is used for the table name. 
			-you probably want to delete the 'ACS_14_5YR_B09018_' part, so it looks like Relationship_Children for example
		Click 'Next' to move on to page 2 when youre ready

		Page 2 is where you define the mappings and column names. 
		It is split into 3 panes
			On the left is a list of columns. They are clickable buttons, and turn red when you click.
				-This is used to select columns for mappings. You can click multiple buttons for a column summation
				-Click 'Add' when you have a mapping ready
			The middle column is of mappings (from spreadsheet columns to SQL attributes)
				-This will be populated with the mappings one at a time as you click 'Add'
				-Selecting multiple columns will default to summation, but you can change the math operator by editing the entry field
			The right column is a list of Entry fields. You use this to define the column names. 
				-This will be populated with fields one at a time as you click 'Add'. 
				-You can type in the actual column name
		When you hit 'Finish', it will create the tablename_table.py class definition file. 
			-It will probably overwrite whatever is there, so watch out. 
			-It calls writeclassFile.py to do the actual file writing. 
			TODO: close the window when you hit 'Finish'

	So to create a class for Relationship_Children as an example
		-run this script
		-open the XLSX
		-change the name in the entry field to Relationship_Children
		-hit next
		-do the mappings: (no sums in this one, but they are straightforward: press multiple column buttons)
			-press 'total' button, hit 'add'
			-press 'biological' button, hit 'add'
			-press 'adopted' button, hit 'add'
			-press 'stepchild' button, hit 'add'
			-press 'grandchild' button, hit 'add'
			-press 'other relatives' button, hit 'add'
			-press 'foster' button, hit 'add'
		-change the column names
		-hit finish.
		Will output the .py table definition.
		The formatting is a slightly off from what we have, but I think it ought to work normally. 
		 	-you still have to manually change the __init__.py file for now
			
			
TODO:
-Scrolling issues
-figure something out for the __init__.py file updating 
-do some null checking, so you don't accidentally add blank mappings or something



