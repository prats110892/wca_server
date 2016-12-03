# Overview

These files run the server for the Data Dashboard upload wizard. Functionality includes 
  -uploading new data (such as Demographic, Housing or Education data)
  -uploading new calculations files (in case the region barriers are to change
  -downloading a formatted CSV for a type of data and a given region (Ex: Race data for the NPU regions)
  
# Architecture
wca_server.py is the top-level file which is used to run the server. It calls a variety of other files to provide the functionality present within our tool. 

The classes of data (such as Race, Relationship_Children, or Median_Age_Sex) are defined by Python class files within the Tables folder. These contain all the metadata needed for the creation of an SQL table (attribute names) and the parsing of the spreadsheet which is uploaded into the system (mappings from rows in the raw CSV file to SQL attributes). 

A primary use of the system is to upload a raw CSV file (which comes from the US Census usually), and put it into the database. You can also retrieve the formatted CSV which is used on the Data Dashboard itself. The key difference between the original file and the formatted file is that the original contains data for each census block, and the formatted data contains sums for larger regions such as NPU, ZIP code or Neighborhood. 

The system also allows for data access in the JSON standard, which can be used to write data-scraping programs without the necessity of parsing through a CSV. 
