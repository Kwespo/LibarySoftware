#Imports
import sqlFunc as sqf
import fileFunc as ff

# Create instances of the classes
dbCursor = sqf.SQLFunc()
fileCursor = ff.FileFunc()
"""
print(dbCursor.return_All_Doc())

print(dbCursor.docNames())

print(dbCursor.search_For_File(dName='atp27c')[0][0])
"""

# Use the data
file = dbCursor.search_For_File(dName='jp3-09.3(CAS)')
print(file)
fileCursor.display_File(file[0][0])